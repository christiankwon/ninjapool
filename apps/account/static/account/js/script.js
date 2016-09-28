(function() {
    "use strict";

    var init = function() {
        var _populateLogin = function() {
            $('#login-email').val('test@email.com').focus();
            $('#login-pass').val('1q2w3e4r').focus();
        };

        var _populateRegister = function() {
            $('#register-fname').val('FirstTesting').focus();
            $('#register-lname').val('LastTesting').focus();
            $('#register-email').val('test@email.com').focus();
            $('#register-pass').val('1q2w3e4r').focus();
            $('#register-cpass').val('1q2w3e4r').focus();
        };

        $('#populateLogin').on('click', _populateLogin);
        $('#populateRegister').on('click', _populateRegister);
    };

    $(init);

//login display jQuery
    $('#logintoregister a').on('click', function(){
        $('.loginform').toggle();
        $('.registerform').toggle();
        $('#logintoregister').toggle();
    })


    $('#backtologin').on('click', function(){
        $('.loginform').toggle();
        $('.registerform').toggle();
        $('#logintoregister').toggle();
    })



})();


