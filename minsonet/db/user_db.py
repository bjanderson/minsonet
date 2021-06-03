from ..models import User
from .crud_db import CrudDB


class UserDB(CrudDB):
    @property
    def table_name(self):
        return "user"

    @property
    def table_column_definitions(self):
        # Note: these columns must be in the same order as the property assignments in the User calss or the mappings will break
        return [
            "pk INTEGER PRIMARY KEY AUTOINCREMENT",
            "email TEXT NOT NULL",
            "name TEXT NOT NULL",
        ]

    def create_item(self, tup):
        user = User.from_tuple(tup)
        return user
