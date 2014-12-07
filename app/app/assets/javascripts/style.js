$(document).ready(function(){
	$(".tree_form").submit(function(event){
		event.preventDefault();
		var inpt = $("#text_to_parse").val();
		// http://stackoverflow.com/questions/596351/how-can-i-get-which-radio-is-selected-via-jquery
		var grammar = $('input[name=grammar]:checked', '#parsing').val();
		console.log(grammar);
		$.ajax({
			type: 'POST',
			url: '/path',
			data: {k : inpt, gram: grammar},
			async: false,
		}).done(function(resp){
			if (resp.tree === null) {
				$("#result").html("<em>The given sentence is ungrammatical or could not be parsed.</em>");
			} else {
				$("#result").html("<img src='assets/"+resp.tree+"'>");
			}
			if (resp.counter >= 2) {
				$("#text_to_parse").attr("disabled", "disabled");
				$(".draw_tree").attr("disabled", "disabled");
				$("#survey").css("display","block");
			}
			console.log(resp);
		});
	});

	$("button").click(function(){
		$.post("/path", {k: "clear"}, function(){
			location.reload();
		});
	});
});