import os
from openai import OpenAI
import numpy as np
import faiss
from dotenv import load_dotenv

knowledge_path = "knowledge_base"

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), timeout=60.0)


def load_data():
    documents = []
    for file_name in os.listdir(knowledge_path):
        if file_name.endswith(".md"):
            with open(os.path.join(knowledge_path, file_name), "r", encoding="utf-8") as f:
                text = f.read().strip()
                documents.append(text)

    print(f"Loaded {len(documents)} documents")
    print("Sample content:", documents[0][:200], "...") 
    return documents

def create_embeddings(documents):
    embeddings_list = []
    for doc in documents:
        response = client.embeddings.create(
            model="text-embedding-3-large",
            input=doc
        )
        embedding_vector = response.data[0].embedding
        embeddings_list.append(np.array(embedding_vector, dtype=np.float32))
    np.save("embeddings.npy", embeddings_list)
    print("Embeddings created for all documents")
    return embeddings_list
    
def store_embeddings(embeddings,documents):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)  # L2 = Euclidean distance
    index.add(np.stack(embeddings))
    faiss.write_index(index, "knowledge_index.faiss")
    np.save("documents.npy", documents) 
    
    print(f"FAISS index created with {index.ntotal} vectors")
    
def main():
    # documents = load_data()
    # embeddings = create_embeddings(documents)
    # store_embeddings(embeddings,documents)
    index = faiss.read_index("knowledge_index.faiss")
    docs = np.load("documents.npy", allow_pickle=True)
    
    print(index.ntotal)
    print(docs[0][:100])
    
if __name__ == "__main__":
    main()