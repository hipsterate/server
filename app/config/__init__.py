import os
import configparser


secret = configparser.ConfigParser()
secret_path = '/app/app/config/secret.yml'
if not os.path.exists(secret_path):
    raise FileNotFoundError(secret_path)
secret.read(secret_path)


class Config:
    TIMEZONE = 'Asia/Seoul'

    FACEBOOK_APP_ID = secret.get('default', 'fb_app_id')
    FACEBOOK_APP_SECRET = secret.get('default', 'app_secret')


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
