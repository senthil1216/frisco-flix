from flask.ext import restful
from app.util import appfabric
from app import app
from app.dbcontext import factory
import json
from collections import OrderedDict
cache_repo = appfabric.cache_repo

class GeoLocation(restful.Resource):
    def get(self,movie_title):
	if not cache_repo.get(movie_title) is None:
		return cache_repo.get(movie_title)
	objects_list = []
	for row in factory.query_db('SELECT LAT,LNG FROM MOVIE WHERE TITLE=:title;', {"title":movie_title}):
	    d = OrderedDict()
            d['LAT'] = row[0]
            d['LNG'] = row[1]
            objects_list.append(d)
	data = json.dumps(objects_list)
	cache_repo.set(movie_title, data)
	return cache_repo.get(movie_title)
