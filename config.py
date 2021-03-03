import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'admin@forgame@8964'

    SECURITY_PASSWORD_SALT = 'salt@admin@forgame@8964'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'

    SECURITY_REGISTERABLE = True

    MAX_CONTENT_LENGHTH = 1024 * 1024
