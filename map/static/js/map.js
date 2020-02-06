function initLiteTooltip(){
	$('.litetooltip-hotspot-wrapper .hotspot').each(function () {
		$(this).LiteTooltip({
			title: $(this).find('.data-container').html()
		});
	});
}

function showAllContinents(){
	$('.continent .node-title').addClass('active'); // Highlight text

	// Hide non-continents
	$('.hotspot:not(.continent):not(.ocean)').css({'opacity': 0});
}

function hideAllContinents(){
	$('.continent .node-title').removeClass('active');

	$('.hotspot:not(.continent):not(.ocean)').css({'opacity': 1});
}

function initCompass(){
	$('#hotspot_compass')
		.mouseenter(function() {
			showAllContinents();
		})
		.mouseleave(function() {
			hideAllContinents();
		});
}

function initMapOverlays(){
	// Show overlay image
	$('[id*="hotspot_"]')
		.mouseenter(function() {
			$("."+$(this)[0]['id']+"__background").addClass('show');
		})
		.mouseleave(function() {
			$("."+$(this)[0]['id']+"__background").removeClass('show');
		});
}

$(document).ready(function(){
	initLiteTooltip();
	initMapOverlays();
	initCompass();
});
