

class TrelloCard:
    def __init__(self, json_obj):
        self.id = json_obj['id']
        self.list_id = json_obj['idList']
        self.title = json_obj['name']

    def __str__(self):
        return str(f'title: {self.title}, id: {self.id}, list_id: {self.list_id}\n')
