# Especificación: Gestión de Proyectos en Suno AI (API)

Basado en ingeniería inversa de la API de Suno AI. No hay documentación oficial pública de estos endpoints.

## Problema

Suno no expone una función "mover a proyecto" en su interfaz web; solo se puede asignar una canción una vez durante la creación. Las canciones sin proyecto caen en "My Workspace" (Unassigned). El Suno MCP no tiene herramientas de gestión de proyectos.

La API REST de Suno sí lo permite: es posible **agregar** clips a un proyecto y **removerlos** de cualquier proyecto.

## Endpoints

### Listar proyectos del usuario

```
GET /api/project/me
```

Respuesta: `{ "projects": [ { "id": "...", "name": "...", "clip_count": N }, ... ] }`

### Obtener detalle de un proyecto (incluye clips)

```
GET /api/project/{project_id}
```

### Obtener clips de un proyecto

```
GET /api/project/{project_id}/clips
```

### Agregar clips a un proyecto

```
POST /api/project/{project_id}/clips
Content-Type: application/json

{
  "update_type": "add",
  "metadata": {
    "clip_ids": ["uuid1", "uuid2", ...]
  }
}
```

- Respuesta exitosa: HTTP 204 (sin cuerpo)
- No usa wrapper `spec`; `update_type` y `metadata` van en la raíz del JSON.
- Los clip_ids deben ser UUIDs completos (ej. `53598994-8ab0-4902-8a61-a52bd278765f`), no truncados. UUIDs truncados devuelven HTTP 400 "Invalid clip_ids sent".

### Remover clips de un proyecto

```
POST /api/project/{project_id}/clips
Content-Type: application/json

{
  "update_type": "remove",
  "metadata": {
    "clip_ids": ["uuid1", "uuid2", ...]
  }
}
```

- Respuesta exitosa: HTTP 204 (sin cuerpo)

### Obtener todos los clips del usuario (feed paginado)

```
GET /api/feed/v2?page=N
```

- Respuesta: `{ "data": [ ... ], "has_next": bool }`
- Cada clip incluye `id`, `title`, `project_id`, `project_name`, `status`, etc.

## Reglas del negocio

1. **Un clip puede estar en múltiples proyectos simultáneamente.** Esto es inusual: la UI de Suno muestra un solo proyecto por clip, pero la API permite tener el mismo clip en N proyectos.
2. **Mover un clip existente** requiere dos llamadas: `remove` del proyecto origen + `add` al proyecto destino. Si el clip ya está en el destino, `add` es no-op (no hay error).
3. **Clips sin proyecto** tienen `project_id: null` y/o aparecen en proyectos llamado vacío o "My Workspace" (que en la API se devuelve como `project_name: "Unassigned"`).
4. **El límite de batch** es desconocido; por seguridad se envían de a 50 clips por llamada.

## Scripts disponibles

### `scripts/suno-move-clips.py`

Mueve clips entre proyectos buscándolos por título en el índice local.

```bash
# Mover clips a un proyecto destino
just suno-move-clips "Singles" "Mamá" "si vuelvo"

# Mover clips DESDE un proyecto específico (remove + add)
just suno-move-clips-from "Fronteras" "Singles" "Mamá" "si vuelvo"
```

El script:
1. Busca coincidencias por título en `suno-index.json` (todos los términos deben aparecer, case-insensitive)
2. Si se usa `--from`, remueve los clips del proyecto origen antes de agregarlos al destino
3. Agrega los clips al proyecto destino
4. Verifica que los clips hayan llegado consultando `GET /api/project/{destino}/clips`

### `scripts/suno-index.py`

Indexa el feed completo de clips y los guarda en `suno-index.json`. Ahora también **actualiza** el `project_name` y otros campos mutables de clips existentes (no solo añade nuevos).

```bash
just suno-index
```

### `scripts/suno-search.py`

Busca clips en el índice local por título.

```bash
just suno-search "término"
```

### `scripts/suno-stats.py`

Resumen del catálogo por proyecto.

```bash
just suno-stats
```

## Mantenimiento del índice local

El índice (`suno-index.json`) se actualiza correctamente si se ejecuta `just suno-index` después de mover clips. El script ahora parchea `project_name`/`project_id` de clips existentes cuando estos cambian en la API.

**No se actualiza automáticamente** — hay que ejecutar `just suno-index` periódicamente o después de operaciones de movimiento.

## IDs de proyectos conocidos

| Proyecto | ID |
|----------|----|
| Singles | `22d6c3fd-d388-4a15-8f83-eeee3bbb02d0` |
| Fronteras | `25a3e114-b673-4178-9aa5-382ee663bb86` |
| Finished | (no documentado) |
| De poetas y sapoetas | (no documentado) |
