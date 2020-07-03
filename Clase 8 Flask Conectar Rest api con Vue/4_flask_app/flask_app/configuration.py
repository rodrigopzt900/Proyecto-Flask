class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI= "postgresql+psycopg2://postgres:rodrigopedro@database-2.czqukvhuls7s.us-west-2.rds.amazonaws.com:5432/manillo"
class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo key'