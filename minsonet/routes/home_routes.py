from flask import redirect, render_template, url_for


def init_home_routes(app):
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/favicon.ico")
    def favicon():
        return redirect(url_for("static", filename="favicon.ico"))
