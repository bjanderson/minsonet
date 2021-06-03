from minsonet.db import DB
from tests.utils import has_method

db = DB(":memory:")


def test_db():
    assert has_method(DB, "get_connection")
