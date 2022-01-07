from typing import List
from .trello_card import TrelloCard


class TrelloList:
    def __init__(self, list_json):
        self.id: str = list_json['id']
        self.title: str = list_json['name']
        self.cards: List[TrelloCard] = []

    def __str__(self):
        return str(f'name: {self.title}, id: {self.id}\n')

    def add_card(self, card: TrelloCard):
        self.cards.append(card)

    def get_card(self, card_id: str):
        for c in self.cards:
            if c.id == card_id:
                return c
        return None
