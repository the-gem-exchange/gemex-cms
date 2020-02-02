

$(document).ready(function(){
	$('.litetooltip-hotspot-wrapper .hotspot').each(function () {
		$(this).LiteTooltip({
			title: $(this).find('.data-container').html()
		});
	});
});
