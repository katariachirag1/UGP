$(function() {

	 $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	var getUrlParameter = function getUrlParameter(sParam) {
    	var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    	for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        	}
    		}
	};
	var error = getUrlParameter('error');
	var array_error=["Username or password is less than 6 character","Form is incomplete","Passwords do not match","Username exists","Existing email","Server error.Please try later","Username or password is incorrect ","User is inactive","'Roll no' or 'id' is already in use"]
	if(error && error < 9 )
	{
		document.querySelector('.results').innerHTML = array_error[error];
		var write=$('#error_message');
		write.innerHTML=array_error[error];
		
		$('#myModal').modal('toggle');	
	}
});

