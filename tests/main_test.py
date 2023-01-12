import pytest
from app import app

def test_post_api():
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list
    assert response.json[0].get("pk") == 1

def test_post_api_by_id():
    response = app.test_client().get('/api/posts/2')
    assert type(response.json) == dict
    assert response.json.get('pk') == 2