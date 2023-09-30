import os
from dotenv import load_dotenv

load_dotenv()
def get_env_variable(name):
    try:
        return os.getenv(name)
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

class Config:
    SECRET_KEY = get_env_variable('SECRET_KEY')
    OPENAI_KEY = get_env_variable('OPENAI_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')