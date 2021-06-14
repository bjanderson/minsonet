class Password:
    def __init__(self, value):
        setattr(self, "password", value.get("password"))
        setattr(self, "userPK", value.get("userPK"))
        if not self.password:
            raise AttributeError("password password is required")
        if not self.userPK:
            raise AttributeError("password userPK is required")

    @staticmethod
    def from_tuple(tup):
        # Note: these property assignments must be in the same order as the database columns in the PasswordDB class or the mappings will break
        return Password(
            {
                "password": tup[0],
                "userPK": tup[1],
            }
        )
