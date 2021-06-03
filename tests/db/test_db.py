import sqlite3
from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from minsonet.db import DB
from pytest import raises
from tests.utils import has_method

db_location = ":memory:"
db = DB(db_location)


class DBTests(TestCase):
    def test_db_has_method_get_connection(self):
        assert has_method(db, "get_connection")

    @patch("sqlite3.connect", return_value="connection succeeded")
    def test_db_calls_sqlite_connect(self, mocked_sqlite):
        connection = db.get_connection()
        sqlite3.connect.assert_called_with(db_location)
        self.assertEqual(connection, "connection succeeded")

    def test_close_calls_connection_close(self):
        connection = Mock()  # create a mock object
        # connection.close()  # mock automatically adds properties and functions as you access them on the mock object - so you can add them yourself, or just allow them to be added by your code when your test is run
        db.close(connection)
        connection.close.assert_called()

    def test_rollback_calls_connection_rollback(self):
        connection = Mock()
        db.rollback(connection)
        connection.rollback.assert_called()

    def test_execute_completes_all_calls(self):
        cursor = Mock()
        connection = Mock()
        connection.cursor = MagicMock(return_value=cursor)
        db.get_connection = MagicMock(return_value=connection)
        db.close = Mock()

        stmt = "test sql statement"
        db.execute(stmt)

        connection.cursor.assert_called()
        cursor.execute.assert_called_with(stmt)
        connection.commit.assert_called()
        db.close.assert_called()

    def test_execute_calls_close_on_error(self):
        error_message = "test error"
        connection = Mock()
        connection.cursor = MagicMock(side_effect=Exception(error_message))
        db.get_connection = MagicMock(return_value=connection)
        db.close = Mock()

        stmt = "test sql statement"
        with raises(Exception) as e_info:
            db.execute(stmt)

        assert e_info.value.args[0] == error_message
        connection.commit.assert_not_called()
        db.close.assert_called()
