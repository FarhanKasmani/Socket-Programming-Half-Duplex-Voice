$(document).ready(function() {
	var x1 = null;
	$('#send').click(function() {
		x1 = $.ajax({
			url: '/send',
			beforeSend: function() {
				if (x1 != null) {
					x1.abort();
				}
			},
			success: function(result) {
				console.log('Done');
			}
		});
	});
	$('#recieve').click(function() {
		console.log('Yoyo');
		x1 = $.ajax({
			url: '/recieve',
			beforeSend: function() {
				if (x1 != null) {
					x1.abort();
				}
			},
			success: function(result) {
				console.log('Done');
			}
		});
	});
});
