from bson.objectid import ObjectId
from .status import Status

class Item:
    def __init__(self, title: str, description: str = '', status: str = Status.TODO) -> None:
        self.title: str = title
        self.description: str = description
        self.status: Status = status
        self._id: ObjectId = None
    
    @staticmethod
    def from_dict(dict_data: dict):
        item = Item(dict_data['title'])
        item.description = dict_data['description']
        item.status = Status(dict_data['status'])
        item._id = dict_data['_id']

        return item
    
    def __dict__(self):
        self_dict = {
            'title': self.title,
            'description': self.description,
            'status': self.status.value
        }

        if self._id is not None:
            self_dict['_id'] = self._id
        
        return self_dict
    