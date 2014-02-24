from flask.ext import restful
from app.util import appfabric
from app import app
from app.dbcontext import factory
import json

cache_repo = appfabric.cache_repo

class Movies(restful.Resource):
    def get(self):
        if not cache_repo.get("MOVIES") is None:
            return cache_repo.get("MOVIES")
        movie_titles = []
        for title in factory.query_db('SELECT DISTINCT(TITLE) FROM MOVIE;'):
            movie_titles.append(str(title[0]))
        cache_data = json.dumps(movie_titles)
        cache_repo.set("MOVIES",cache_data)
        return cache_repo.get("MOVIES")
