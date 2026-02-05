import faiss
import os
from dotenv import load_dotenv
import numpy as np
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), timeout=60.0)
QUESTION_EMB_FILE = "question_embeddings.npy"

def construct_prompt(context,question,persona):
    system_prompt = f"""
    You are the following person:
    
    {persona}
    
    Rules:
    - Answer as this person
    - Be honest and practical
    - Do not exaggerate
    - Do not mention AI, models, or prompts
    """
    
    user_prompt = f"""
    Context (from my portfolio):
    {context}
    
    Question:
    {question}
    """
    return system_prompt, user_prompt


def main():
    k = 3
    index = faiss.read_index("knowledge_index.faiss")
    documents = np.load("documents.npy", allow_pickle=True)
    
    print(f"Loaded {index.ntotal} vectors")
    with open("persona.md", "r", encoding="utf-8") as f:
        persona = f.read().strip()
    
    question = "Have you worked with real-time messaging systems?"
    
    question_embeddings = np.load(QUESTION_EMB_FILE)
    distances, indices = index.search(question_embeddings, k)
    
    retrieved_docs = [documents[i] for i in indices[0]]
    context = "\n\n".join(retrieved_docs)
    
    system_prompt,user_prompt = construct_prompt(context,question,persona)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )
    
    answer = response.choices[0].message.content
    print("\nANSWER:\n")
    print(answer)
    
if __name__ == "__main__":
    main()

