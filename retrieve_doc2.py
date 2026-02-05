import faiss
import os
from dotenv import load_dotenv
import numpy as np
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), timeout=60.0)

QUESTION_EMB_FILE = "question_embeddings.npy"
QUESTION_TEXT_FILE = "questions.npy"

def embedding_question():
    if os.path.exists(QUESTION_EMB_FILE):
        question_embeddings = np.load(QUESTION_EMB_FILE)
        questions = np.load(QUESTION_TEXT_FILE).tolist()
    else:
        question_embeddings = []
        questions = []
        question = "Have you worked with real-time messaging systems?"
    
        response = client.embeddings.create(
            model="text-embedding-3-large",
            input=question
        )
        
        embedding  = np.array(
            response.data[0].embedding,
            dtype="float32"
        )
        questions.append(question)
        question_embeddings.append(embedding)
        
        question_embeddings = np.vstack(question_embeddings)
        
        #save question embeddings
        np.save(QUESTION_EMB_FILE, question_embeddings)
        np.save(QUESTION_TEXT_FILE, question_embeddings)
    
    print("Question embedding saved")
    return question_embeddings

def main():
    k = 3  # number of results to retrieve
    # Load stored index and documents
    index = faiss.read_index("knowledge_index.faiss")
    documents = np.load("documents.npy", allow_pickle=True)
    
    print(f"Loaded {index.ntotal} vectors")
    
    question_vector = embedding_question()
    distances, indices = index.search(question_vector, k)
    print(distances.shape)
    print(indices.shape)
    print("Top matching documents:\n")
    
    for i in indices[0]:
        print("-----")
        print(documents[i][:300])  # print first 300 chars

if __name__ == "__main__":
    main()


