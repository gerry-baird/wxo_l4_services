from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.routing import APIRoute
from routers import task, credit
from models.Message import Message

app = FastAPI()

app.include_router(task.task_router)
app.include_router(credit.credit_router)

security = HTTPBasic()


@app.get("/ping",
         summary='Ping',
         description='Ping',
         )
def ping(credentials: HTTPBasicCredentials = Depends(security)) -> Message:

    m = Message(message="WxO L4 services are alive")
    return m



def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, operation ID will be 'greeting'


use_route_names_as_operation_ids(app)