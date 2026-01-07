# concept-clarity-scientific-terminology
An AI-based web application that simplifies scientific terminology by generating easy-to-understand explanations for complex concepts.

An AI-powered scientific term explainer built using:
- Streamlit (Frontend)
- FastAPI (Backend)
- PostgreSQL (Database)
- JWT Authentication

## Features
- User signup & login
- JWT-based authentication
- Search history stored for logged-in users
- Guest access for anonymous users

## How to Run
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
streamlit run app.py
