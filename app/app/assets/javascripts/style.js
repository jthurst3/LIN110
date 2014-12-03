$(document).ready(function(){
	$("form").submit(function(){
		event.preventDefault();
		var inpt = $("#text_to_parse").val();
		/*$.post("/path", {k : inpt},  function(response, status){
			console.log(status);
			console.log(response);
			$("#result").append("<img src='t.ps'>");
			//$("#result").append(resp);

		}).done(function(){
			alert("done");
		}).always(function(){
			alert("always");
		});*/
		$.ajax({
			type: 'POST',
			url: '/path',
			data: {k : inpt},
			async: false,
			success: function(resp, status){
				//alert(resp);
			}
		}).done(function(resp){
			//var link = resp.substring(6)
			$("#result").append("<img src='assets/"+resp+"'>");
			console.log(resp);
		});
	});
});