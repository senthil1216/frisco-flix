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

1. **_Jquery UI Auto-Complete_** : for displaying the Movie Titles as a type-head drop down

2. **_Jquery Async_** : for making AJAX calls to the REST API

3. **_JSON2_** : for parsing the JSON data

4. **_Google Maps JavaScript API v3_** : for plotting the filming locations in a map

##TO-DO
###Back-End
1. NOSQL like MongoDB for storing the data, since there is a lot of redundant data stored in sqlite
2. Define models and ORM for managing data in the NOSQL db

###Front-End
1. Async-defer loading of all the javascripts
2. Bundle & Minify all the javascripts loaded in the client
3. Move the inline-styles to a separate stylesheet

###Unit-Test
1. Unit Tests for JS code
2. Unit Tests for REST API calls

##### Housekeeping
1. Define jobs or admin pages which can load the data dynamically from the DATA SF API

### Resume Online
My Resume is at the AppEngine url [Senthil Sivasubramanian](http://root-node.appspot.com/me)

### Other Projects:

1. [Blogging Platform](https://github.com/senthil1216/root-node) : Developed a blogging platform using Flask Python framework and deployment using Google App Engine


2. [Telemetry](https://github.com/senthil1216/telemetry) : Developed a telemetry framework using Flask Python which captures all user events from client side and sends the data to REST API exposed from server.
