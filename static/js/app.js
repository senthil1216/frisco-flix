var markersArray = [];

function clearOverlays(){
	for(var i=0; i< markersArray.length; i++){
		markersArray[i].setMap(null);
	}
	markersArray.length = 0;
}

function initialize() {		
	var myLatlng = new google.maps.LatLng(37.7577,-122.4376);
	var mapOptions = {
		zoom: 4,
		center: myLatlng
	};

	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
	map.setZoom(12);  
   
	var input = /** @type {HTMLInputElement} */(
      document.getElementById('pac-input'));
	map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
	}
	
function createMarker(mapObj,title,lat,lng,contentString){
	
	var pos = new google.maps.LatLng(lat,lng);
	mapObj.setCenter(pos);
	var marker = new google.maps.Marker({
		  position: pos,
		  map: mapObj,
		  title: title
	});
	
	markersArray.push(marker);

	if(contentString === undefined) return;
	if(contentString === null) return;
	if(contentString.length == 0) return;
	
	var infowindow = new google.maps.InfoWindow({
		content: contentString,      
	});

	google.maps.event.addListener(marker, 'click', function() {
		infowindow.open(mapObj,marker);
	});
}


function get_location(movieTitle){
	$.ajax({
		type: 'GET',
		url: '/GeoLocation/' + movieTitle,
		datatype: 'json',
		success: function(data){
			clearOverlays();
			var loc_obj = JSON.parse(data);
			for(var i = 0;i < loc_obj.length;i++){
				createMarker(map,movieTitle,loc_obj[i].LAT,loc_obj[i].LNG,movieTitle);
			}					
		}
	});	
}

$(document).ready(function() {
	$.ajax({ 
	    type: 'GET',
	    url: '/Movies',
	    dataType: 'json',
	    success: function (data) {
		  var availableTags = JSON.parse(data);
		    $( "#pac-input" ).autocomplete({
				source: availableTags,
				select: function( event, ui ) {
					if(ui.item){
						get_location(ui.item.value);
					}
				
				}
			});
		}
	});
})
google.maps.event.addDomListener(window, 'load', initialize);
