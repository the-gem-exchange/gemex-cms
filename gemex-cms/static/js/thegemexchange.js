var scrollSpeed;

function showNav() {
	$('nav.site-nav').removeClass('hidden');
}

function hideNav() {
	$('nav.site-nav').addClass('hidden');
}

function showHideNav() {
	$(document).bind('mousewheel DOMMouseScroll', function(e){
		scrollSpeed = e.originalEvent.wheelDelta || e.originalEvent.detail || 0;

		let down = scrollSpeed >= 1;
		let up   = scrollSpeed <= -1;

		if (down)   { hideNav(); }
		else if(up) { showNav(); }

		if($('#content').scrollTop() == 0 && $('#homepage-content').length){
			$('nav.site-nav').addClass('transparent');
		}
		else{
			$('nav.site-nav').removeClass('transparent');
		}
	});
}

$(document).ready(function(){
	// Prevents FA from converting <i> tags to <svg> and breaking CSS
	window.FontAwesomeConfig = { autoReplaceSvg: false }
	showHideNav();
	$('body.basic-page nav.site-nav').removeClass('transparent');
})
