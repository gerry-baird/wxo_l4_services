from fastapi import APIRouter, Path, HTTPException
from starlette import status
from models.Task import Task, TaskRequest

TASKS = [
    Task(1, "Closed", "High", "HR", "Some sort of note")
]

task_router = APIRouter()

def find_task_id(task: Task):
    task.id = 1 if len(TASKS) == 0 else TASKS[-1].id + 1
    return task

@task_router.get("/tasks", status_code=status.HTTP_200_OK)
async def read_all_tasks():
    return TASKS

@task_router.get("/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def read_task(task_id: int = Path(gt=0)):
    for task in TASKS:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail='Item not found')

@task_router.post("/tasks/create_task", status_code=status.HTTP_201_CREATED)
async def create_task(task_request: TaskRequest):

    new_task = Task(**task_request.dict())
    TASKS.append(find_task_id(new_task))

    return new_task