from minsonet import app

if __name__ == "__main__":
    # this only runs if you run it with python (not flask run)
    print(
        "Make sure to set your environment variables in order to run flask with python"
    )
    print("export FLASK_APP=app.py")
    print("export FLASK_ENV=development")
    app.run("0.0.0.0", 3000, debug=True)
