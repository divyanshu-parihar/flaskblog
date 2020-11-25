from flaskblog import app
from flask import render_template
from flaskblog.models import data
for data_screen in data:
    print(data_screen['text'])
# routes
# home route
@app.route('/home/')
@app.route('/')
def index():
    # response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    # response.headers['Cache-Control'] = 'public, max-age=0'
    return render_template('index.html',data = data)

#<------------- NOT FOR NOW .THESE WILL WE ADDED LATER!! ----------------->

# admin_login route
@app.route('/<name>/')
def admin_login(name):
    return f'{name}world!'
# add_content route
@app.route('/')
def add_content():
    return 'hello world!'
