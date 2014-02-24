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

GeoLocation = collections.namedtuple('GeoLocation', ['lat', 'lng'], verbose=True)
		
def save_movie_data(movie):
	con = sqlite3.connect("movie.db")
	con.text_factory = str  #bugger 8-bit bytestrings
	print movie.title + " " + movie.location + " " + movie.lat + " " + movie.lng
	con.execute("INSERT INTO MOVIE (TITLE,LOC,LAT,LNG) VALUES (?,?,?,?)", (movie.title,movie.location,movie.lat,movie.lng))
	con.commit()
	con.close()
	
def get_geo_code(sf_location_string):
	GOOGLE_MAPS_GEOCODE_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
	encoded_args = urllib.urlencode({'address': sf_location_string, 'sensor': 'false'})
	maps_url = '%s?%s' % (GOOGLE_MAPS_GEOCODE_URL, encoded_args)
	response = urllib2.urlopen(maps_url)
	geo_data = json.load(response)
	if geo_data is None:
		return None
	results = geo_data['results']
	#print results
	if len(results) == 0:
		return None
	geocode = results[0].get('geometry', {}).get('location', {})
	lat = str(geocode.get('lat', {}))
	lng = str(geocode.get('lng', {}))
	if len(lat) == 0 or len(lng) == 0:
		return GeoLocation("","")
	return GeoLocation(lat,lng)
	
movie_data = csv.reader(open("Film_Locations_in_San_Francisco.csv"))
for row in movie_data:
	movie_data = Movie(title = str(row[0]),location = str(row[2]))
	print movie_data.location
	geo_loc = get_geo_code(movie_data.location)	
	if geo_loc is None or len(geo_loc.lat) == 0 or len(geo_loc.lng) == 0:
		continue	
	movie_data.set_lng(geo_loc.lng)
	movie_data.set_lat(geo_loc.lat)
	save_movie_data(movie_data)