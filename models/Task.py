from pydantic import BaseModel, Field
from typing import Optional
class Task:
    id: int
    status: str
    priority: str
    team: str
    notes: str

    def __init__(self, id, status, priority, team, notes):
        self.id = id
        self.status = status
        self.priority = priority
        self.team = team
        self.notes = notes


class TaskRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    status: str
    priority: str
    team: str
    notes: str
