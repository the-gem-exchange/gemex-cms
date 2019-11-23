var scrollSpeed;
var transparentNav = false;

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
		if(!isFirefox){
			up   = scrollSpeed >= 1;
			down = scrollSpeed <= -1;
		}

		if (down)   { hideNav(); }
		else if(up) { showNav(); }

		if($('#content').scrollTop() == 0 && transparentNav){
			$('nav.site-nav').addClass('transparent');
		}
		else{
			$('nav.site-nav').removeClass('transparent');
		}
	});
}

function toggleMobileMenu() {
	$('.toggle-mobile-menu').add('.mobile-overlay').on('click', function(e){
		e.preventDefault();
		$('.mobile-nav').toggleClass('active');
		$('.mobile-overlay').toggleClass('active');
	});
}

$(document).ready(function(){
	showHideNav();
	toggleMobileMenu();

	if($('#homepage-content').length || $('.comicpage').length){
		transparentNav = true;
	}
	else{
		$('nav.site-nav').removeClass('transparent');
	}
})
