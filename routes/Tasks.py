from typing import Annotated
from fastapi import APIRouter
from models import Task, TaskModel, User

router = APIRouter(prefix="/task")

lista = []


@router.post("/")
async def create_task(current_user: Annotated[User, Depends()], task: Task):
    taskModel = TaskModel(**task.model_dump())
    lista.append(taskModel)
    return {"message": "Task created", "id": taskModel.id}


@router.get("/")
async def get_tasks():
    return {"tasks": [ticket for ticket in lista if not ticket.deleted]}


@router.patch("/{id}")
async def update_task(id: str, task: Task):

    saved_task = [ticket for ticket in lista if ticket.id == id and not ticket.deleted]

    if len(saved_task) == 0:
        return {"message": "Task not found"}

    saved_task[0].title = task.title
    saved_task[0].description = task.description

    return {"message": "Task updated"}


@router.delete("/{id}")
async def delete_tasks(id: str):
    if len(lista) == 0:
        return {"message": "Task not found"}

    task: list[TaskModel] = [ticket for ticket in lista if ticket.id == id]

    if len(task) == 0:
        return {"message": "Task not found"}

    task[0].deleted = True

    return {"tasks": [ticket for ticket in lista if not ticket.deleted]}
