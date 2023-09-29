from Application import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'sam'}
    return '''
    <html>
        <head>
            <title>HomePage-SocialTalks</title>
        </head>
        <body>
            <h1>Hello, ''' +user['username']+ '''!</h1>
        </body>
    </html> '''