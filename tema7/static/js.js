function generateChartData(data) {
	console.log("From chart data function", data);
	console.log(data["expected"][0]["x"]);
    var chartData = [];
    

    for (var i = 0; i < data["expected"].length; i++) {
        var newDate = data["expected"][i]["x"];
        

        var expected = data["expected"][i]["y"];

        var approximated = data["real"][i]["y"];

        chartData.push({
            date: newDate,
            visits: expected,
            views: approximated
        });
    }
    return chartData;
}

function zoomChart(){
    chart.zoomToIndexes(chart.dataProvider.length - 20, chart.dataProvider.length - 1);
}



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
			// resp = JSON.parse(resp);
			// $('#response').html(resp);
			var chartData = generateChartData(resp);
			console.log(chartData);

			var chart = AmCharts.makeChart("chartdiv", {
			    "type": "serial",
			    "theme": "light",
			    "legend": {
			        "useGraphSettings": true,
					"valueWidth": 150,
					"align": "left"
			    },
			    "dataProvider": chartData,
			    "synchronizeGrid":true,
			    "valueAxes": [{
			        "id":"v1",
			        "axisColor": "#FF6600",
			        "axisThickness": 2,
			        "axisAlpha": 1,
			        "position": "left"
			    }, {
			        "id":"v3",
			        "axisColor": "#B0DE09",
			        "axisThickness": 2,
			        "gridAlpha": 0,
			        "offset": 50,
			        "axisAlpha": 1,
			        "position": "left"
			    }],
			    "graphs": [{
			        "valueAxis": "v1",
			        "lineColor": "#FF6600",
			        "bullet": "round",
			        "bulletBorderThickness": 1,
			        "hideBulletsCount": 30,
			        "title": "expected",
			        "type": "smoothedLine",
			        "valueField": "visits",
					"fillAlphas": 0
			    }, {
			        "valueAxis": "v3",
			        "lineColor": "#B0DE09",
			        "bullet": "triangleUp",
			        "bulletBorderThickness": 1,
			        "hideBulletsCount": 30,
			        "title": "actual",
			        "type": "smoothedLine",
			        "valueField": "views",
					"fillAlphas": 0
			    }],
			    "chartScrollbar": {},
			    "chartCursor": {
			        "cursorPosition": "mouse"
			    },
			    "categoryField": "date",
			    "categoryAxis": {
			        "parseDates": false,
			        "axisColor": "#DADADA",
			        "minorGridEnabled": true,
			        "autoGridCount": false
			    },
			    "export": {
			    	"enabled": true,
			        "position": "bottom-right"
			     }
						});
					},
		error: function(resp) {
			$('#response').html(resp);	
		}
	});
}

function periodic() {
	$.ajax({
		type: "POST",
		contentType: "application/json",
		url: "/periodic",
		async: false,
		success: function(resp) {
			console.log(resp);
			// resp = JSON.parse(resp);
			// $('#response').html(resp);
			var chartData = generateChartData(resp);
			console.log(chartData);

			var chart = AmCharts.makeChart("chartdiv", {
			    "type": "serial",
			    "theme": "light",
			    "legend": {
			        "useGraphSettings": true,
					"valueWidth": 150,
					"align": "left"
			    },
			    "dataProvider": chartData,
			    "synchronizeGrid":true,
			    "valueAxes": [{
			        "id":"v1",
			        "axisColor": "#FF6600",
			        "axisThickness": 2,
			        "axisAlpha": 1,
			        "position": "left"
			    }, {
			        "id":"v3",
			        "axisColor": "#B0DE09",
			        "axisThickness": 2,
			        "gridAlpha": 0,
			        "offset": 50,
			        "axisAlpha": 1,
			        "position": "left"
			    }],
			    "graphs": [{
			        "valueAxis": "v1",
			        "lineColor": "#FF6600",
			        "bullet": "round",
			        "bulletBorderThickness": 1,
			        "hideBulletsCount": 30,
			        "title": "expected",
			        "type": "smoothedLine",
			        "valueField": "visits",
					"fillAlphas": 0
			    }, {
			        "valueAxis": "v3",
			        "lineColor": "#B0DE09",
			        "bullet": "triangleUp",
			        "bulletBorderThickness": 1,
			        "hideBulletsCount": 30,
			        "title": "actual",
			        "type": "smoothedLine",
			        "valueField": "views",
					"fillAlphas": 0
			    }],
			    "chartScrollbar": {},
			    "chartCursor": {
			        "cursorPosition": "mouse"
			    },
			    "categoryField": "date",
			    "categoryAxis": {
			        "parseDates": false,
			        "axisColor": "#DADADA",
			        "minorGridEnabled": true,
			        "autoGridCount": false
			    },
			    "export": {
			    	"enabled": true,
			        "position": "bottom-right"
			     }
						});
					},
		error: function(resp) {
			$('#response').html(resp);	
		}
	});
}

function calculateFunctionValue() {
	data = {}
	data["lower"] = $('#lowerBound').val();
	data["upper"] = $('#upperBound').val();
	data["function"] = $('#function').val();
	data["num"] = $('#numOfNums').val();
	data["value"] = $('#xvalue').val();

	$.ajax({
		type: "POST",
		contentType: "application/json",
		url: "/lagrange",
		async: false,
		data: JSON.stringify(data),
		success: function(resp) {
			$("#result").html(resp["value"]);
			console.log(resp);
		}
	});
}

function periodValue() {
	data = {}
	data["value"] = $('#xxvalue').val();

	$.ajax({
		type: "POST",
		contentType: "application/json",
		url: "/periodicCompute",
		async: false,
		data: JSON.stringify(data),
		success: function(resp) {
			console.log(resp);
			$("#result2").html(resp["value"]);
		}
	});
}



// generate some random data, quite different range
