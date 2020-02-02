

$(document).ready(function(){
	$('.litetooltip-hotspot-wrapper .hotspot').each(function () {
		$(this).LiteTooltip({
			title: $(this).find('.data-container').html()
		});
	});

	// Show overlay image
	$('[id*="hotspot_"]')
		.mouseenter(function() {
			$("#"+$(this)[0]['id']+"__background").addClass('show');
		})
		.mouseleave(function() {
			$("#"+$(this)[0]['id']+"__background").removeClass('show');
		});
});
