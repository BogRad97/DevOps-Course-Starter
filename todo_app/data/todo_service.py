import os
import pymongo
from bson.objectid import ObjectId
from .models.item import Item
from .models.status import Status


class TodoService():
    def __init__(self) -> None:
        self.mongo_client = pymongo.MongoClient(os.getenv('CONNECTION_STRING'))
        self.database = self.mongo_client[os.getenv('DATABASE_NAME')]
        self.collection = self.database[os.getenv('COLLECTION_NAME')]
    
    def add_item(self, item_name: str) -> None:
        item = Item(item_name)
        self.collection.insert_one(item.__dict__())

    def get_items(self) -> list[Item]:
        raw_items = list(self.collection.find({}))
        return [Item.from_dict(x) for x in raw_items]
    
    def remove_item(self, id: str) -> None:
        self.collection.delete_one({'_id': id})
    
    def move_across(self, id: str) -> None:
        self.__move_card(id, Status.get_next)

    def move_backwards(self, id: str) -> None:
        self.__move_card(id, Status.get_prev)

    def __move_card(self, id: str, status_function: callable) -> None:
        item: Item = Item.from_dict(self.collection.find_one({'_id': ObjectId(id)}))
        new_status = status_function(item.status)
        self.collection.update_one({'_id': id}, {"$set": {'status': new_status.value}})
