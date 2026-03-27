"""
Starter code for REST API with FastAPI assignment.
Complete the implementation following the requirements in README.md
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI app
app = FastAPI()

# Define data models using Pydantic
class TodoItem(BaseModel):
    """Model for todo item"""
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    status: str = "pending"
    priority: int = 1


# In-memory storage for todos (replace with database in production)
todos_db: List[TodoItem] = []
next_todo_id = 1


# Root endpoint
@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Todo API"}


# TODO: Implement GET all todos endpoint


# TODO: Implement GET single todo endpoint


# TODO: Implement POST create todo endpoint


# TODO: Implement PUT update todo endpoint


# TODO: Implement DELETE todo endpoint


# TODO: Add status filtering capability


# TODO: Add priority filtering capability


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
