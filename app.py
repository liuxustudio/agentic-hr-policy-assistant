import gradio as gr

def chat(question, history):
    nodes = retriever.retrieve(question)
    answer = "\n\n".join([
        f"📄 {n.metadata.get('file_name')} | Seite {n.metadata.get('page_label', '?')}\n{n.text[:300]}"
        for n in nodes
    ])
    return answer

gr.ChatInterface(fn=chat, title="HR Policy Assistant").launch()