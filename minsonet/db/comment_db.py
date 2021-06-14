from ..models import Comment
from .crud_db import CrudDB


class CommentDB(CrudDB):
    @property
    def table_name(self):
        return "comment"

    @property
    def table_column_definitions(self):
        # Note: these columns must be in the same order as the property assignments in the Comment class or the mappings will break
        return [
            "createdAt TEXT NOT NULL",
            "commenterPK TEXT NOT NULL",
            "comment TEXT NOT NULL",
            "parentCommentPK TEXT",
            "pk TEXT NOT NULL PRIMARY KEY",
            "postPK TEXT NOT NULL",
            "FOREIGN KEY(commenterPK) REFERENCES user(pk)",
            "FOREIGN KEY(parentCommentPK) REFERENCES comment(pk)",
            "FOREIGN KEY(postPK) REFERENCES post(pk)",
        ]

    def create_item(self, tup):
        comment = Comment.from_tuple(tup)
        return comment
