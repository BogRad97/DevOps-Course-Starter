import requests
import os
import json
from .models.trello_card import TrelloCard
from .models.trello_list import TrelloList
from typing import List
from copy import deepcopy

auth_query_params = {
    "key": os.getenv("TRELLO_CONSUMER_KEY"),
    "token": os.getenv("TRELLO_ACCESS_TOKEN")
}


def get_items() -> List[TrelloList]:
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """

    TRELLO_BOARD_ID = os.getenv("TRELLO_BOARD_ID")
    content = json.loads(requests.get(f'https://trello.com/1/board/{TRELLO_BOARD_ID}/cards', auth_query_params).content)
    cards = [TrelloCard(x) for x in content]
    content = json.loads(requests.get(f'https://trello.com/1/board/{TRELLO_BOARD_ID}/lists', auth_query_params).content)
    lists = [TrelloList(x) for x in content]

    for li in lists:
        for c in cards:
            if c.list_id == li.id:
                li.add_card(c)

    return lists


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """

    lists = get_items()

    first_list_id = lists[0].id
    query_params = deepcopy(auth_query_params)
    query_params['idList'] = first_list_id
    query_params['name'] = title
    query_params['pos'] = 'bottom'

    requests.post('https://trello.com/1/cards', query_params)


def remove_item(card_id: str):
    """
    Removes an item with the specified id to the session.

    Args:
        card_id: The id of the item.
    """
    requests.delete(f'https://trello.com/1/cards/{card_id}', params=auth_query_params)


def move_across(card_id: str):
    """
        Moves an item to the next list

        Args:
            card_id: The id of the item.
    """
    lists = get_items()
    new_list = None
    for idx, list in enumerate(lists):
        if list.get_card(card_id) is not None and (idx + 1 < len(lists)):
            new_list = lists[idx + 1]
            break

    if new_list is not None:
        query_params = deepcopy(auth_query_params)
        query_params['idList'] = new_list.id
        requests.put(f'http://trello.com/1/cards/{card_id}', params=query_params)


def move_backwards(card_id: str):
    """
        Moves an item to the previous list

        Args:
            card_id: The id of the item.
    """
    lists = get_items()
    new_list = None
    for idx, list in enumerate(lists):
        if list.get_card(card_id) is not None and (idx - 1 >= 0):
            new_list = lists[idx - 1]
            break

    if new_list is not None:
        query_params = deepcopy(auth_query_params)
        query_params['idList'] = new_list.id
        requests.put(f'http://trello.com/1/cards/{card_id}', params=query_params)
