function initLiteTooltip(){
	$('.litetooltip-hotspot-wrapper .hotspot').each(function () {
		$(this).LiteTooltip({
			title: $(this).find('.data-container').html()
		});
	});
}

function showAllOverlays(){
	$('[id*="__background"]').addClass('show');
	$('.continent .node-title').addClass('active');
}

function hideAllOverlays(){
	$('[id*="__background"]').removeClass('show');
	$('.continent .node-title').removeClass('active');
}

function initCompass(){
	$('#hotspot_compass')
		.mouseenter(function() {
			showAllOverlays();
		})
		.mouseleave(function() {
			hideAllOverlays();
		});
}

function initMapOverlays(){
	// Show overlay image
	$('[id*="hotspot_"]')
		.mouseenter(function() {
			$("#"+$(this)[0]['id']+"__background").addClass('show');
		})
		.mouseleave(function() {
			$("#"+$(this)[0]['id']+"__background").removeClass('show');
		});
}

$(document).ready(function(){
	initLiteTooltip();
	initMapOverlays();
	initCompass();
});
