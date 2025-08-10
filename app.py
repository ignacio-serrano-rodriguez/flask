from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'The index page'

@app.route('/post/<int:post_id>/')
def post_post_id(post_id):
    return f'Post: {post_id}'

@app.route('/path/<path:subpath>/')
def path_subpath(subpath):
    return f'Subpath: {escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about/')
def about():
    return 'The about page'

@app.route('/user/<username>/')
def user_username(username):
    return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('user_username', username='John Doe'))
    
def valid_login(username, password):
    valid = False
    if username == password:
        valid = True
    return(valid)
    
def log_the_user_in(username):
    return render_template('hello.html', person=username)
    
    
# HTTP Methods options ----------------------------------

# Option 1
# @app.get('/login/')
# def login_get():
#     return valid_login()

# @app.post('/login/')
# def login_post():
#     return log_the_user_in()

# Option 2
@app.route('/login/', methods=['GET', 'POST'])
def login() -> str:
    error: str | None = None
    
    if request.method == 'POST':
        username: str = request.form.get('username', '')
        password: str = request.form.get('password', '')
        
        if not username or not password:
            error = "Valid username and password are required"
        elif valid_login(username, password):
            return log_the_user_in(username)
        else:
            error = "Invalid username or password"
            
    return render_template('login.html', error=error)

# -------------------------------------------------------   

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', person=name)