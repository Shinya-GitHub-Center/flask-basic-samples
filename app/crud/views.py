from flask import Blueprint
from flask import render_template, url_for, redirect, session
from app.crud import forms
from app.main import app
from app import models
from app.main import db


crud = Blueprint(
    'crud',
    __name__,
    template_folder='templates_crud',
    static_folder='static_crud',
)


@crud.route('/admincreate', methods=['GET', 'POST'])
def login():
    form = forms.AdminForm()

    session['logged_in'] = False

    if form.validate_on_submit():
        if form.username.data != app.config['USERNAME'] \
        or form.password.data != app.config['PASSWORD']:
            return render_template('login.html', form=form)
        else:
            session['logged_in'] = True
            return redirect(url_for('crud.article'))

    return render_template('login.html', form=form)


@crud.route('/post', methods=['GET', 'POST'])
def article():
    if not session.get('logged_in'):
        return redirect(url_for('crud.login'))

    form_art = forms.ArticlePost()

    if form_art.validate_on_submit():
        mypost = models.Blogpost(
            title=form_art.post_title.data,
            contents=form_art.post_contents.data,
        )
        db.session.add(mypost)
        db.session.commit()
        session.pop('logged_in', None)
        return redirect(url_for('crud.login'))

    return render_template('post.html', form=form_art)
