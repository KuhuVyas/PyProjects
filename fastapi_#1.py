from pydantic import BaseModel 
from typing import Lists, Dicts, Optionals
from fastapi import FastAPI 
from uuid import UUID, uuid4

app = FastAPI()
class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks = []

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task
