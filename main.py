from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Model for creating/updating a todo
class Todo(BaseModel):
    title: str
    completed: bool = False


# Temporary in-memory database
todos = []


# GET - Get all todos
@app.get("/todos")
def get_todos():
    return todos


# POST - Create a todo
@app.post("/todos")
def create_todo(todo: Todo):
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title,
        "completed": todo.completed
    }

    todos.append(new_todo)

    return new_todo


# PUT - Update a todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for item in todos:
        if item["id"] == todo_id:
            item["title"] = todo.title
            item["completed"] = todo.completed
            return item

    return {"message": "Todo not found"}


# DELETE - Delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for item in todos:
        if item["id"] == todo_id:
            todos.remove(item)
            return {"message": "Todo deleted"}

    return {"message": "Todo not found"}
