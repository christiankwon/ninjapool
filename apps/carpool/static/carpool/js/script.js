(function() {
    "use strict";

    var init = function() {
        // Initialize all select elements
        $('select').material_select();

        $('#leave, #arrive').timepicker()
    };

    $(init);

})();
