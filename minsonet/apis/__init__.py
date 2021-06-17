from ..db import DB, CommentDB, PasswordDB, PostDB, PostLikeDB, UserDB
from ..enums import DatabaseLocation
from .comment_api import CommentAPI
from .post_api import PostAPI
from .post_like_api import PostLikeAPI
from .user_api import UserAPI


def init_apis(app):

    db = DB(DatabaseLocation.MINSONET.value)
    comment_db = CommentDB(db)
    password_db = PasswordDB(db)
    post_db = PostDB(db)
    post_like_db = PostLikeDB(db)
    user_db = UserDB(db)
    CommentAPI(app, comment_db)
    PostAPI(app, post_db)
    PostLikeAPI(app, post_like_db)
    UserAPI(app, user_db, password_db)
