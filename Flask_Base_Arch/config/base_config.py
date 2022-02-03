"""Flask config class."""
import os


class BaseConfig:
    """Base config vars."""
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Password_123@localhost:3306/practice"
    DEBUG = 0
    SQLALCHEMY_TRACK_MODIFICATIONS = False