from flask import url_for

from .example_routes import init_example_routes
from .home_routes import init_home_routes
from .login_routes import init_login_routes


def init_routes(app):

    init_home_routes(app)
    init_login_routes(app)

    init_example_routes(app)
