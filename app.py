from flask import Flask
from flask import url_for
from flask import request
from markupsafe import escape

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

@app.route('/user/<username>')
def user_username(username):
    return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('user_username', username='John Doe'))
    
def do_the_login():
    return("\"do_the_login\" function")
    
def show_the_login_form():
    return("\"show_the_login_form\" function")
    
    
# HTTP Methods options

# Option 1
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
# Option 2
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()