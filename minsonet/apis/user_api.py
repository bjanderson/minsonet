from .crud_api import CrudAPI


class UserAPI(CrudAPI):
    def __init__(self, app, user_db, password_db):
        super().__init__(app, user_db)

    @property
    def route(self):
        return "/user"
