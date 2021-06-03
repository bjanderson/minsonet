from flask import Flask
from minsonet.routes import init_home_routes


def get_client():
    app = Flask(__name__, template_folder="../templates")
    init_home_routes(app)
    client = app.test_client()
    return client


def test_home():
    client = get_client()
    url = "/"

    response = client.get(url)
    assert response.get_data() == b"<h1>Test index.html</h1>"
    assert response.status_code == 200
