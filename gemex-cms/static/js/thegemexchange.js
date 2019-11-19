var currentPos  = $(document).scrollTop();
var scrollingUp = false;
var newScrollPos;

function showHideNav() {
	newScrollPos = $(document).scrollTop();

	// User is scrolling down - Hide Nav
	if (newScrollPos > currentPos && !scrollingUp && newScrollPos >= 70) { // Only hide if we are scrolled past the height of the header
		$('nav.site-nav').addClass('hidden');
		scrollingUp = !scrollingUp;
	}
	// User is scrolling up - Show Nav
	else if(newScrollPos < currentPos && scrollingUp) {
		$('nav.site-nav').removeClass('hidden');
		scrollingUp = !scrollingUp;
	}

	if(newScrollPos < 100) $('nav.site-nav').addClass('transparent');
	else                   $('nav.site-nav').removeClass('transparent');

	currentPos = newScrollPos;
}

$(document).on('scroll', function() {
	showHideNav();
});

$(document).ready(function(){
	// Prevents FA from converting <i> tags to <svg> and breaking CSS
	window.FontAwesomeConfig = { autoReplaceSvg: false }
})
