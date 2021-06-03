from unittest import TestCase
from unittest.mock import Mock

from flask import Flask
from minsonet.apis import UserAPI, init_apis


class TestUserAPI(TestCase):
    def get_client(self):
        app = Flask(__name__)
        init_apis(app)
        client = app.test_client()
        return client

    def test_route(self):
        app = Flask(__name__)
        db = Mock()
        api = UserAPI(app, db)
        assert api.route == "/user"
