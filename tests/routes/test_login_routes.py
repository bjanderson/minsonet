from flask import Flask
from minsonet.routes import init_login_routes


def get_client():
    app = Flask(__name__, template_folder="../templates")
    app.secret_key = "dont store your secrets in plain text"
    init_login_routes(app)
    client = app.test_client()
    return client


def test_login_get():
    client = get_client()
    url = "/login"

    response = client.get(url)
    assert response.get_data() == b"<h1>Test login.html</h1>"
    assert response.status_code == 200


def test_login_post():
    client = get_client()
    url = "/login"

    response = client.post(url, data=dict(nm="test-user"))
    # msg = b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>Redirecting...</title>\n<h1>Redirecting...</h1>\n<p>You should be redirected automatically to target URL: <a href="/user">/user</a>.  If not click the link.'
    # assert response.get_data() == msg
    assert response.status_code == 302


def test_logout():
    client = get_client()
    url = "/logout"

    response = client.get(url)
    # msg = b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>Redirecting...</title>\n<h1>Redirecting...</h1>\n<p>You should be redirected automatically to target URL: <a href="/login">/login</a>.  If not click the link.'
    # assert response.get_data() == msg
    assert response.status_code == 302
