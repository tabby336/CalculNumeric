function sendParams() {
	data = {}
	data["lower"] = $('#lowerBound').val();
	data["upper"] = $('#upperBound').val();
	data["function"] = $('#function').val();
	data["num"] = $('#numOfNums').val();
	
	$.ajax({
		type: "POST",
		contentType: "application/json",
		url: "/parameters",
		async: false,
		data: JSON.stringify(data),
		success: function(resp) {
			console.log(resp);
			$('#response').html(resp);
		},
		error: function(resp) {
			$('#response').html(resp);	
		}
	});
}

function calculateFunctionValue() {
	value = $('#xvalue').val();

	$.ajax({
		type: "POST",
		contentType: "application/json",
		url: "/lagrange",
		async: false,
		data: JSON.stringify('{ "value":"' + value +'"}'),
		success: function(resp) {
			console.log(resp);
		}
	});
}