# Especificación: Sistema RAG para composición

## Descripción

Sistema de Retrieval-Augmented Generation que indexa y consulta el conocimiento del proyecto para asistir en la composición musical.

## Requisitos

- REQ-1: Indexar archivos .md y .txt de docs/, specs/ y corpus/
- REQ-2: Soportar consultas en lenguaje natural sobre el corpus indexado
- REQ-3: El LLM debe usar el contexto recuperado para responder
- REQ-4: Todo debe ejecutarse localmente (Ollama)
- REQ-5: La indexación debe ser incremental (reescaneo completo)

## Prompt del compositor

El sistema usa un prompt fijo que instruye al LLM a actuar como compositor profesional, usando el contexto recuperado para fundamentar sus respuestas.

## Métricas de chunking

- Tamaño de chunk: 1000 caracteres
- Overlap: 200 caracteres
- Retriever: top-6 chunks por consulta

## Stack tecnológico

- LangChain.js (orquestación)
- Ollama (embeddings + LLM local)
- nomic-embed-text (embeddings)
- gemma4 (generación)
