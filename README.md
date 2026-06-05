# Agentic HR Policy Assistant

An AI-powered multi-agent HR policy assistant built with **RAG (Retrieval-Augmented Generation)**, local LLMs (Ollama), and LlamaIndex.
The system routes user queries through specialized agents (HR, Policy, Compliance) and generates **traceable answers with citations** from internal documents.

---

##  Project Overview

This project simulates a real-world enterprise AI assistant that can answer HR-related questions such as:

* Remote work policies
* Employee guidelines
* Compliance regulations
* Internal HR procedures



---
##  Architecture

* **LlamaIndex** : document ingestion & retrieval
* **Ollama (Mistral)** : local LLM inference
* **HuggingFace Embeddings** : semantic search
* **Vector Store Index** : document retrieval
* **Custom Agents** : routing & domain specialization

---

##  Tech Stack

* Python 3.10+
* LlamaIndex
* Ollama (Mistral)
* HuggingFace Transformers
* SentenceTransformers
* RAG (Retrieval-Augmented Generation)
* Gradio (UI optional)

---

##  Project Structure

```
hr-policy-agent/
│
├── core/
│   ├── router.py
│   ├── agent.py
│   ├── index.py
│
├── data/
│   └── hr_policy/
│
├── ingest.py
├── query.py
├── storage/ (not included in repo)
│
├── requirements.txt
└── README.md
```

---

##  Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Ollama

```bash
ollama run mistral
```

### 3. Build index

```bash
python ingest.py
```

### 4. Run query engine

```bash
python query.py
```

---

##  Example

**Input:**

```
Kann ich im Homeoffice arbeiten?
```


GitHub: https://github.com/liuxustudio
LinkedIn: [www.linkedin.com/in/liuxu-lu](http://www.linkedin.com/in/liuxu-lu)
