from llama_index.llms.ollama import Ollama

router_llm = Ollama(model="mistral", temperature=0)

def route_question(question: str) -> str:
    prompt = f"""
You are a router for an HR system.

Classify the question into ONE category:

- HR
- POLICY
- COMPLIANCE

Question:
{question}

Return ONLY one word.
"""

    result = router_llm.complete(prompt).text.strip().upper()


    return result