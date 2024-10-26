var express = require('express');
var fs = require('fs')
app = express();
var msg = process.env.APP_MSG;
var response;
app.get('/', function (req, res) {
    response = 'Value in the APP_MSG env var is => ' + msg + '\n';
    fs.readFile('/opt/app-root/secure/myapp.sec', 'utf8', function (secerr,secdata) {
        if (secerr) {
            console.log(secerr + '\n');
            response += secerr + '\n';
        }
        else {
            response += 'The secret is => ' + secdata + '\n';
        }
        res.send(response);
    });
});

app.listen(8080, function () {
  console.log('Server listening on port 8080...');
});
