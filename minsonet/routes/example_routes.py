import json

from flask import redirect, request, url_for

from ..enums import MimeType


def init_example_routes(app):
    @app.route("/admin")
    def admin():
        return redirect(url_for("home"))

    @app.route("/post/example", methods=["POST"])
    def post_example():
        headers = request.headers

        auth_token = headers.get("authorization-sha256")
        # print(f"auth_token: {auth_token}")

        if not auth_token:
            return "Unauthorized", 401

        data_string = request.get_data()
        data = json.loads(data_string)
        # print(f"data: {data}")

        request_id = data.get("request_id")
        payload = data.get("payload")

        if request_id and payload:
            return (
                json.dumps({"received": data}),
                200,
                {"Content-Type": MimeType.JSON.value},
            )
        else:
            return "Bad Request", 400
