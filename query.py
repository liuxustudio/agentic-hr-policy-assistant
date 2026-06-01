import gradio as gr
from llama_index.core import StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)
retriever = index.as_retriever(similarity_top_k=2)

def chat(question, history):
    nodes = retriever.retrieve(question)
    if not nodes:
        return "Keine relevanten Informationen gefunden."


    answer_parts = []
    for i, node in enumerate(nodes):
        paragraphs = [p.strip() for p in node.text.split('\n\n') if p.strip()]
        for para in paragraphs:
            answer_parts.append(f"{para}")
        answer_parts.append("")


    citation_parts = ["\n---\n📚 **Quellen** *(zum Lesen aufklappen)*\n"]
    for i, node in enumerate(nodes):
        file_name = node.metadata.get('file_name', 'unknown')
        page = node.metadata.get('page_label', node.metadata.get('page', '?'))
        score = round(node.score, 3)
        paragraphs = [p.strip() for p in node.text.split('\n\n') if p.strip()]

        citation_parts.append(f"**[{i+1}] 📄 {file_name} | Seite {page} | Score: {score}**")
        for j, para in enumerate(paragraphs):
            citation_parts.append(f"> Absatz {j+1}: {para[:300]}")
        citation_parts.append("")

    return "\n".join(answer_parts) + "\n".join(citation_parts)

gr.ChatInterface(
    fn=chat,
    title="🤖 HR Policy Assistant",
    description="Fragen Sie nach HR-Richtlinien auf Deutsch.",

).launch()