from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'The index page'

@app.route('/hello')
def hello():
    return 'Hello user'

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello user with name {escape(name)}!"

@app.route('/post/<int:post_id>')
def post_post_id(post_id):
    return f'Post: {post_id}'

@app.route('/path/<path:subpath>')
def path_subpath(subpath):
    return f'Subpath: {escape(subpath)}'

@app.route('/projects')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def user_username(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('user_username', username='John Doe'))