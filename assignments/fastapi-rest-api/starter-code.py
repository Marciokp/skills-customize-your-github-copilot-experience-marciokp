from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

tasks = [
    {"id": 1, "title": "Estudar rotas", "completed": False},
    {"id": 2, "title": "Praticar FastAPI", "completed": True},
]
next_task_id = 3


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


@app.get("/")
def read_root():
    # TODO: retorne uma mensagem indicando que a API está ativa.
    pass


@app.get("/tasks")
def list_tasks():
    # TODO: retorne a lista de tarefas.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: encontre a tarefa pelo ID ou responda com HTTP 404.
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    # TODO: crie um ID, adicione a tarefa à lista e retorne-a.
    pass