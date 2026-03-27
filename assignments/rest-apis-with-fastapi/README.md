# 🚀 REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework. You'll learn how to create API endpoints, handle HTTP methods (GET, POST, PUT, DELETE), work with request and response models, and implement data validation to create a production-ready API.

## 📝 Tasks

### 🛠️ Create a Todo API

#### Description
Build a REST API for managing a todo list. Students will create endpoints to perform CRUD operations (Create, Read, Update, Delete) on todo items, implement proper HTTP status codes, and validate input data.

#### Requirements
Completed API should:

- Use FastAPI to define at least 5 endpoints (GET all todos, GET single todo, POST create todo, PUT update todo, DELETE todo)
- Store todos in an in-memory list or simple data structure
- Accept JSON request bodies with proper validation (todo title required, optional description)
- Return appropriate HTTP status codes (200, 201, 404, 400)
- Include a root endpoint that returns a welcome message
- Use Pydantic models for request/response data validation
- Include at least one path parameter (e.g., `/todos/{todo_id}`) and query parameters (e.g., optional filters)

### 🛠️ Add Advanced Features

#### Description
Extend the todo API with additional features to demonstrate deeper understanding of FastAPI capabilities and API design patterns.

#### Requirements
Completed API should:

- Implement status filtering (get todos by status: pending, completed)
- Add priority levels to todos with filtering capability
- Include proper error handling with custom error messages
- Add request/response documentation using FastAPI's automatic OpenAPI/Swagger support
- Implement at least one POST endpoint that accepts complex nested data structures
