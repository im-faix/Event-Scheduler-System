import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_event(client):
    response = client.post('/events', json={
        "title": "Test Event",
        "description": "This is a test",
        "start_time": "2025-07-01T10:00:00",
        "end_time": "2025-07-01T11:00:00"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == "Test Event"

def test_list_events(client):
    response = client.get('/events')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_search_event(client):
    response = client.get('/search?q=test')
    assert response.status_code == 200

def test_delete_event(client):
    response = client.post('/events', json={
        "title": "To Delete",
        "description": "Delete me",
        "start_time": "2025-07-01T12:00:00",
        "end_time": "2025-07-01T13:00:00"
    })
    event_id = response.get_json()['id']
    del_response = client.delete(f'/events/{event_id}')
    assert del_response.status_code == 200
