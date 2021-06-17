import json

from flask import request


class PostLikeAPI:
    @property
    def route(self):
        return "/post_like"

    @property
    def id(self):
        return str(self.route).replace("/", "")

    def __init__(self, app, db):
        self.app = app
        self.db = db
        self.configure_routes(app)

    def post(self):
        data_string = request.get_data()
        data = json.loads(data_string)
        item = self.db.insert(data)
        if item is None:
            response_item = json.dumps(
                {"message": f"Could not insert data {json.loads(data_string)}"}
            )
            response = self.app.response_class(
                response=response_item, status=500, mimetype="application/json"
            )
            return response
        else:
            response_item = json.dumps(item.__dict__)
            response = self.app.response_class(
                response=response_item, status=200, mimetype="application/json"
            )
            return response

    def delete(self, postPK=None, userPK=None):
        self.db.delete(postPK, userPK)
        return f"delete - postPK: {postPK}, userPK: {userPK}"

    def get_number_of_likes_for_post(self, postPK=None):
        likes = self.db.get_number_of_likes_for_post(postPK)
        item = {"postPK": postPK, "likes": likes}
        response = self.app.response_class(
            response=json.dumps(item), status=200, mimetype="application/json"
        )
        return response

    def configure_routes(self, app):
        app.add_url_rule(
            f"{self.route}/number-of-likes/<postPK>",
            f"{self.id}-get_number_of_likes_for_post",
            self.get_number_of_likes_for_post,
            methods=["GET"],
        )
        app.add_url_rule(
            f"{self.route}", f"{self.id}-post", self.post, None, methods=["POST"]
        )
        app.add_url_rule(
            f"{self.route}/<postPK>/<userPK>",
            f"{self.id}-delete",
            self.delete,
            None,
            methods=["DELETE"],
        )
