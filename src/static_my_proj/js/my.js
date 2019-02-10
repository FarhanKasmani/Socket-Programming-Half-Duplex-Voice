$(document).ready(function() {
	$('#send').click(function() {
		$.ajax({
			url: '/send',
			success: function(result) {
				console.log('Done');
			}
		});
	});
	$('#recieve').click(function() {
		console.log('Yoyo');
		$.ajax({
			url: '/recieve',
			success: function(result) {
				console.log('Done');
			}
		});
	});
});
