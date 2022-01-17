import logging

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_python_static_files]
