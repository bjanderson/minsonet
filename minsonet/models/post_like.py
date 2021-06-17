class PostLike:
    def __init__(self, value):
        setattr(self, "postPK", value.get("postPK"))
        setattr(self, "userPK", value.get("userPK"))
        if not self.postPK:
            raise AttributeError("postPK is required")
        if not self.userPK:
            raise AttributeError("userPK is required")

    @staticmethod
    def from_tuple(tup):
        # Note: these property assignments must be in the same order as the database columns in the PostDB class or the mappings will break
        return PostLike(
            {
                "postPK": tup[0],
                "userPK": tup[1],
            }
        )
