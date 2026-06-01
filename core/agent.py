from core.index import retriever
from llama_index.llms.ollama import Ollama

llm = Ollama(model="mistral", temperature=0.1)

def build_context(question):
    nodes = retriever.retrieve(question)

    context = ""
    for i, n in enumerate(nodes):
        context += f"[{i+1}] {n.text}\n\n"

    return context, nodes


def hr_agent(question):
    return _run_agent("HR", question)


def policy_agent(question):
    return _run_agent("POLICY", question)


def compliance_agent(question):
    return _run_agent("COMPLIANCE", question)


def _run_agent(role, question):
    context, nodes = build_context(question)

    prompt = f"""
You are a {role} assistant.

Use ONLY the context below.
Answer the question clearly.

Add citations like [1][2] when using context.

Context:
{context}

Question:
{question}
"""

    answer = llm.complete(prompt).text

    return answer, nodes