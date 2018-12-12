class Config:
    pass


class LocalConfig(Config):
    MYSQL_URI = 'mysql://mysql:3306@local:local/hipsterate'
