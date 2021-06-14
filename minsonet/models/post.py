class Post:
    def __init__(self, value):
        setattr(self, "authorPK", value.get("authorPK"))
        setattr(self, "content", value.get("content"))
        setattr(self, "createdAt", value.get("createdAt"))
        setattr(self, "pk", value.get("pk"))
        setattr(self, "title", value.get("title"))
        if not self.authorPK:
            raise AttributeError("authorPK is required")
        if not self.content:
            raise AttributeError("content is required")
        if not self.title:
            raise AttributeError("title is required")

    @staticmethod
    def from_tuple(tup):
        # Note: these property assignments must be in the same order as the database columns in the PostDB class or the mappings will break
        return Post(
            {
                "authorPK": tup[0],
                "content": tup[1],
                "createdAt": tup[2],
                "pk": tup[3],
                "title": tup[4],
            }
        )
