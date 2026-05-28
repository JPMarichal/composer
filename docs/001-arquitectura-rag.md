# ADR-001: Arquitectura del sistema RAG para composición musical

## Estado

Aceptado

## Contexto

Necesitamos un sistema que permita realizar consultas textuales y semánticas sobre un corpus de conocimiento musical, las especificaciones del proyecto y la documentación de desarrollo, para asistir en la composición de canciones.

## Decisión

Implementaremos un sistema RAG (Retrieval-Augmented Generation) con la siguiente arquitectura:

- **Vector store local**: Almacén vectorial JSON con embeddings generados localmente
- **Embeddings**: nomic-embed-text vía Ollama (local)
- **LLM**: Gemma4 vía Ollama (local)
- **Chunking**: RecursiveCharacterTextSplitter con chunks de 1000 chars y overlap de 200
- **Búsqueda**: Similaridad coseno sobre vectores

## Fuentes de conocimiento

- `corpus/` → Teoría musical, estructuras de canciones, armonía, letras de referencia
- `specs/` → Especificaciones del sistema, contratos de módulos
- `docs/` → Documentación técnica, ADRs, decisiones de desarrollo

## Consultas

Toda consulta de composición hace RAG sobre los tres directorios simultáneamente.
