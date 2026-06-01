from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os


DATA_PATH = "data/hr_policy"

documents = SimpleDirectoryReader(
    input_dir=DATA_PATH,
    recursive=True
).load_data()

print(f"Loaded {len(documents)} documents")


text_splitter = SentenceSplitter(
    chunk_size=256,
    chunk_overlap=50
)

Settings.text_splitter = text_splitter

# =========================
# 3. Embedding model（本地）
# =========================
embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

Settings.embed_model = embed_model

index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model,
    transformations=[text_splitter]
)


PERSIST_DIR = "./storage"


if os.path.exists(PERSIST_DIR):
    print("⚠️ removing old storage...")
    import shutil
    shutil.rmtree(PERSIST_DIR)

index.storage_context.persist(persist_dir=PERSIST_DIR)

print("✅ HR Policy index created and saved to ./storage")