import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    config_obj = None
    env = os.environ.get('ENVIRONMENT', 'local')
    if env == 'local':
        config_obj = 'app.config.LocalConfig'

    if config_obj is not None:
        app.config.from_object(config_obj)

    return app


app = create_app()


@app.route('/')
def home():
    return 'home'
