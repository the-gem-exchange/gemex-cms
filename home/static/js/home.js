var isScrolling    = false;
var totalSections  = 0;
var currentSection = 1;

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

function bindScroll(){
	$('.homepage #content').bind('mousewheel DOMMouseScroll', function(e){
		e.preventDefault();
		if(!isScrolling){
			// Scrolling Down
			if (e.originalEvent.wheelDelta >= 0 || e.originalEvent.detail >= 0) {
				scrollNext()
			}
			// Scrolling Up
			else {
				scrollPrevious()
			}
		}
	})
}

function scrollToSection(number) {
	isScrolling = true;
	$('.homepage #content').scrollTo(
		$('.home-section-'+number), 500,
		onAfter=function(){
			currentSection = getCurrentSection()
			setTimeout(function(){
				isScrolling = false;
			}, 500)
		}
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
	let current = 0;
	$('[class*="home-section-"]').each(function(i){
		let section_number = i+1;
		let isCurrentSection = $(this)[0].getBoundingClientRect().top == 0;
		if(isCurrentSection){
			current = section_number
		}
	})
	return current
}

$(document).ready(function(){
	totalSections  = $('[class*="home-section-"]').length
	currentSection = getCurrentSection();

	bindArrowKeys();
	bindScroll();

	$('img.background-after').on('load',function(e){
		let img = $(this)
		setTimeout(function(){
			img.closest('div').addClass('background-loaded')
		}, 600)
	})
});
