from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from app.models import User
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'MA'},
            'body': 'Hi Jacob'
        },
        {
            'author': {'username': 'Josh'},
            'body': 'What?'
        },
        {
            'author': {'username': 'Jacob'},
            'body': 'Chicken butt.'
        },
        {
            'author': {'username': 'asdasd'},
            'body': 'dsadsa!'
        }
    ]
    return render_template('index.html', title='Home', \
                            user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or nor user.check_password(form.password.data):
            flask('Invalid username of password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
    
