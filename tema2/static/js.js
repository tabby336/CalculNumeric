STATIC_RELOAD_MATHJAX = '	<script type="text/javascript"> \
								MathJax.Hub.Queue(["Typeset",MathJax.Hub]); \
							</script> \
						'

function choleski() {
	$.ajaxSetup({
		async: true,
		timeout: 10000
	});
	$.get('/choleski', function(data){
		resp  = '<div class="container">';
		resp +=  '<div class="toAlign">' + represent_matrix(data['n'], data['a']) + '</div>';
		resp += '<div class="toAlign sign"> = </div>';
		resp += '<div class="toAlign">' + represent_matrix(data['n'], data['l']) + '</div>';
		resp += '<div class="toAlign">' + represent_matrix(data['n'], data['d']) + '</div>';
		resp += '<div class="toAlign">' + represent_matrix(data['n'], data['lt']) + '</div>';
		resp += '</div>';
		resp += STATIC_RELOAD_MATHJAX;
		$('#choleski').html(resp);
	});
}

function determinant() {
	$.ajaxSetup({
		async: true,
		timeout: 10000
	});
	$.get('/determinant', function(data){
		resp  = '<div class="container">';
		resp += '<div class="toAlign sign"> D = </div>';  
		resp +=  '<div class="toAlign">' +represent_matrix(data['n'], data['d']) + '</div>';
		resp += '</div>';

		resp += '<div class="container">';
		resp += '<p class="eq"><i>det</i>(D) =' + data['det'];
		resp += '</p></div>';
		resp += STATIC_RELOAD_MATHJAX;
		$('#determinant').html(resp);
	});
}

function solution() {
	$.ajaxSetup({
		async: true,
		timeout: 10000
	});
	$.get('/solution', function(data){
		console.log(data['x']);
		resp  = '<div class="container">';
		resp += '<div class="toAlign">' + represent_matrix(data['n'], data['a']) + '</div>';
		resp += '<div class="toAlign">' + represent_vector(data['n'], data['x']) + '</div>';
		resp += '<div class="toAlign sign"> ~ </div>';
		resp += '<div class="toAlign">' + represent_vector(data['n'], data['b']) + '</div>';
		resp += '</div>';
		resp += STATIC_RELOAD_MATHJAX;
		$('#solution').html(resp);
	});
}

function lu() {
	$.ajaxSetup({
		async: true,
		timeout: 10000
	});
	$.get('/lu', function(data){
		resp  = '<div class="container">';
		resp += '<div class="toAlign sign"> P = </div>';  
		resp += '<div class="toAlign">' + represent_matrix(data['n'], data['P']) + '</div>';
		resp += '</div>';

		resp += '<div class="container">';
		resp += '<div class="toAlign sign"> L = </div>';  
		resp += '<div class="toAlign">' + represent_matrix(data['n'], data['L']) + '</div>';
		resp += '</div>';

		resp += '<div class="container">';
		resp += '<div class="toAlign sign"> U = </div>';  
		resp += '<div class="toAlign">' + represent_matrix(data['n'], data['U']) + '</div>';
		resp += '</div>';

		resp += '<div class="container">';
		resp += '<div class="toAlign sign"> Solution = </div>';  
		resp += '<div class="toAlign">' + represent_vector(data['n'], data['solution']) + '</div>';
		resp += '</div>';

		resp += STATIC_RELOAD_MATHJAX;
		$('#lu').html(resp);
	});
}

function norm() {
	$.ajaxSetup({
		async: true,
		timeout: 10000
	});
	$.get('/norm', function(data){
		resp  = '<div class="container">';
		resp += '<p class="eq"> Ax - b </p>';
		resp += '</div>';

		resp += '<div class="container">';
		resp += '<div class="toAlign">' + represent_matrix(data['n'], data['a']) + '</div>';
		resp += '<div class="toAlign">' + represent_vector(data['n'], data['x']) + '</div>';
		resp += '<div class="toAlign sign"> - </div>';
		resp += '<div class="toAlign">' + represent_vector(data['n'], data['b']) + '</div>';
		resp += '<div class="toAlign sign"> = </div>';
		resp += '<div class="toAlign">' + represent_vector(data['n'], data['prod_terms']) + '</div>';
		resp += '<div class="toAlign sign"> - </div>';
		resp += '<div class="toAlign">' + represent_vector(data['n'], data['b']) + '</div>';
		resp += '</div>';

		resp += '<div class="container">';
		resp += '<div class="toAlign eq"> ||Ax-b|| =  </div>';
		resp += '<div class="toAlign eq">' + data['norm'] + '</div>';
		resp += '</div>'
		
		resp += STATIC_RELOAD_MATHJAX;
		$('#norm').html(resp);
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

function represent_vector(nr, matrix) {
	var resp = '\\[\\begin{pmatrix}';
	var n = parseInt(nr);
	var matrix_nums = matrix.split(" ");
	console.log(matrix_nums);
	for(var i = 0; i < n; i++) {
		resp = resp + matrix_nums[i] + '\\\\';
	}
	resp += '\\end{pmatrix}\\]';
	return resp;
}

