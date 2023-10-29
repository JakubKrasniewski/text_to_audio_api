from flask import Flask
from src.config import Config
from src.views import speech_blueprint, download_blueprint, languages_blueprint

def create_app():
    app = Flask(__name__)

    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_db.sqlite3"
    app.config.from_object(Config)
    app.register_blueprint(speech_blueprint)
    app.register_blueprint(download_blueprint)
    app.register_blueprint(languages_blueprint)

    return app