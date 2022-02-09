class BaseConfig(object):
    APP_NAME ="Bard API"
    AWS_REGION = "us-west-2"
    BARD_S3_BUCKET = "bard"
    FLASK_RUN_PORT = 8080
    FLASK_RUN_HOST = "127.0.0.1"
    VALUE = "v1"

    @staticmethod
    def configure(app):
        from os import environ
        environ["FLASK_ENV"] = app.config["FLASK_ENV"]


class TestingConfig(BaseConfig):
    DEBUG = True
    MONGO_DATABASE = 'bard-db-test'
    FLASK_ENV = "development"
    VALUE = "testing_value"


class DevConfig(BaseConfig):
    DEBUG = True
    MONGO_DATABASE = 'bard-db-dev'
    FLASK_ENV = "development"
    VALUE = "dev_value"

class ProdConfig(BaseConfig):
    DEBUG = False
    MONGO_DATABASE = 'bard-db-prod'
    FLASK_ENV = "development"
    VALUE = "prod_value"

config = dict(
    local=DevConfig,
    prod=ProdConfig,
    testing=TestingConfig
)