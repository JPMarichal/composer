#!/bin/bash
# Copia a la carpeta de fotogramas cada imagen nueva y avisa por lotes de 3.
D=/d/myapps/composer/youtube/mentira-que-te-menti/imgs
P='P:/Canciones/audio/wav/love/assets/fotogramas/mentira-que-te-menti'
mkdir -p "$P"
pend=()
while true; do
  for f in "$D"/*.png; do
    [ -e "$f" ] || continue
    b=$(basename "$f")
    if [ ! -e "$P/$b" ]; then
      sleep 4
      cp "$f" "$P/$b" && pend+=("$b")
    fi
  done
  total=$(ls "$P"/*.png 2>/dev/null | wc -l)
  if [ ${#pend[@]} -ge 3 ] || { [ "$total" -ge 30 ] && [ ${#pend[@]} -gt 0 ]; }; then
    echo "LOTE listo ($total/30): ${pend[*]}"
    pend=()
  fi
  [ "$total" -ge 30 ] && break
  sleep 20
done
echo "FIN: 30/30 copiadas"
