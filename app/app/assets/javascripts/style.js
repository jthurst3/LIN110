$(document).ready(function(){
	$(".tree_form").submit(function(event){
		event.preventDefault();
		var inpt = $("#text_to_parse").val();
		// http://stackoverflow.com/questions/596351/how-can-i-get-which-radio-is-selected-via-jquery
		var grammar = $('input[name=grammar]:checked', '#parsing').val();
		console.log(grammar);
		// default should be first grammar
		if (grammar === undefined) {grammar = "1"};
		console.log(grammar);
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
			// reset the result text
			$("#result").html("");
			// output the environments
			$("#result").append("<b>Environments for [" + phone1 + "]</b>: " + resp.env1 + "<br>");
			$("#result").append("<b>Environments for [" + phone2 + "]</b>: " + resp.env2 + "<br>");
			// output complementary or contrastive
			$("#result").append("<b>[" + phone1 + "]</b> and <b> [" + phone2 + "]</b> are in " + resp.result1 + ".<br>");
			// output same or different
			if (resp.result2 !== null) {
				$("#result").append("<b>[" + phone1 + "]</b> and <b> [" + phone2 + "]</b> are " + resp.result2 + ".<br>");
			};
			if (resp.counter >= 2) {
				$("#text_to_parse").attr("disabled", "disabled");
				$(".draw_tree").attr("disabled", "disabled");
				$("#survey").css("display","block");
			}
			console.log(resp);
		});
	});

	$(".ipa_fields").focus(function(event) {
		$(".ipa_fields").attr("field_selected", "false");
		$(this).attr("field_selected", "true");
	});
	$(".english_fields").focus(function(event) {
		$(".ipa_fields").attr("field_selected", "false");
	});

	$(".ipa_sounds").click(function(event) {
		// insert the button text into the selected IPA text field
		// really lazy way to do this!
		if ($("#first_phone").attr("field_selected") === "true") {
			$("#first_phone").val($(this).text());
		}
		else if ($("#second_phone").attr("field_selected") === "true") {
			$("#second_phone").val($(this).text());
		}
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