from .crud_api import CrudAPI


class PostAPI(CrudAPI):
    @property
    def route(self):
        return "/post"
