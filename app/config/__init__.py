import os


class Config:
    TIMEZONE = 'Asia/Seoul'

    FACEBOOK_APP_ID = 2119931328023450
    FACEBOOK_APP_SECRET = 'be9c9bb5c7c5402b5e8045f0746c2a45'


class TestConfig(Config):
    DEBUG = True
    TESTING = True

    SECRET_KEY = 'RwKNvZx8cSuBiHj/wAHxDg=='

    SQLALCHEMY_DATABASE_URI = 'mysql://local:local@mysql:3306/hipsterate'


class LocalConfig(Config):
    DEBUG = True
    TESTING = True

    SECRET_KEY = 'RwKNvZx8cSuBiHj/wAHxDg=='

    SQLALCHEMY_DATABASE_URI = 'mysql://local:local@mysql:3306/hipsterate'


def get_config_obj():
    config_obj = None

    env = os.environ.get('ENVIRONMENT', 'local')
    if env == 'test':
        config_obj = 'app.config.TestConfig'
    elif env == 'local':
        config_obj = 'app.config.LocalConfig'

    if config_obj is None:
        raise ValueError('invalid config environment')

    return config_obj
