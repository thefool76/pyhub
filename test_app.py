from app import app


def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Hello, World!" in response.data
        assert b"This is a simple Flask application running in a Docker container." in response.data