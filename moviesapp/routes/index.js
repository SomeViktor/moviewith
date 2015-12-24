var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.sendFile("public/index.html")
});


router.get('/suggestions', function(req, res, next) {
  console.log("got request");
  var response =[];
  response.push(req["content"]);
  //response.push("John Travolta");
  //response.push("John Travolta");
  res.json(response);
});


module.exports = router;
