from flask import Flask
app = Flask(__name__)



@app.route('/index')
def hello_world():
    user = {'username': 'чел'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''



if __name__ == '__main__':
    app.run(debug=True)