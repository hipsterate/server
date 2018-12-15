class Config:
    TIMEZONE = 'Asia/Seoul'


class LocalConfig(Config):
    SECRET_KEY = 'RwKNvZx8cSuBiHj/wAHxDg=='

    SQLALCHEMY_DATABASE_URI = 'mysql://local:local@mysql:3306/hipsterate'
