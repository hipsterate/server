class Config:
    TIMEZONE = 'Asia/Seoul'


class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://local:local@mysql:3306/hipsterate'
