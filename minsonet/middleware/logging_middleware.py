import logging

# from werkzeug.wrappers import Request, Response


class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        method = environ["REQUEST_METHOD"]
        scheme = environ["wsgi.url_scheme"]
        host = environ["HTTP_HOST"]
        uri = environ["REQUEST_URI"]
        query = environ["QUERY_STRING"]
        log_str = f"{method} {scheme}://{host}{uri}{query}"
        logging.info(log_str)
        return self.app(environ, start_response)

        # res = Response("Authorization failed", status=401)
        # return res(environ, start_response)

        # request = Request(environ)
        # username = request.authorization("username")
        # password = request.authorization("password")

        # print(f"username: {username}")
        # print(f"password: {password}")

        # if username is not None:
        #     environ["user"] = {"name": username}
        #     return self.app(environ, start_response)

        # else:
        #     res = Response("Authorization failed", status=401)
        #     return res(environ, start_response)
