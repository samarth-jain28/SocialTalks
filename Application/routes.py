from flask import render_template
from Application import app
from Application.form import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'sam'}
    posts = [
        {
            'author' : 'Sam',
            'body' : 'Today\'s day is very beautyful. '
        },
        {
            'author' : 'Mam',
            'body' : 'Yes , you\'re right. '
        }
    ]
    return render_template('index.html',title='HomePage', user=user, post=posts)

@app.route('/login' , methods=['GET' , 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html' ,title='SignIn' ,form = form)