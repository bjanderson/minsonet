from flask import url_for

from .example_routes import init_example_routes
from .login_routes import init_login_routes
from .site_routes import init_site_routes


def init_routes(app):

    init_site_routes(app)
    init_login_routes(app)

    init_example_routes(app)
