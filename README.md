# Flask

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

## Official Documentation

- [Installation](https://flask.palletsprojects.com/en/stable/installation/)

- [Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)

- [Jinja2 - Template Designer Documentation](https://jinja.palletsprojects.com/en/stable/templates/)
  - [Template Inheritance](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/)

- [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)

- [User's Guide](https://flask.palletsprojects.com/en/stable/#user-s-guide)

- [CLI](https://flask.palletsprojects.com/en/stable/cli/)

- [Development Server](https://flask.palletsprojects.com/en/stable/server/)

- [API Reference](https://flask.palletsprojects.com/en/stable/#api-reference)

- [Deploying to Production](https://flask.palletsprojects.com/en/stable/deploying/)

- More

  - [Patterns](https://flask.palletsprojects.com/en/stable/patterns/)
  - [API](https://flask.palletsprojects.com/en/stable/api/)
  - [Additional Notes](https://flask.palletsprojects.com/en/stable/#additional-notes)

- Main dependencies

   - [Werkzeug - WSGI toolkit](https://werkzeug.palletsprojects.com/en/stable/)
   - [Jinja - Template engine](https://jinja.palletsprojects.com/en/stable/)
   - [Click - CLI toolkit](https://click.palletsprojects.com/en/stable/)
