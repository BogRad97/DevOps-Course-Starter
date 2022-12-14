from todo_app.data.models.view_model import ViewModel
from todo_app.data.models.item import Item
from todo_app.data.models.status import Status

def populate_view_model():
    todo_item = Item('Todo Title', 'Todo Desc', Status.TODO)
    doing_item = Item('Doing Title', 'Doing Desc', Status.DOING)
    done_item = Item('Done Title', 'Done Desc', Status.DONE)

    items: list[Item] = [todo_item, doing_item, done_item]
    return ViewModel(items)

def test_todo_items():
    # given
    view_model = populate_view_model()

    # when
    items = view_model.todo_items

    # then
    assert len(items) == 1
    assert items[0].status == Status.TODO

def test_doing_items():
    # given
    view_model = populate_view_model()

    # when
    items = view_model.doing_items

    # then
    assert len(items) == 1
    assert items[0].status == Status.DOING

def test_done_items():
    # given
    view_model = populate_view_model()

    # when
    items = view_model.done_items

    # then
    assert len(items) == 1
    assert items[0].status == Status.DONE