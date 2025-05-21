# 🚀 my-fastapi-app

A beginner-friendly Python project to explore **FastAPI** and **PostgreSQL**, with the vision of integrating **LLMs** (Large Language Models) for a future-ready **AI-powered knowledge base**.

## 🔍 Project Goals

- Learn the fundamentals of Python & FastAPI
- Set up PostgreSQL as the backend database
- Build RESTful APIs with FastAPI
- Prepare for AI integration with LLMs for intelligent querying

## 🧰 Tech Stack

- Python 3.13.3
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- OpenAI / Ollama for LLM integration

## 🚧 Status

> Still in early learning and development phase. Basic APIs under construction. LLM integration to follow.

## 📦 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/Parbaz-Hossain/my-fastapi-app
cd my-fastapi-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
