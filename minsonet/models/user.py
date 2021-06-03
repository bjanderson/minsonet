# https://www.learnbyexample.org/python-properties/


class User:
    def __init__(self, value):
        setattr(self, "pk", value.get("pk"))
        setattr(self, "email", value.get("email"))
        setattr(self, "name", value.get("name"))
        if not self.name:
            raise AttributeError("user name is required")

    @staticmethod
    def from_tuple(tup):
        # Note: these property assignments must be in the same order as the database columns in the UserDB class or the mappings will break
        return User(
            {
                "pk": tup[0],
                "email": tup[1],
                "name": tup[2],
            }
        )
