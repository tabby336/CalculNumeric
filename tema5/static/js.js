STATIC_RELOAD_MATHJAX = '	<script type="text/javascript"> \
								MathJax.Hub.Queue(["Typeset",MathJax.Hub]); \
							</script> \
						'

function initMatrix() {
	$.ajaxSetup({
		async: true,
		timeout: 10000
	});
	$.get('/initMatrix', function(data) {
		resp  = '<div class="container">';
		resp += '<div class="toAlign">' + represent_matrix(data['n'], data['a']) + '</div>';
		resp += '</div>';
		resp += STATIC_RELOAD_MATHJAX;
		$('#initMatrix').html(resp);
	});
}

function schultz() {
	getInverse('schultz');
}

function formula2() {
	getInverse('formula2');
}

function formula3() {
	getInverse('formula3');
}

function getInverse(method) {
	$.ajaxSetup({
		async: true,
		timeout: 10000
	});
	$.get('/' + method, function(data) {
		console.log(data)
		if(typeof data.divergent !== "undefined") {
			$('#' + method).html("Sirul este divergent. Numarul de iteratii facute: " + data['k'] + ".");
		} else {
			resp = '<div class="container">';
			resp += '<div class="toAlign"> Inversa aproximata in ' + data['k'] + ' iteratii.</div>';
			resp += '<div class="toAlign"> Norma ' + data['norm'] + '.</div>';
			resp += '</div>';
			resp += STATIC_RELOAD_MATHJAX;
			$('#' + method).html(resp);
		}
	});
}

function represent_matrix(nr, matrix) {
	var resp = '\\[\\begin{pmatrix}';
	var n = parseInt(nr);
	var matrix_nums = matrix.split(" ");
	console.log(matrix_nums);
	for(var i = 0; i < n*n; i++) {
		if(i%n == n-1) {
			resp = resp + matrix_nums[i] + '\\\\';
		} else {
			resp = resp + matrix_nums[i] + ' & ';
		}
	}
	resp += '\\end{pmatrix}\\]';
	return resp;
}

