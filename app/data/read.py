import inspect
import json
import urllib
import urllib2
import collections
import csv,sqlite3

class Movie():
	title = ""
	location = ""
	lat = ""
	lng = ""
	def __init__(self,title,location):
		self.title = title
		self.location = '%s, San Francisco, CA' % location
		
	def get_lat(self):
		return self.lat
	def set_lat(self,lat):
		self.lat = lat
	
	def get_lng(self):
		return self.lng
	def set_lng(self,lng):
		self.lng = lng	

con = sqlite3.connect("movie.db")
con.text_factory = str  #bugger 8-bit bytestrings	
title = "180"
cur = con.cursor()
row_data = []
cur.execute("SELECT LAT,LNG FROM MOVIE WHERE TITLE =:title", {"title":title})
rows = cur.fetchall()
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['LAT'] = row[0]
    d['LNG'] = row[1]
    objects_list.append(d)
j = json.dumps(objects_list)
objects_file = 'student_objects.js'
f = open(objects_file,'w')
print >> f, j
	
con.close()	
