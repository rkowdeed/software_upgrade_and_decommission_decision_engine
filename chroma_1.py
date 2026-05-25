from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings()

db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding
)

db.add_texts(["Kafka lag is high", "CPU usage spike"])

docs = db.similarity_search("performance issue")