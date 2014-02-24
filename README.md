#Frisco Flix
A webapp which plots all the filming locations in San Francisco City based on movie title.

The data is loaded from [DataSF: Filming Locations](https://data.sfgov.org/Arts-Culture-and-Recreation-/Film-Locations-in-San-Francisco/yitu-d5am "DataSF: Filming Locations")

The application is hosted in Open Shift Online @ [Frisco Flix](http://ubercode-senthilsiva.rhcloud.com "Frisco Flix")

#Technical Spec

##Back-end
I chose a common and basic stack on the server side, have used **Python+Flask+Sqlite** for the back-end.
Have also created *REST API* using **Flask-Restful** with json data as output.
There are two *REST API* created 
1. **_/Movies_** : This API will provide the list of all the movie titles
2. **_/GeoLocation_** : This API will provide the geolocation: lat, lng of the movie locations

Once the data is read from the SQLite DB, have used **Werkzeug Simple Cache** for storing the data in memory.

##Front-end
I have used the following libraries
1. **_ Jquery UI Auto-Complete _** : for displaying the Movie Titles as a type-head drop down
2. **_ Jquery Async _** : for making AJAX calls to the REST API
3. ** _ JSON2 _ ** : for parsing the JSON data
4. **_ Google Maps JavaScript API v3 _** : for plotting the filming locations in a map

##TO-DO
###Back-End
1. NOSQL like MongoDB for storing the data, since there is a lot of redundant data stored in sqlite
2. Define models and ORM for managing data in the NOSQL db

###Front-End
1. Async-defer loading of all the javascripts
2. Bundle & Minify all the javascripts loaded in the client
3. Move the inline-styles to a separate stylesheet

##### Housekeeping
1. Define jobs or admin pages which can load the data dynamically from the DATA SF API


