# Overview
A Task Management REST API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. This API allows users to create, retrieve, update, and delete tasks, along with user authentication and token-based authorization.
# Features
 - **User Authentication** – Secure authentication using JWT tokens;
 - **CRUD Operations** – Manage tasks (Create, Read, Update, Delete);
 - **PostgreSQL Database** – Uses SQLAlchemy ORM for database interaction;
 - **Data Validation**– Input validation using Pydantic;
 - **Role-Based Access** – Users can only manage their own tasks;
 - **Interactive API Docs** – Auto-generated documentation with Swagger UI;

# Technologies used
- **FastAPI**  - Modern web framework for building APIs
- **PostgreSQL**  - Relational database for storing tasks and users
- **SQLAlchemy**  - ORM for database interactions
- **Pydantic**  - Data validation
- **JWT (JSON Web Tokens)**  - Secure authentication
- **Postman**  - API testing
- **Visual Studio Code** ✍ - Development environment
# Set Up and Installation 
# Clone the repository
- Run the following command in your terminal:
- git clone https://github.com/VladM-Sashev/Task_APP-FastAPI.git
# Create Virtual Environment 
- python -m venv venv
- source venv/bin/activate  # macOS/Linux
- venv\Scripts\activate    # Windows
# Install Dependencies
- pip install -r requirements.txt
# Set Up Environment variables
- Create a .env file in the root directory and add your PostgreSQL credentials:
- database_hostname=localhost
- database_port=5432
- database_username=your_username
- database_password=your_password
- database_name=your_database
- secret_key=your_secret_key
- algorithm=HS256
- time_access_token=30
# Run the Application
uvicorn app.main:app --reload
The API will be available at:
 http://127.0.0.1:8000
# Authentication and authorization 
# User Login(JWT Token)
The API uses OAuth2 with password flow.
Users must log in to receive an access token.
# Login request
POST /login
# Login Response
{
  "access_token": "your_jwt_token",
  "token_type": "Bearer"
}
# Use JWT Token in Requests
Include the token in the Authorization header
Authorization: Bearer your_jwt_token


