function getSpeciesItemHeight(element){
	let subspecies_count = $(element).next('.subspecies-list').find('.subspecies-item').length;

	if(window.innerWidth < 460 && subspecies_count > 1){
		return 320 + (subspecies_count * 280);
	}
	else if(window.innerWidth < 690 && subspecies_count > 2){
		return 880;
	}
	else if(window.innerWidth < 905 && subspecies_count > 3){
		return 880;
	}
	else{
		return 600;
	}
}

function resizeSpeciesItem(){
	$('.expand-subspecies').each(function(){
		if(!$(this).next('.subspecies-list').hasClass('closed')){
			let container_height = getSpeciesItemHeight(this);
			$(this).closest('.species-item').css({'height':container_height});
		}
	});
}

function showSubspecies(parent){
	$('.expand-subspecies').each(function(){
		if(this == parent && $(this).next('.subspecies-list').hasClass('closed')){
			let container_height = getSpeciesItemHeight(this);
			$(this).closest('.species-item').css({'height':container_height});
			$(this).next('.subspecies-list').removeClass('closed');
		}
		else{
			hideSubspecies(this);
		}
	});
}

function hideSubspecies(parent){
	$(parent).closest('.species-item').css({'height':200});
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
	});

	$(window).resize(function(){
		resizeSpeciesItem();
	})
})
