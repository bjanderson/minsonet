from flask import flash, redirect, render_template, request, session, url_for


def init_login_routes(app):
    @app.route("/login", methods=["GET", "POST"])
    def login():
        # this route/method handles two different use cases depending on the type of request
        if request.method == "POST":
            session.permanent = True
            # handle the login request
            user = request.form["nm"]
            session["user"] = user
            flash("login successful", "info")
            return redirect(url_for("user"))
        else:
            if "user" in session:
                flash("You are already logged in", "info")
                return redirect(url_for("user"))
            else:
                return render_template("login.html")

    @app.route("/logout")
    def logout():
        if "user" in session:
            flash("You logged out successfully.", "info")

        session.pop("user", None)
        return redirect(url_for("login"))

    @app.route("/user")
    def user():
        if "user" in session:
            user = session["user"]
            return render_template("user.html", user=user)
        else:
            return redirect(url_for("login"))
