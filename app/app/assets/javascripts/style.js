$(document).ready(function(){
	$(".tree_form").submit(function(event){
		event.preventDefault();
		var inpt = $("#text_to_parse").val();
		// http://stackoverflow.com/questions/596351/how-can-i-get-which-radio-is-selected-via-jquery
		var grammar = $('input[name=grammar]:checked', '#parsing').val();
		$.ajax({
			type: 'POST',
			url: '/path',
			data: {k : inpt, gram: parseInt(grammar)},
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
	$(".phonology_form").submit(function(event){
		event.preventDefault();
		// get phones
		var phone1 = $("#first_phone").val();
		var phone2 = $("#second_phone").val();
		// get words
		var words = [];
		for (var i = 0; i < 5; i++) {
			words.push($("#word" + i).val());
		};
		$.ajax({
			type: 'POST',
			url: '/phoneme_allophone_program',
			data: {phones : phone1 + " " + phone2, words: words},
			async: false,
		}).done(function(resp){
			// if (resp.tree === null) {
			// 	$("#result").html("<em>The given sentence is ungrammatical or could not be parsed.</em>");
			// } else {
				$("#result").html("Success");
			// }
			if (resp.counter >= 2) {
				$("#text_to_parse").attr("disabled", "disabled");
				$(".draw_tree").attr("disabled", "disabled");
				$("#survey").css("display","block");
			}
			console.log(resp);
		});
	});

	$("#parsing-submit-button").click(function(){
		$.post("/path", {k: "clear"}, function(){
			// location.reload();
		});
	});
	$("#phonology-submit-button").click(function(){
		$.post("/phoneme_allophone_program", {k: "clear"}, function(){
			// location.reload();
		});
	});
});