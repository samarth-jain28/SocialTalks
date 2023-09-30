from flask import render_template
from Application import app

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