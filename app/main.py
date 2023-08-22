import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import select
from app import models


app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = SQLAlchemy()
db.init_app(app)

basedir = os.path.dirname(os.path.dirname(__file__))
mgdir = basedir + '/database/migrations'
Migrate(app, db, directory=mgdir)


@app.route('/')
def index():
    stmt = select(models.Blogpost).order_by(models.Blogpost.id.desc())
    entries = db.session.execute(stmt).scalars().all()
    return render_template('index.html', rows=entries)


from app.crud.views import crud

app.register_blueprint(crud)
