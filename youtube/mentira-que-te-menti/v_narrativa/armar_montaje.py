"""Arma tabla_montaje.json y transiciones_montaje.json: añade la portada al inicio y la tarjeta final al cierre.

Portada: 00_portada (0 a 3,5 s) y la primera imagen se corre a 3,5 s; la segunda a 7,0 s.
Cierre: 61_cierre entra a los 193,0 s (la última imagen conserva 4 s) y dura hasta el final del audio más la cola.
Los cortes de transiciones.json se desplazan un lugar por la portada que se inserta.
"""
import json

tabla = json.load(open("tabla.json", encoding="utf-8"))
assert len(tabla) == 60
tabla[0]["t"] = 3.5
tabla[1]["t"] = 7.0
tabla.insert(0, {"id": "00_portada", "t": 0.0, "letra": "(portada)", "kind": "C", "ref": None})
tabla.append({"id": "61_cierre", "t": 193.0, "letra": "(cierre)", "kind": "C", "ref": None})
json.dump(tabla, open("tabla_montaje.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

tr = json.load(open("transiciones.json", encoding="utf-8"))
cortes = {str(int(k) + 1): v for k, v in tr["cortes"].items()}
cortes["1"] = {"tipo": "Cross Dissolve", "dur": 1.0, "nota": "de la portada a la primera imagen"}
cortes["61"] = {"tipo": "Cross Dissolve", "dur": 1.0, "nota": "de la última imagen a la tarjeta final"}
json.dump({"default": tr["default"], "cortes": cortes}, open("transiciones_montaje.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(tabla), "planos;", len(cortes), "cortes con ajuste")
