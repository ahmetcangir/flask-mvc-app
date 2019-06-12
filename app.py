from app import app


if __name__ == "__main__":
    app.config.from_object('config')
    app.secret_key = app.config["SECRET_KEY"]
    app.debug = app.config["DEBUG"]
    app.run(host=app.config["HOST"], port=app.config["PORT"])

