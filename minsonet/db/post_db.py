from ..models import Post
from .crud_db import CrudDB


class PostDB(CrudDB):
    @property
    def table_name(self):
        return "post"

    @property
    def table_column_definitions(self):
        # Note: these columns must be in the same order as the property assignments in the Post class or the mappings will break
        return [
            "authorPK TEXT NOT NULL",
            "content TEXT NOT NULL",
            "createdAt TEXT NOT NULL",
            "pk TEXT NOT NULL PRIMARY KEY",
            "title TEXT NOT NULL",
            "FOREIGN KEY(authorPK) REFERENCES user(pk)",
        ]

    def create_item(self, tup):
        post = Post.from_tuple(tup)
        return post
