from flask import Flask

from app.config import get_config_obj
from app.common.auth import login_manager
from app.common.db import db
from app.user.api import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config_obj())

    register_extension(app)
    register_blueprint(app)

    return app


def register_extension(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprint(app):
    app.register_blueprint(user_blueprint, url_prefix='/user')


app = create_app()
