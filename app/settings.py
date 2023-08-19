import os


basedir = os.path.dirname(os.path.dirname(__file__))
dbdir = basedir + '/database'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dbdir, 'database.db')
SECRET_KEY = os.urandom(10)
