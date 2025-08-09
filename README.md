# Flask

## Official Documentation

1. [Installation](https://flask.palletsprojects.com/en/stable/installation/)

2. [Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)

3. [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)

4. [Patterns](https://flask.palletsprojects.com/en/stable/patterns/)

5. [API](https://flask.palletsprojects.com/en/stable/api/)

6. <u>Main dependencies</u>

   - [Werkzeug - WSGI toolkit](https://werkzeug.palletsprojects.com/en/stable/)
   - [Jinja - Template engine](https://jinja.palletsprojects.com/en/stable/)
   - [Click - CLI toolkit](https://click.palletsprojects.com/en/stable/)

7. [User's Guide](https://flask.palletsprojects.com/en/stable/#user-s-guide)

8. [API Reference](https://flask.palletsprojects.com/en/stable/#api-reference)

9. [Additional Notes](https://flask.palletsprojects.com/en/stable/#additional-notes)

## Useful commands

  - `flask --app "filename".py run`

    Explicitly specifies which Python file contains your Flask application and runs it. This command is useful when:
    - Your Flask app file is not named `app.py` or `wsgi.py` (Flask's default names)
    - You have multiple Flask applications in the same directory
    - You want to be explicit about which file to run

  - `flask run`

    Starts the Flask development server. This command runs your Flask application locally, making it accessible at `http://127.0.0.1:5000` by default.

  - `flask run --debug`

    Starts the Flask development server with debug mode enabled. Debug mode provides:
    - Automatic reloading when code changes
    - Detailed error messages in the browser
    - Interactive debugger for troubleshooting
