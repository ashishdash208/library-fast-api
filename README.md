# 📚 Library Book API (FastAPI)

A simple mock REST API for managing a book library, built with FastAPI.  
This project follows a clean architecture pattern with clear separation of concerns: models, repositories, services, controllers, and routers.

---

## 🚀 Features

- Add, retrieve, delete books
- Update book availability
- Clean modular structure
- FastAPI with automatic Swagger/OpenAPI docs

---

## 📁 Project Structure

library-api/
│
├── main.py # Entry point of the app
├── controllers/ # Handles API logic & validation
│ └── book_controller.py
├── routers/ # Defines API routes
│ └── book_router.py
├── services/ # Business logic
│ └── book_service.py
├── repositories/ # Data access layer (mock DB)
│ └── book_repository.py
└── models/ # Pydantic models for data validation
└── book_model.py

## Install dependencies

pip install -r requirements.txt
## Run the app

python -m uvicorn main:app --reload
App runs at: http://127.0.0.1:8000

Interactive Docs: http://127.0.0.1:8000/docs

📌 API Endpoints
Method	Endpoint	Description
GET	/books	List all books
GET	/books/{id}	Get book by ID
POST	/books	Add a new book
DELETE	/books/{id}	Delete a book
PATCH	/books/{id}/availability?available=false	Update availability

## Team Members
1.Stuti Shah
2.Ashish Dash
3.Swati Tiwari
