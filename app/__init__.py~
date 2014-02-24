import os
from flask import Flask
app = Flask(__name__)  
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE = os.path.abspath(os.path.dirname(__file__)) + '/data/movie.db'
))

from app import views
