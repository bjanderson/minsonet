from .crud_api import CrudAPI


class UserAPI(CrudAPI):
    @property
    def route(self):
        return "/user"
