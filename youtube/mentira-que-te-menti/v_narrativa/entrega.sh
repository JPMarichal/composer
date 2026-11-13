#!/bin/bash
# Copia imágenes nuevas a P: y avisa cada 3 (o al terminar).
SRC=/d/myapps/composer/youtube/mentira-que-te-menti/v_narrativa/imgs
DST=/p/Canciones/audio/wav/love/assets/fotogramas/mentira-que-te-menti-narrativa/imgs
mkdir -p "$DST"; new=0
while true; do
  for f in "$SRC"/*.png; do
    b=$(basename "$f"); [ -e "$DST/$b" ] && continue
    sz=$(stat -c %s "$f"); [ "$sz" -lt 200000 ] && { echo "NEGRA: $b"; continue; }
    sleep 3; cp "$f" "$DST/$b"; new=$((new+1)); n=$(ls "$DST"/*.png | wc -l)
    if [ $((new % 3)) -eq 0 ]; then echo "LOTE listo ($n/60): ultimas 3 en $DST"; fi
  done
  [ $(ls "$DST"/*.png 2>/dev/null | wc -l) -ge 60 ] && { echo "COMPLETO 60/60"; break; }
  sleep 20
done
