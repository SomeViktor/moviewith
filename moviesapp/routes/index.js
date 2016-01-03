var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/mo');



var movieSchema = mongoose.Schema({
    title: String,
    actors: [String]
});

var Movie = mongoose.model('Movie', movieSchema);


var actorSchema = mongoose.Schema({
    name: String,
    
});

var Actor = mongoose.model('Actor', actorSchema);


/* GET home page. */
router.get('/', function(req, res, next) {
  res.sendFile("public/index.html")
});


router.post('/suggestions', function(req, res, next) {
	input = req.body.content;
	var response = "asfd";
  	console.log("got request");
  	//console.log(req);
  	re_string = "^" + input + "";
  	console.log(re_string);
	Actor.find({name: { $regex: re_string, $options: 'i' }}, function (err, movies) {
	  if (err) return console.error(err);
	  //console.log(movies);
	  res.send(movies);
	})
  
});


router.post('/query', function(req, res, next) {
	content = req.body.content;
	console.log(content);
	query = [];
	content.forEach(function(actor){
		query.push({actors:{ $eq: actor }});

	});
	console.log(query);
	Movie.find({$and : query}, function(err, movies){
		console.log(movies);
		res.send(movies);
//

	});

	//search for movie in collection where all three actors are keys

	//if some result:


});

module.exports = router;
