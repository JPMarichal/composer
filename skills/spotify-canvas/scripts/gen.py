"""Genera material para un Spotify Canvas vía la API HTTP de ComfyUI (solo stdlib).

  python gen.py image --prompt "..." [--seed N] [--width 576 --height 1024] [--prefix canvas_start]
  python gen.py video --image archivo_en_ComfyUI/input.png --prompt "..." [--negative "..."] [--seed N]
                      [--width 448 --height 800 --length 97 --steps 20]

Requisitos: ComfyUI en marcha (COMFY_API, por defecto http://127.0.0.1:8188), nodo ComfyUI-GGUF instalado
y los modelos de comfyui-models/ (ver SKILL.md). Imprime el JSON de salidas de ComfyUI al terminar.
"""
import argparse, json, os, sys, time, urllib.error, urllib.request

API = os.environ.get("COMFY_API", "http://127.0.0.1:8188")


def post(path, data):
    req = urllib.request.Request(API + path, json.dumps(data).encode(), {"Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        sys.exit(e.read().decode()[:3000])


def run(graph):
    pid = post("/prompt", {"prompt": graph})["prompt_id"]
    while True:
        h = json.load(urllib.request.urlopen(f"{API}/history/{pid}"))
        if pid in h:
            st = h[pid]["status"]
            if st["status_str"] != "success":
                sys.exit(json.dumps(st["messages"][-3:], indent=1)[:3000])
            return h[pid]["outputs"]
        time.sleep(5)


def image_graph(a):
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "z_image_turbo_nvfp4.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen_3_4b_fp8_mixed.safetensors", "type": "lumina2", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "ae.safetensors"}},
        "4": {"class_type": "ModelSamplingAuraFlow", "inputs": {"model": ["1", 0], "shift": 3.0}},
        "5": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": a.prompt}},
        "6": {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": ["5", 0]}},
        "7": {"class_type": "EmptySD3LatentImage", "inputs": {"width": a.width, "height": a.height, "batch_size": 1}},
        "8": {"class_type": "KSampler", "inputs": {"model": ["4", 0], "positive": ["5", 0], "negative": ["6", 0],
              "latent_image": ["7", 0], "seed": a.seed, "steps": 8, "cfg": 1.0, "sampler_name": "euler",
              "scheduler": "simple", "denoise": 1.0}},
        "9": {"class_type": "VAEDecode", "inputs": {"samples": ["8", 0], "vae": ["3", 0]}},
        "10": {"class_type": "SaveImage", "inputs": {"images": ["9", 0], "filename_prefix": a.prefix}},
    }


def video_graph(a):
    return {
        "1": {"class_type": "UnetLoaderGGUF", "inputs": {"unet_name": "Wan2.2-TI2V-5B-Q4_K_M.gguf"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "umt5_xxl_fp8_e4m3fn_scaled.safetensors", "type": "wan", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "Wan2.2_VAE.pth"}},
        "4": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["1", 0], "shift": 8.0}},
        "5": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": a.prompt}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": a.negative}},
        "7": {"class_type": "LoadImage", "inputs": {"image": a.image}},
        "8": {"class_type": "Wan22ImageToVideoLatent", "inputs": {"vae": ["3", 0], "width": a.width, "height": a.height,
              "length": a.length, "batch_size": 1, "start_image": ["7", 0]}},
        "9": {"class_type": "KSampler", "inputs": {"model": ["4", 0], "positive": ["5", 0], "negative": ["6", 0],
              "latent_image": ["8", 0], "seed": a.seed, "steps": a.steps, "cfg": 5.0, "sampler_name": "uni_pc",
              "scheduler": "simple", "denoise": 1.0}},
        "10": {"class_type": "VAEDecode", "inputs": {"samples": ["9", 0], "vae": ["3", 0]}},
        "11": {"class_type": "CreateVideo", "inputs": {"images": ["10", 0], "fps": 24.0}},
        "12": {"class_type": "SaveVideo", "inputs": {"video": ["11", 0], "filename_prefix": "video/canvas",
               "format": "mp4", "codec": "h264"}},
    }


p = argparse.ArgumentParser()
p.add_argument("stage", choices=["image", "video"])
p.add_argument("--prompt", required=True)
p.add_argument("--negative", default="text, letters, logo, watermark, hat, photorealistic, fast motion, flashing, "
               "camera shake, blurry, distorted hands, extra people")
p.add_argument("--image", help="video: nombre del PNG ya copiado a ComfyUI/input")
p.add_argument("--seed", type=int, default=777123)
p.add_argument("--width", type=int)
p.add_argument("--height", type=int)
p.add_argument("--length", type=int, default=97, help="frames; 4n+1 (97 = 4.04 s a 24 fps)")
p.add_argument("--steps", type=int, default=20)
p.add_argument("--prefix", default="canvas_start")
a = p.parse_args()
if a.stage == "video" and not a.image:
    p.error("video requiere --image")
a.width = a.width or (576 if a.stage == "image" else 448)
a.height = a.height or (1024 if a.stage == "image" else 800)
print(json.dumps(run(image_graph(a) if a.stage == "image" else video_graph(a)), indent=1))
