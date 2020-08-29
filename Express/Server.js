const express = require('express');
const app = express();

app.use(express.static(__dirname + '/public')); //Path file
app.set('port', (process.env.PORT || 3003)); //running port 3003


app.listen(app.get('port'), function () {
  console.log('run at port', app.get('port'));
});

app.get('/', function (req, res) {
  res.jsonp("{Hello World}");
});

app.get('/Hello', function (req, res) {
  res.jsonp("{Hello AOF}");
});
