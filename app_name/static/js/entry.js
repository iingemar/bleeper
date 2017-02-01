var content = require("./content.js");
require("../css/main.less");


// Test underscore
console.log('underscore: ', _.first([5, 4, 3, 2, 1]));

// Test Backbone
var IndexView = Backbone.View.extend({
    el: $('#backbone-content'),

    events: {
        'click .btn': 'click'
    },

    render: function(){
        console.log('render');
    },

    click: () =>  {
        console.log('ES6 click');
    }
});


var indexView = new IndexView();

indexView.render();


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
}


$(document).ready(function() {
    console.log('ajax');

    var q = getParameterByName('q');
    console.log('q=' + q);

    $.ajax({
        url: '/api/bleeps',
        data: {
            'q': q
        },
        method: 'GET',
        success: function(bleeps) {
            console.log('SUCCESS');
            console.log(bleeps);
            _.each(bleeps, function(bleep){
                console.log(bleep);
                console.log(bleep.content);
                $('.bleep-container').append('<li>' + bleep.content + '</li>');
            })
        },
        error: function(bleeps) {
            console.log('ERROR');
            console.log(bleeps);
        }

    });
});