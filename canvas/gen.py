"""Genera el fotograma inicial (z_image_turbo) y el clip (Wan2.2 TI2V 5B GGUF) vía API de ComfyUI."""
import json, sys, time, urllib.request

API = "http://127.0.0.1:8188"


def post(path, data):
    req = urllib.request.Request(API + path, json.dumps(data).encode(), {"Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        print(e.read().decode()[:3000]); sys.exit(1)


def run(graph):
    pid = post("/prompt", {"prompt": graph})["prompt_id"]
    while True:
        h = json.load(urllib.request.urlopen(f"{API}/history/{pid}"))
        if pid in h:
            st = h[pid]["status"]
            if st["status_str"] != "success":
                print(json.dumps(st["messages"][-3:], indent=1)[:3000]); sys.exit(1)
            return h[pid]["outputs"]
        time.sleep(5)


IMG_PROMPT = ("Vertical hand-painted storybook illustration, soft gouache and flat 2D animation style, warm golden "
              "hour, quiet neighborhood street with a row of old wooden utility poles, a young man about 20 years old with a full head of thick wavy dark hair, youthful face, in a suit and tie, "
              "bare-headed, seen from the side, carefully carving something into a wooden pole "
              "with a small pocket knife, wood shavings falling, cozy houses and a street lamp in the background, "
              "centered composition, no text, no hat")
VID_PROMPT = ("Gentle fluid 2D animation, the young man slowly carves into the wooden pole with small hand movements, "
              "wood shavings drift down, leaves and wires sway softly in the breeze, warm sunset light shimmers. "
              "Static camera, calm smooth motion, illustrated painterly style")
NEG = ("text, letters, logo, watermark, hat, cap, photorealistic, fast motion, flashing, camera shake, blurry, "
       "distorted hands, extra people, multiple characters")

stage = sys.argv[1]
if stage == "image":
    g = {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "z_image_turbo_nvfp4.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen_3_4b_fp8_mixed.safetensors", "type": "lumina2", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "ae.safetensors"}},
        "4": {"class_type": "ModelSamplingAuraFlow", "inputs": {"model": ["1", 0], "shift": 3.0}},
        "5": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": IMG_PROMPT}},
        "6": {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": ["5", 0]}},
        "7": {"class_type": "EmptySD3LatentImage", "inputs": {"width": 576, "height": 1024, "batch_size": 1}},
        "8": {"class_type": "KSampler", "inputs": {"model": ["4", 0], "positive": ["5", 0], "negative": ["6", 0],
              "latent_image": ["7", 0], "seed": 777123, "steps": 8, "cfg": 1.0, "sampler_name": "euler",
              "scheduler": "simple", "denoise": 1.0}},
        "9": {"class_type": "VAEDecode", "inputs": {"samples": ["8", 0], "vae": ["3", 0]}},
        "10": {"class_type": "SaveImage", "inputs": {"images": ["9", 0], "filename_prefix": "canvas_postes_start"}},
    }
else:
    g = {
        "1": {"class_type": "UnetLoaderGGUF", "inputs": {"unet_name": "Wan2.2-TI2V-5B-Q4_K_M.gguf"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "umt5_xxl_fp8_e4m3fn_scaled.safetensors", "type": "wan", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "Wan2.2_VAE.pth"}},
        "4": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["1", 0], "shift": 8.0}},
        "5": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": VID_PROMPT}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": NEG}},
        "7": {"class_type": "LoadImage", "inputs": {"image": sys.argv[2]}},
        "8": {"class_type": "Wan22ImageToVideoLatent", "inputs": {"vae": ["3", 0], "width": 448, "height": 800,
              "length": 97, "batch_size": 1, "start_image": ["7", 0]}},
        "9": {"class_type": "KSampler", "inputs": {"model": ["4", 0], "positive": ["5", 0], "negative": ["6", 0],
              "latent_image": ["8", 0], "seed": 20261029, "steps": 20, "cfg": 5.0, "sampler_name": "uni_pc",
              "scheduler": "simple", "denoise": 1.0}},
        "10": {"class_type": "VAEDecode", "inputs": {"samples": ["9", 0], "vae": ["3", 0]}},
        "11": {"class_type": "CreateVideo", "inputs": {"images": ["10", 0], "fps": 24.0}},
        "12": {"class_type": "SaveVideo", "inputs": {"video": ["11", 0], "filename_prefix": "video/canvas_postes",
               "format": "mp4", "codec": "h264"}},
    }
print(json.dumps(run(g), indent=1))
