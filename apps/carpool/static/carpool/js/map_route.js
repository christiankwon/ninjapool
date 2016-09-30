var users = [];
var dests = [];

for( var i = 0; i < raw_users.length; i++ ) {
    var _ = raw_users[i];

    var full = _[3] + ' ' + _[4] + ', ' + _[5] + ' ' + _[6];

    users.push({
        'id': _[0],
        'first_name': _[1],
        'last_name': _[2],
        'address': _[3],
        'city': _[4],
        'state': _[5],
        'zip': _[6],
        'arrival': _[7],
        'full_address': full,
        'full_name': _[1] + ' ' + _[2]
    });

    dests.push(full);
}

function routeInit() {
    var directionsDisplay = new google.maps.DirectionsRenderer();
    var directionsService = new google.maps.DirectionsService();
    var dojo = new google.maps.LatLng(47.6104, -122.2007);
    var mapOptions = {
        zoom: 12,
        mapTypeId: 'roadmap',
        center: dojo
    }
    var map = new google.maps.Map(document.getElementById('map'), mapOptions);
    directionsDisplay.setMap(map);

    var wpts = [];
    for( var i = 0; i < dests.length; i++ ) {
        wpts.push({
            location: dests[i],
            stopover: true
        });
    }

    directionsService.route({
        origin: start_address,
        destination: dojo_address,
        waypoints: wpts,
        optimizeWaypoints: true,
        travelMode: 'DRIVING'
    }, function(response, status) {
        if( status === 'OK' ) {
            directionsDisplay.setDirections(response);
            var route = response.routes[0];
            var summaryPanel = document.getElementById('directions-panel');
            summaryPanel.innerHTML = '';
            // For each route, display summary information.
            for (var i = 0; i < route.legs.length; i++) {
                var routeSegment = i + 1;
                summaryPanel.innerHTML += '<b>Route Segment: ' + routeSegment +
                '</b><br>';
                console.log(route)
                summaryPanel.innerHTML += route.legs[i].start_address + ' to ';
                summaryPanel.innerHTML += route.legs[i].end_address + '<br>';
                summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>';
            }
        } else {
            console.log('Directions failed due to ' + status);
        }
    });
}
