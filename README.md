# 🤖 AI Portfolio Assistant (RAG + Tool-Using Agent)

An end-to-end AI agent that represents me and answers questions about my portfolio, projects, and experience in real time.

This project demonstrates practical **LLM engineering**, **RAG pipelines**, **tool calling**, **voice integration**, and **production deployment**.
---
## ✨ Features

- 💬 Chat with an AI assistant trained on my portfolio
- 🧠 Retrieval-Augmented Generation (RAG)
- 📄 Download my CV directly from chat
- 📩 Send email to me from chat (backend SMTP)
- 🔊 Voice input & output using Deepgram
- 🌐 Deployed backend API (PythonAnywhere)

---

## 🧠 How It Works

1. Portfolio content is converted into embeddings  
2. Embeddings stored in FAISS vector database  
3. User asks a question  
4. Relevant documents retrieved via semantic search  
5. Context + persona prompt sent to OpenAI LLM  
6. Agent can call tools (CV download / email)  
7. Response returned 

---

## 🏗️ Architecture Diagram

            ┌──────────────────────┐
            │   Portfolio Content  │
            │ (projects, skills)   │
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │ OpenAI Embeddings    │
            │ text-embedding-3-large│
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │   FAISS Vector DB    │
            │  (Local Knowledge)   │
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │   Context Retrieval  │
            │  Relevant Documents  │
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │ Persona + Prompt     │
            │ Engineering Layer    │
            │ (persona.md + query) │
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │ OpenAI GPT Model     │
            │   (gpt-4o-mini)      │
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │   Agent Tool Layer   │
            │  • Download CV       │
            │  • Send Email        │
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │   Flask REST API     │
            │   /ask endpoint      │
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │  Chat Widget / UI    │
            │  (Text + Voice)      │
            └──────────────────────┘


---

## 🧠 RAG Pipeline

### 1. Knowledge Base Creation
Portfolio content structured into markdown files containing:
- Projects
- Experience
- Skills
- Achievements

### 2. Embeddings Generation
Used OpenAI **text-embedding-3-large** to convert text into semantic vectors.

### 3. Vector Database (FAISS)
- Stored embeddings locally using FAISS.
- Chosen over Redis/Pinecone to keep costs minimal.
- Enables fast similarity search.

### 4. Persona Engineering
Created `persona.md` to define:
- Assistant tone
- Writing style
- Professional behavior

### 5. Answer Generation
Used **gpt-4o-mini** for:
- Fast responses
- Low cost
- High quality answers

---

## 🛠️ Agent Tools (Function Calling)

### 📄 CV Download Tool
Detects resume-related queries and returns a download button dynamically.

### 📩 Email Sending Tool
Users can contact me directly from chat:
- Backend SMTP email sending
- Structured tool responses
- Easily extendable tool architecture

---

## 🔊 Voice Features (Deepgram)

Integrated Deepgram for:

- 🎤 Speech-to-Text (voice input)
- 🔈 Text-to-Speech (voice responses)

Enables a **voice-enabled AI portfolio assistant**.

---

## 🌐 Backend & Deployment

- Built with **Python + Flask**
- Hosted on **PythonAnywhere**
- Implemented:
  - REST API (`/ask`)
  - CORS handling
  - Tool-aware response structure
  - Production WSGI setup

---

## 💻 Tech Stack

### AI / LLM
- OpenAI API
- RAG Architecture
- Prompt Engineering
- Function Calling Agents

### Backend
- Python
- Flask
- FAISS Vector DB
- SMTP Email

### Voice
- Deepgram API

### Deployment
- PythonAnywhere

---

## 🚀 Why This Project Matters

This project demonstrates real-world **LLM product engineering**:

- Vector databases & semantic search
- Prompt & persona engineering
- Tool-using AI agents
- API design & deployment
- Voice AI integration

---
Demo: www.tharindu.space
---

