from __future__ import annotations
from enum import Enum

class Status(Enum):
    TODO = 'To Do'
    DOING = 'Doing'
    DONE = 'Done'

    def get_next(self) -> Status:
        match self:
            case Status.TODO:
                return Status.DOING
            case Status.DOING:
                return Status.DONE
            case Status.DONE:
                return Status.DONE
    
    def get_prev(self) -> Status:
        match self:
            case Status.TODO:
                return Status.TODO
            case Status.DOING:
                return Status.TODO
            case Status.DONE:
                return Status.DOING
