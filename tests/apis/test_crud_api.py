from unittest import TestCase
from unittest.mock import Mock

from minsonet.apis.crud_api import CrudAPI


class TestApi(CrudAPI):
    @property
    def route(self):
        return "/test"


TestApi.__test__ = False  # tell pytest-cov not to complain about this class


class CrudApiTests(TestCase):
    def test_id(self):
        app = Mock()
        db = Mock()
        api = TestApi(app, db)
        assert api.id == "test"

    def test_configure_routes(self):
        app = Mock()
        db = Mock()
        api = TestApi(app, db)
        api.configure_routes(app)
        app.add_url_rule.assert_called_with(
            "/test/<pk>", "test-delete", api.delete, None, methods=["DELETE"]
        )
