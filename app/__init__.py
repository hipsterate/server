import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    env = os.environ.get('ENVIRONMENT')
    if env == 'local':
        config_obj = 'app.config.LocalConfig'

    app.config.from_object(config_obj)

    return app


app = create_app()


@app.route('/')
def home():
    return 'home'
