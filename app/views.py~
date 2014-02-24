from flask import Flask,render_template
from flask.ext import restful
from app import app
from api.movie.controller import Movies
from api.geolocation.controller import GeoLocation
from dbcontext import factory

api = restful.Api(app)
@app.before_request
def before_request():
	factory.connect_db()

@app.teardown_request
def teardown_request(exception):
	factory.close_db()

@app.teardown_appcontext
def close_connection(exception):
	factory.close_connection()
  
@app.route('/')
@app.route('/index')
def hello_world(name='Ben\'s Site'):
    return render_template('index.html', name=name)

api.add_resource(Movies, '/Movies')
api.add_resource(GeoLocation, '/GeoLocation/<string:movie_title>')


