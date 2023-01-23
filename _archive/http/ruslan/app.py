from flask import Flask
from flask import Response

app_ = Flask(__name__)


@app_.route('/hello')
def hello():
    return Response("Hello world from Flask!", mimetype='text/plain')

app = app_.wsgi_app
