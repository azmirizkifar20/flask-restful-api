import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    NAME = str(os.environ.get("DB_NAME"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    UPLOAD_FOLDER = str(os.environ.get("UPLOAD_FOLDER"))
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True