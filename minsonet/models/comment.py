class Comment:
    def __init__(self, value):
        setattr(self, "comment", value.get("comment"))
        setattr(self, "commenterPK", value.get("commenterPK"))
        setattr(self, "createdAt", value.get("createdAt"))
        setattr(self, "parentCommentPK", value.get("parentCommentPK"))
        setattr(self, "pk", value.get("pk"))
        setattr(self, "postPK", value.get("postPK"))
        if not self.comment:
            raise AttributeError("comment comment is required")
        if not self.commenterPK:
            raise AttributeError("comment commenterPK is required")
        if not self.postPK:
            raise AttributeError("comment postPK is required")

    @staticmethod
    def from_tuple(tup):
        # Note: these property assignments must be in the same order as the database columns in the CommentDB class or the mappings will break
        return Comment(
            {
                "comment": tup[0],
                "commenterPK": tup[1],
                "createdAt": tup[2],
                "parentCommentPK": tup[3],
                "pk": tup[4],
                "postPK": tup[5],
            }
        )
