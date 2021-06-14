from ..db import DB, CommentDB, PasswordDB, PostDB, UserDB
from ..enums import DatabaseLocation
from .comment_api import CommentAPI
from .post_api import PostAPI
from .user_api import UserAPI


def init_apis(app):

    db = DB(DatabaseLocation.MINSONET.value)
    comment_db = CommentDB(db)
    password_db = PasswordDB(db)
    post_db = PostDB(db)
    user_db = UserDB(db)
    CommentAPI(app, comment_db)
    PostAPI(app, post_db)
    UserAPI(app, user_db, password_db)
