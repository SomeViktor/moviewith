var j= '[["John Travolta", "Samuel L. Jackson"],["Kristen Stewart", "Robert Pattison", " (shitty)"],["Mark Hamill", "Carrie Fisher"],["Anthony Perkins", "Vera Miles"]]';
var i = 1;
var jobject = JSON.parse(j);

var ms;
var actors;




setInterval(updateNames, 3000);
var i = 0;
function updateNames (){
    document.getElementById('ad1').innerHTML = "";  
	document.getElementById('a1').innerHTML = jobject[i][0];
	document.getElementById('a2').innerHTML = jobject[i][1];
    if(jobject[i][2]){
      document.getElementById('ad1').innerHTML = jobject[i][2];  
    }
	i++;
	if(i==4){
		i=0;
	}
}




$( document ).ready(function() {

});


$(function() {
    ms = $('#in1').magicSuggest({
        allowFreeEntries: false,
        data : ["test"]
    });

    $.ajax({
        type: "GET",
        url: "/data/actors.json",
        contentType: "application/json",
        dataType: "json",
        success:function(data){
            console.log("returned data from movie query:")
            actors = data;
            ms.setData(actors);
        }
    })

    
});

function build_list(data){
    console.log(data.length);
    if (data.length == 0){
        $("#result_header").html("<b>No Results :(</b>");
        return
    }
    $("ul").html("");
    for(var i in data) {
        var li = "<li class='list-group-item'>";
        $("ul").append(li.concat(data[i]['title']));
    }
    $("#result_header").html("<b>Woo! Praised be the lord! I got you some results:</b>");


};


function ask_for_suggestions(input_nr, content){
	console.log("ask for suggestion.");
	//console.log(input_nr);
	//console.log(content);
    var exec_url = "/suggestions";
    var post_data = {};
    post_data["content"] = content;
    
    $.ajax({
        type: "POST",
        url: exec_url,
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify(post_data),
        success:function(data){
            console.log("returned data from suggestion query:")
            //console.log(data);
            //var jsonthing = JSON.parse(data);
            //console.log(jsonthing);
            data.forEach(function(actor){
                console.log(actor['name']);


            });
        }
    })
};


function query_movie(){
    var ids = ms.getValue();

    console.log(ids);

    var exec_url = "/query";
    var post_data = {};
    post_data["content"] = ids;

    
    $.ajax({
        type: "POST",
        url: exec_url,
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify(post_data),
        success:function(data){
            console.log("returned data from movie query:")
            console.log(data);
            build_list(data);


            

            
        }
    })
};









