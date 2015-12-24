var j= '[["John Travolta", "Samuel L. Jackson"],["Kristen Stewart", "Robert Pattison", " (shitty)"],["Mark Hamill", "Carrie Fisher"],["Anthony Perkins", "Vera Miles"]]';
var i = 1;
var jobject = JSON.parse(j);


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
    
	
	$('#in1').on('input', function(event){
		ask_for_suggestions(1,$('#in1').val() );
    });
    $('#in2').on('input', function(event){
        ask_for_suggestions(2,$('#in2').val() );
    });
    $('#in3').on('input', function(event){
        ask_for_suggestions(3,$('#in3').val() );
    });
});


function ask_for_suggestions(input_nr, content){
	console.log("ask for suggestion:");
	console.log(input_nr);
	console.log(content);
    var exec_url = "/suggestions";
    var post_data = {};
    post_data["content"] = content;
    
    $.ajax({
        type: "GET",
        url: exec_url,
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify(post_data),
        success:function(data){
            console.log(data);
            //var jsonthing = JSON.parse(data);
            //console.log(jsonthing);
            
        }
    })
};



















