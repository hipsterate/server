import os

from flask import Flask

from app.common.auth import login_manager
from app.common.db import db
from app.user.api import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)

    config_obj = None
    env = os.environ.get('ENVIRONMENT', 'local')
    if env == 'local':
        config_obj = 'app.config.LocalConfig'

    if config_obj is not None:
        app.config.from_object(config_obj)

    register_extension(app)
    register_blueprint(app)

    return app


def register_extension(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprint(app):
    app.register_blueprint(user_blueprint, url_prefix='/user')


app = create_app()
