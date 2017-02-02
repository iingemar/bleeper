require("../css/main.less");

var getParameterByName = function(name, url) {
    if (!url) {
      url = window.location.href;
    }
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
};

var getBleeps = function() {
    console.log('getBleeps');

    $.ajax({
        url: '/api/bleeps',
        data: {
            'q': getParameterByName('q')
        },
        method: 'GET',
        success: function(bleeps) {
            console.log('getBleeps: SUCCESS');
            console.log('getBleeps:', bleeps);

            $('.bleep-container').empty();
            _.each(bleeps.results, function(bleep){
                $('.bleep-container').append('<li>' + bleep.content +  '<br/> '+ bleep.date_display +'</li>');
            })
        }
    });
};

$(document).ready(function() {
    getBleeps();

    $('#bleep-create-form').submit(function(e) {
        e.preventDefault();
        var formData = $(this).serialize();

        $.ajax({
            url: '/api/bleeps/create/',
            data: formData,
            method: 'POST',
            success: function(result) {
                console.log('SUCCESS');
                console.log(result.status);
                console.log(result.statusText);
                getBleeps();
            },
            error: function(result) {
                console.log('ERROR');
                console.log(result.status);
                console.log(result.statusText);
            }

        });
    });

});