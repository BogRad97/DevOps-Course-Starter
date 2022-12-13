from todo_app.data.models.item import Item
from todo_app.data.models.status import Status

class ViewModel:
    def __init__(self, items):
        self._items: list[Item] = items if items is not None else []
    
    @property
    def len_items(self) -> int:
        return len(self._items)
    
    @property
    def aggregated_items(self) -> dict[list[Item]]:
        return {
            Status.TODO: self.todo_items,
            Status.DOING: self.doing_items,
            Status.DONE: self.done_items
        }
    
    @property
    def todo_items(self) -> list[Item]:
        return list(filter(lambda x: x.status == Status.TODO, self._items))
    
    @property
    def doing_items(self) -> list[Item]:
       return list(filter(lambda x: x.status == Status.DOING, self._items))
    
    @property
    def done_items(self) -> list[Item]:
        return list(filter(lambda x: x.status == Status.DONE, self._items))
