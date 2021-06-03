import json

from flask import Flask
from minsonet.routes import init_routes


def get_client():
    app = Flask(__name__)
    init_routes(app)
    client = app.test_client()
    return client


def test_admin():
    client = get_client()
    url = "/admin"

    response = client.get(url)

    assert response.status_code == 302


def test_post_example():
    client = get_client()
    url = "/post/example"

    mock_request_headers = {"authorization-sha256": "fake-auth"}

    mock_request_data = {"request_id": "123", "payload": {"py": "pi", "java": "script"}}

    response = client.post(
        url, data=json.dumps(mock_request_data), headers=mock_request_headers
    )

    assert response.status_code == 200
