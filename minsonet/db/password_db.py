from ..models import Password
from .crud_db import CrudDB


class PasswordDB(CrudDB):
    @property
    def table_name(self):
        return "password"

    @property
    def table_column_definitions(self):
        # Note: these columns must be in the same order as the property assignments in the Password class or the mappings will break
        return [
            "password TEXT NOT NULL",
            "userPK INTEGER PRIMARY KEY AUTOINCREMENT",
            "FOREIGN KEY(userPK) REFERENCES user(pk)",
        ]

    def create_item(self, tup):
        password = Password.from_tuple(tup)
        return password
