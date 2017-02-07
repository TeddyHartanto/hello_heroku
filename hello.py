import os
import logging
from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    logging.debug('saying hello')
    name = os.environ.get('NAME', 'Teddy')
    return 'Hello {}!'.format(name)

