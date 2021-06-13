import logging
from datetime import timedelta

from flask import Flask

from .apis import init_apis
from .middleware import LoggingMiddleware
from .routes import init_routes

# https://docs.python.org/3.8/howto/logging.html
logging.basicConfig(
    filename="minsonet.log",
    format="%(asctime)s - %(levelname)s (%(name)s): %(message)s",
    level=logging.DEBUG,
)

app = Flask(__name__)
app.wsgi_app = LoggingMiddleware(app.wsgi_app)
app.secret_key = "dont store your secrets in plain text"
app.permanent_session_lifetime = timedelta(days=1)
init_apis(app)
init_routes(app)

welcome = "\n#####################################\n\t Welcome to MinSoNet\n\thttp://localhost:5000\n#####################################\n"
logging.info(welcome)
print(welcome)
