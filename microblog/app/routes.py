from flask import render_template
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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
