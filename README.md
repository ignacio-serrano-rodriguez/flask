# Flask

## 1. Useful CLI commands

- [Official Documentation](https://flask.palletsprojects.com/en/stable/cli/)
    - [Click - CLI toolkit (Main dependency)](https://click.palletsprojects.com/en/stable/)

- `flask --app "filename".py run`

    Explicitly specifies which Python file contains your Flask application and runs it. This command is useful when:
    - Your Flask app file is not named `app.py` or `wsgi.py` (Flask's default names)
    - You have multiple Flask applications in the same directory
    - You want to be explicit about which file to run

- `flask run`

    Starts the Flask development server. This command runs your Flask application locally, making it accessible at `http://127.0.0.1:5000` by default.

- `flask run --debug`

    Starts the Flask development server with debug mode enabled. Debug mode provides:
    - **Automatic reloading**: Server restarts automatically when you save code changes
    - **Detailed error pages**: Shows full stack traces and exact error locations in the browser
    - **Interactive debugger**: Click on traceback lines to open a Python console (requires PIN)
    - **Enhanced logging**: More verbose output in the terminal
  
    **Security Warning**: Never use debug mode in production! The interactive debugger allows code execution.

## 2. API Debugging Tool

### HTTP POST Method

#### Headers
- **Content-Type**: `application/x-www-form-urlencoded`

#### Body Configuration
- Select **Body** tab
- Choose **x-www-form-urlencoded**
- Add key-value pairs for form fields

## 3. Deploying to Production

- [Official Documentation](https://flask.palletsprojects.com/en/stable/deploying/)
- [Source](https://www.reddit.com/r/flask/comments/1jcdaux/finally_deployed_my_flask_app_and_wow_i_was_not/)

#### Production Server Requirements
- **Don't use Flask's built-in server** in production 
    - install **Gunicorn** or similar WSGI server
- Flask's development server (`flask run`) is only for local development

#### Security & Configuration
- **Never hardcode API keys** 
    - use environment variables instead
- **Check your code** before pushing to GitHub to avoid exposing secrets
- Use `.env` files locally and proper environment configuration in production

#### Database Management
- **Properly close database connections** to prevent memory leaks
- Use **SQLAlchemy's connection pooling** for better performance under load
- Monitor your database connections in production

#### Development Tools
- **Docker is essential**, not overkill 
    - simplifies deployment with `docker-compose up`
- **Flask-CORS** quickly fixes cross-origin request issues in APIs

#### Quick Deployment Checklist
- Replace Flask dev server with Gunicorn
- Move all secrets to environment variables
- Configure proper database connection handling
- Set up Docker containers
- Configure CORS if building an API

**Bottom line**: What works locally often breaks in production. Plan for proper production infrastructure from the start!

## 4. Official Documentation

- [Installation](https://flask.palletsprojects.com/en/stable/installation/)

- [Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)

- [Jinja2 - Template Designer Documentation](https://jinja.palletsprojects.com/en/stable/templates/)
    - [Template Inheritance](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/)
    - [Jinja - Template engine (Main dependency)](https://jinja.palletsprojects.com/en/stable/)

- [SQLAlchemy](https://flask.palletsprojects.com/en/stable/patterns/sqlalchemy/)

- [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)

- [User's Guide](https://flask.palletsprojects.com/en/stable/#user-s-guide)

- [Development Server](https://flask.palletsprojects.com/en/stable/server/)

- [API Reference](https://flask.palletsprojects.com/en/stable/#api-reference)

- More

    - [Patterns](https://flask.palletsprojects.com/en/stable/patterns/)
    - [API](https://flask.palletsprojects.com/en/stable/api/)
    - [Additional Notes](https://flask.palletsprojects.com/en/stable/#additional-notes)
    - [Werkzeug - WSGI toolkit (Main dependency)](https://werkzeug.palletsprojects.com/en/stable/)
