var express = require('express');
var app = express();
var markdown = require( "markdown" ).markdown;

app.get('/markdown', function(req, res){
    res.send(markdown.toHTML(req.query.body)+'\n');
});

var server = app.listen(3000, function() {
    //console.log('Listening on port %d', server.address().port);
});
