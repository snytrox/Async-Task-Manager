# 🚀 TaskFlow Backend API

This project is a modern and scalable **Task Management API** built with a fully **asynchronous** architecture.

## 🛠️ Tech Stack
- **Framework:** FastAPI
- **Database:** PostgreSQL (Asynchronous)
- **ORM:** SQLAlchemy 2.0 (Mapped Declarative)
- **Validation:** Pydantic v2
- **Language:** Python 3.10+

## 🌟 Key Features
- **Async/Await:** All database operations are handled asynchronously to ensure high performance and responsiveness.
- **Auto-Schema Generation:** Database tables are automatically created on application startup.
- **Type Safety:** Ensures API input/output security and consistency using Pydantic schemas.
- **Clean Architecture:** Separated models, schemas, and database configurations for better maintainability.

## ⚙️ Installation & Setup
1. Create a virtual environment:  
   `python -m venv venv`
2. Activate the virtual environment:  
   - Windows: `venv\Scripts\activate`  
   - Linux/Mac: `source venv/bin/activate`
3. Install dependencies:  
   `pip install -r requirements.txt`
4. Start the application:  
   `uvicorn main:app --reload`
