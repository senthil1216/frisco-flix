import json
import urllib
import urllib2
import datetime
import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client['movie']
collection = db['MovieInfo']

class Movie():
	title = ""
	location = []
	def __init__(self,title):
		self.title = title		
	def set_location(self,location):
		if not location in self.location:
			self.location = location
	def get_location(self):
		return self.location
	def get_title(self):
		return self.title

encoded_args = urllib.urlencode({'$select':'title, locations'})		
sf_url = "https://data.sfgov.org/api/views/yitu-d5am/rows.json?"+encoded_args
response = urllib2.urlopen(sf_url)
movie_records = json.load(response)
for s in movie_records:
	print s['title']

"""
for rec in movie_records["data"]:
	#print rec[8]
	moviedata = Movie(title = str(rec[8]),location = str(rec[10]))		
	data = {
			'title' : moviedata.get_title(),
			'location':[""]
			}
	alreadyexist = collection.find_one(data)
	if alreadyexist is None:
		print data
		collection.insert(data)
"""