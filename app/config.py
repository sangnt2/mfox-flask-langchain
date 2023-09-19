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
    OPENAI_KEY = get_env_variable('OPENAI_KEY')
    MFOX_DAT_HOST = get_env_variable("MFOX_DAT_HOST")
    MFOX_DAT_USR = get_env_variable("MFOX_DAT_USR")
    MFOX_DAT_PW = get_env_variable("MFOX_DAT_PW")
    MFOX_DAT_DBNAME = get_env_variable("MFOX_DAT_DBNAME")
    MFOX_DAT_PORT = get_env_variable("MFOX_DAT_PORT")
    DATABASE_DNS = "host='localhost' port='{port}' dbname='{db}' user='{user}' password='{pw}'".format(user=MFOX_DAT_USR,pw=MFOX_DAT_PW,db=MFOX_DAT_DBNAME,port=MFOX_DAT_PORT)