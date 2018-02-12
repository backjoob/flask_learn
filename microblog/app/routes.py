from flask import render_template, flash, redirect, url_for
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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    else:
        pass
        #TODO: error message in case validation fails
    return render_template('login.html', title='Sign In', form=form)
