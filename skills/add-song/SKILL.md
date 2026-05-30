---
name: add-song
description: Registrar canciones existentes (ya compuestas) en el repositorio. Activar cuando el usuario diga "te daré canciones que aún no tienes", "aquí tienes una canción", "registra esta", "add this song", o cualquier variante de añadir una canción ya compuesta al directorio canciones/. NO confundir con compositor (que compone desde cero). Este skill es para archivar, documentar y verificar canciones que el usuario ya tiene escritas/generadas.
---

# Add Song — Registro de Canciones Existentes

## Workflow

### 1. Recibir los datos del usuario

El usuario entrega: letra (con meta-tags), género, BPM, y contexto de creación. Tomar nota de todo.

### 2. Leer specs relevantes

- `specs/003-file-template.md` — estructura del archivo y reglas de formato
- `specs/002-anti-ai-isms.md` — safeguards, léxico prohibido, validación moral
- `specs/004-suno-syntax.md` — reglas de corchetes vs. paréntesis
- `corpus/007-fonetica-acustica.md` §5 — verificación fonética

### 3. Analizar la letra

- **Estructura**: identificar secciones (Intro, Verse, Chorus, Bridge, Outro, etc.)
- **Esquema de rima**: documentar tipo (consonante/asonante) por sección
- **Métrica**: detectar versos quebrados, variaciones de sílaba
- **Léxico**: cazar palabras del listado prohibido (§1), AI-ismos semánticos (§3), verbos forzados (§4b)
- **Moral**: verificar §7 (sin alcohol/drogas/sexo promocionado, principios edificantes)
- **Sintaxis Suno**: verificar que instrucciones de producción usen `[ ]` no `( )` (§Checklist de spec 004)

### 4. Generar archivo

Usar `just template "Título" "Género"` o escribir manualmente siguiendo `specs/003-file-template.md`.

El archivo debe incluir:

- **Metadatos** (Notion DB + producción musical)
- **Armonía** (progresión, patrón rítmico, tabla de acordes por sección)
- **Descripción** (formato 5-partes: hook → tesis → simbolismo → conexión → cierre, máx 2 párrafos)
- **Style Prompt** (fórmula 6-componentes, ≤1000 chars)
- **Letra** con meta-tags `[ ]`
- **Esquema de rima**
- **Checklist Anti-AI** (21 safeguards de spec 002)
- **Verificación Fonética** (4 filtros de corpus/007 §5)
- **Changelog de Autoría**

### 5. Verificar

- 21 safeguards del checklist anti-AI
- 4 filtros fonéticos (clímax, legato, rítmico, prueba del susurro)
- Sintaxis Suno: `[ ]` para instrucciones, `( )` para ad-libs cantados

### 6. Publicar (Notion→Ingest→Push)

Un solo comando hace todo:

```bash
just publish-song "canciones/<titulo-en-kebab-case>.md" "add song: <título>"
```

Esto: sincroniza a Notion (crea/actualiza página + escribe NotionPageID), indexa en vector store, y hace git commit + push.

## Referencias

Todos los specs están en `specs/` y `corpus/` del proyecto. No hay documentación duplicada aquí.
