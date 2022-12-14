import pytest 
from dotenv import load_dotenv, find_dotenv 
from todo_app import app
import mongomock

from todo_app.data.todo_service import TodoService

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client


def test_index_page(client):
    # given
    todo_service = TodoService()
    todo_service.add_item('ToDo Card')

    # when
    response = client.get('/')
    
    # then
    assert response.status_code == 200 
    assert 'ToDo Card' in response.data.decode() 