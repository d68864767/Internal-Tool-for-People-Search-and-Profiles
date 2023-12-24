# tests.py

import pytest
from app import app as flask_app
from models import db, Profile
from config import TestingConfig
import data_ingestion
import search

@pytest.fixture
def app():
    flask_app.config.from_object(TestingConfig)
    db.init_app(flask_app)
    with flask_app.app_context():
        db.create_all()
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Home" in response.data

def test_search_page(client):
    response = client.get('/search')
    assert response.status_code == 200
    assert b"Search" in response.data

def test_profile_page(client):
    response = client.get('/profile/1')
    assert response.status_code == 200
    assert b"Profile" in response.data

def test_data_ingestion():
    data = [
        {
            'id': 1,
            'name': 'Test Profile',
            'description': 'This is a test profile',
            'image_url': 'http://example.com/image.jpg',
            'other_data': {'key': 'value'}
        }
    ]
    data_ingestion.ingest_data(data)
    profile = Profile.query.get(1)
    assert profile is not None
    assert profile.name == 'Test Profile'

def test_search():
    query = 'Test Profile'
    results = search.perform_search(query)
    assert len(results) > 0
    assert 'Test Profile' in [result['name'] for result in results]
