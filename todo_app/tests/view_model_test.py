from typing import List
from todo_app.data.models.trello_card import TrelloCard

from todo_app.data.models.trello_list import TrelloList
from todo_app.data.models.view_model import ViewModel


def populate_view_model():
    first_list: TrelloList = TrelloList({'id': 1, 'name': 'To Do'})
    todo_card: TrelloCard = TrelloCard({'id': 7, 'idList': 1, 'name': 'First ToDo'})
    first_list.add_card(todo_card)

    second_list: TrelloList = TrelloList({'id': 2, 'name': 'Doing'})
    doing_card: TrelloCard = TrelloCard({'id': 8, 'idList': 2, 'name': 'First Doing'})
    second_list.add_card(doing_card)

    third_list: TrelloList = TrelloList({'id': 3, 'name': 'Done'})
    done_card: TrelloCard = TrelloCard({'id': 9, 'idList': 3, 'name': 'First Done'})
    third_list.add_card(done_card)

    items: List[TrelloList] = [first_list, second_list, third_list]
    return ViewModel(items)

def test_todo_items():
    # given
    view_model = populate_view_model()

    # when
    items = view_model.todo_items

    # then
    assert len(items) == 1
    assert items[0].id == 7
    assert items[0].list_id == 1
    assert items[0].title == 'First ToDo'

def test_doing_items():
    # given
    view_model = populate_view_model()

    # when
    items = view_model.doing_items

    # then
    assert len(items) == 1
    assert items[0].id == 8
    assert items[0].list_id == 2
    assert items[0].title == 'First Doing'

def test_done_items():
    # given
    view_model = populate_view_model()

    # when
    items = view_model.done_items

    # then
    assert len(items) == 1
    assert items[0].id == 9
    assert items[0].list_id == 3
    assert items[0].title == 'First Done'