from ..db import DB, UserDB
from ..enums import DatabaseLocation
from .user_api import UserAPI


def init_apis(app):

    db = DB(DatabaseLocation.MINSONET.value)
    userdb = UserDB(db)
    UserAPI(app, userdb)
