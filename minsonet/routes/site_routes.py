from flask import redirect, render_template, url_for


def init_site_routes(app):
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/posts")
    def posts():
        return render_template("posts.html")

    @app.route("/404")
    def not_found():
        return render_template("404.html")

    @app.route("/favicon.ico")
    def favicon():
        return redirect(url_for("static", filename="favicon.ico"))
