import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR = os.path.join(basedir, "../db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "testdb.sqlite3")
    DEBUG = True
    
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT') or '4e3c9f60b5a1e9c8d2f774e08fd192b5'  # Example salt
    # SECURITY_PASSWORD_HASH = 'bcrypt'
    # SECURITY_REGISTERABLE = True
    # SECURITY_SEND_REGISTER_EMAIL = False
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
