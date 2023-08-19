import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = SQLAlchemy()
db.init_app(app)

basedir = os.path.dirname(os.path.dirname(__file__))
mgdir = basedir + '/database/migrations'
Migrate(app, db, directory=mgdir)


@app.route('/')
def index():
    name = 'index'
    return render_template('index.html', title='This is the index page', name=name)
