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

function carpoolInit() {
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

    var currentTime = new Date();
    currentTime.setHours(6);
    currentTime.setMilliseconds(0);
    currentTime.setSeconds(0);
    currentTime.setMinutes(0);


    var _getETA = function(seconds) {
        currentTime.setSeconds(currentTime.getSeconds() + seconds);

        return currentTime;
    };


    directionsService.route({
        origin: start_address,
        destination: dojo_address,
        waypoints: wpts,
        optimizeWaypoints: true,
        travelMode: 'DRIVING',
        drivingOptions: {
            departureTime: currentTime,
            trafficModel: 'pessimistic'
        }

    }, function(response, status) {
        if( status === 'OK' ) {
            directionsDisplay.setDirections(response);
            var route = response.routes[0];

            var order = route.waypoint_order;
            var dojo = $('#dojo_stop');



            for( var i = 0; i < order.length; i++ ) {
                var user = users[order[i]];

                var leg = route.legs[i];

                var row = $('<tr>');
                row.append($('<td>').text(user.first_name + ' ' + user.last_name))
                row.append($('<td>').text(leg.end_address))
                row.append($('<td>').text(leg.distance.text))
                row.append($('<td>').text(leg.duration.text))
                row.append($('<td>').text(_getETA(leg.duration.value).toLocaleTimeString()))
                row.insertBefore(dojo);
            }

            dojo_leg = route.legs[route.legs.length-1];
            dojo.find('.distance').text(dojo_leg.distance.text)
            dojo.find('.time').text(dojo_leg.duration.text)
            dojo.find('.eta').text(_getETA(dojo_leg.duration.value).toLocaleTimeString())

        } else {
            console.log('Directions failed due to ' + status);
        }
    });
}
