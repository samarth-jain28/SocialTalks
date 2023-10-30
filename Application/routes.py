from flask import render_template , flash , redirect ,url_for
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
    if form.validate_on_submit():
        flash('Login requested for user {} , remember me={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html' ,title='SignIn' ,form = form)
