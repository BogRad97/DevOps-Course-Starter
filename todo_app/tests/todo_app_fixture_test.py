import json
import pytest 
from dotenv import load_dotenv, find_dotenv 
from todo_app import app 
import requests
import os

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()
    test_app.testing = True

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        load_dotenv(file_path, override=True)
        yield client

def test_index_page(monkeypatch, client): 
    # Replace call to requests.get(url) with our own function 
    monkeypatch.setattr(requests, 'get', get_lists_stub) 
    response = client.get('/')
    assert response.status_code == 200 
    assert 'ToDo Card' in response.data.decode() 


class StubResponse(): 
    def __init__(self, fake_response_data): 
        self.content = json.dumps(fake_response_data)
        self.fake_response_data = fake_response_data


def get_lists_stub(url, params): 
    test_board_id = os.environ.get('TRELLO_BOARD_ID') 
    fake_response_data = None
    if url == f'https://trello.com/1/board/{test_board_id}/lists': 
        fake_response_data = [{ 
        'id': '1', 
        'name': 'ToDo List', 
        'cards': [{'id': '100', 'name': 'ToDo Card'}] 
        }] 
        return StubResponse(fake_response_data)
    
    if url == f'https://trello.com/1/board/{test_board_id}/cards':
        fake_response_data = [{ 
        'id': '100', 
        'idList': '1', 
        'name': 'ToDo Card' 
        }] 
        return StubResponse(fake_response_data)