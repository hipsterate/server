import os

from flask import Flask

from app.common.auth import login_manager
from app.common.db import db


def create_app():
    app = Flask(__name__)

    config_obj = None
    env = os.environ.get('ENVIRONMENT', 'local')
    if env == 'local':
        config_obj = 'app.config.LocalConfig'

    if config_obj is not None:
        app.config.from_object(config_obj)

    db.init_app(app)
    login_manager.init_app(app)

    return app


app = create_app()
