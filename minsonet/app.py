import logging
from datetime import timedelta

from flask import Flask

from .apis import init_apis
from .middleware import LoggingMiddleware
from .routes import init_routes

logging.basicConfig(
    filename="myflaskapp.log",
    format="%(asctime)s - %(levelname)s (%(name)s): %(message)s",
    level=logging.DEBUG,
)

app = Flask(__name__)
app.debug = True
app.wsgi_app = LoggingMiddleware(app.wsgi_app)
app.secret_key = "dont store your secrets in plain text"
app.permanent_session_lifetime = timedelta(days=1)
init_apis(app)
init_routes(app)

print("\n#####################################")
print("\t Welcome to MinSoNet")
print("\thttp://localhost:5000")
print("#####################################\n")
