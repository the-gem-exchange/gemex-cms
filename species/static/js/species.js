function showSubspecies(parent){
	$('.expand-subspecies').each(function(){
		if(this == parent){
			$(parent).closest('.species-item').addClass('open');
			$(parent).next('.subspecies-list').removeClass('closed');
		}
		else{
			hideSubspecies(this);
		}
	});
}

function hideSubspecies(parent){
	$(parent).closest('.species-item').removeClass('open');
	$(parent).next('.subspecies-list').addClass('closed');
}

$(document).ready(function(){
	$('.expand-subspecies').on('click', function(e){
		e.preventDefault();
		if($(this).closest('.species-item').hasClass('open')){
			hideSubspecies(this);
		}
		else{
			showSubspecies(this);
		}
	})
})
