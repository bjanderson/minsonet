from .crud_api import CrudAPI


class CommentAPI(CrudAPI):
    @property
    def route(self):
        return "/comment"
