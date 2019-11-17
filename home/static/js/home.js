var isScrolling    = false;
var totalSections  = 0;
var currentSection = 1;
var scrollSpeed    = 0;


function unbindArrowKeys(){
	$(document).off('keydown.tabs');
}

function bindArrowKeys(){
	$(document).on('keydown.tabs', function(e){
		const arrow_up   = 38;
		const arrow_down = 40;
		const keyCode    = e.keyCode;

		if(keyCode == arrow_up){
			e.preventDefault()
			scrollPrevious()
		}
		if(keyCode == arrow_down){
			e.preventDefault()
			scrollNext()
		}
	})
}

function unbindScroll(){
	$('.homepage #content').off('mousewheel DOMMouseScroll');
}

function bindScroll(){
	$('.homepage #content').bind('mousewheel DOMMouseScroll', function(e){
		e.preventDefault();
		let newScrollSpeed = e.originalEvent.wheelDelta || e.originalEvent.detail || 0;
		// If previous scoll event finished and the new scroll is greater than the last recorded scroll event
		if(!isScrolling && Math.abs(newScrollSpeed) > scrollSpeed+2){
			// Scroll down
			if (newScrollSpeed >= 1) scrollNext();
			// Scroll up
			else if(newScrollSpeed <= -1) scrollPrevious();
			console.log("Scrolled")
		}
		scrollSpeed = Math.abs(newScrollSpeed)
	})
}

function scrollToSection(number) {
	isScrolling = true;
	$('.homepage #content').scrollTo(
		$('.home-section-'+number), 300,
		{
			onAfter:function(){
				getCurrentSection();
				updateJumplinks();
				setTimeout(function(){
					isScrolling = false;
				}, 300)
			},
			behavior: 'smooth'
		},
	)
}

function scrollNext(){
	let next = currentSection + 1;
	if(next <= totalSections){
		scrollToSection(next)
	}
}

function scrollPrevious(){
	let prev = currentSection - 1;
	if(prev > 0){
		scrollToSection(prev)
	}
}

function getCurrentSection(){
	$('[class*="home-section-"]').each(function(i){
		let section_number = i+1;
		let isCurrentSection = $(this)[0].getBoundingClientRect().top == 0;
		if(isCurrentSection){
			currentSection = section_number
		}
	});
}

function updateJumplinks(){
	$('[class*="home-link-"]').each(function(i){
		if(i+1 == currentSection) $(this).addClass('active')
		else $(this).removeClass('active')
	});
}

/* Disable on mobile */
function toggleHomeJsOnResize(){
	$(window).resize(function(){
		if(window.innerWidth > 991){
			initHome();
		}
		if(window.innerWidth <= 991){
			unbindScroll();
			unbindArrowKeys();
		}
	});
}

function initHome(){
	totalSections  = $('[class*="home-section-"]').length;
	getCurrentSection();
	bindArrowKeys();
	bindScroll();
}

$(document).ready(function(){
	initHome();
	toggleHomeJsOnResize();
	updateJumplinks();
});
