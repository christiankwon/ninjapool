var users = [];
var dests = [];

for( var i = 0; i < raw_users.length; i++ ) {
    var _ = raw_users[i];

    var full = _[3] + ' ' + _[4] + ', ' + _[5] + ' ' + _[6];

    users.push({
        'id': _[0],
        'first_name': _[1],
        'lsat_name': _[2],
        'address': _[3],
        'city': _[4],
        'state': _[5],
        'zip': _[6],
        'arrival': _[7],
        'full_address': full,
        'full_name': _[1] + ' ' + _[2],
        'html_element': $('#user_' + _[0])
    });

    dests.push(full)
}

function showTable() {
    $('#users_table').show()
};

function init() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 47.6104, lng: -122.2007},
        zoom: 12,
        mapTypeId: 'roadmap',
    });

    var markerClick = function(e) {
        var marker = this;

        console.log(this)
    };

    var distMatrixCB = function(response, status) {
        var geocoder = new google.maps.Geocoder();

        var _cb = function(user) {
            return function(results, status) {
                var marker = new google.maps.Marker({
                    map: map,
                    icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
                    position: results[0].geometry.location,
                    user: user
                });

                user.html_element.get(0).marker = marker;

                google.maps.event.addListener(marker, 'click', markerClick);
            }
        };

        geocoder.geocode({'address': response.originAddresses[0]}, function(results, status) {
            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: map,
                icon: 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                position: results[0].geometry.location
            });
            google.maps.event.addListener(marker, 'click', markerClick);
        });

        for( var i = 0; i < response.destinationAddresses.length; i++ ) {
            d = response.destinationAddresses[i];

            var id = users[i].id;

            // if( response.rows[0].elements[i].distance.value > 16093.4 ) continue // 10 miles
            if( response.rows[0].elements[i].distance.value > 8046.72 ) {
                $('#user_' + id).hide()
                continue; // 5 miles
            }
            geocoder.geocode({'address': d}, _cb(users[i]));
        }

        showTable();
    }

    var distMatrix = new google.maps.DistanceMatrixService();
        distMatrix.getDistanceMatrix({
            origins: ["12433 Admiralty Way Everett, WA 98204"],
            destinations: dests,
            travelMode: 'DRIVING',
            // drivingOptions: DrivingOptions,
            unitSystem: google.maps.UnitSystem.IMPERIAL // METRIC,
        }, distMatrixCB);
}
