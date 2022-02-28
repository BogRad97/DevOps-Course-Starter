from typing import List
from todo_app.data.models.trello_list import TrelloList

class ViewModel:
    def __init__(self, items):
        self._items: List[TrelloList] = items

    @property
    def enumerated_items(self):
        return enumerate(self._items)
    
    @property
    def len_items(self):
        return len(self._items)
    
    @property
    def todo_items(self):
        for item in self._items:
            if item.title == 'To Do':
                return item.cards
    
    @property
    def doing_items(self):
       for item in self._items:
            if item.title == 'Doing':
                return item.cards
    
    @property
    def done_items(self):
        for item in self._items:
            if item.title == 'Done':
                return item.cards
