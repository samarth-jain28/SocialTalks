from flask import render_template
from Application import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'sam'}
    return render_template('index.html',title='HomePage', user=user)