// Show a modal with all information about the selected trait
function showTraitDetails(trait){
	Swal.fire({
		html:`
			<img src="${trait.image}"/>
			<h2 class="swal2-title" id="swal2-title">${trait.description}</h2>
			<span>${trait.rarity} ${trait.sex} ${trait.type}</span>
			<br/>
			<span>${trait.species}</span>
			<br/>
		`,
		customClass:"swal2-trait "+trait.rarity.toLowerCase(),
		focusConfirm: false,
		onClose: function(modal){
			modal.classList.add("fadeOutUp");
		}
	});
}

$('.trait *:not(.trait-select):not(.trait-select *)').on('click', function(){
	let trait = $(this).closest('.trait');
	let rarity = trait.data('rarity');
		rarity = rarity.charAt(0).toUpperCase() + rarity.slice(1);

	let sex = trait.data('sex');
	switch(sex){
		case 'm':
			sex = 'Masculine'
			break;
		case 'f':
			sex = 'Feminine'
			break;
		case 'x':
		default:
			sex = 'Unisex'
			break;
	}

	showTraitDetails({
		name:        trait.data('name'),
		species:     trait.data('species'),
		type:        trait.data('type'),
		sex:         sex,
		rarity:      rarity,
		image:       trait.find('.trait-img > img').attr('src'),
		description: trait.find('.trait-description')[0].innerHTML
	});
});

$('#selected-only').on('click', function(){
	if($('#selected-only').is(':checked')){
		$('.trait-container .selected:not(:checked)').closest('.trait-container').hide();
	}
	else{
		$('.trait-container .selected:not(:checked)').closest('.trait-container').show();
		$('.filter-traits').trigger('keyup'); // Re-apply filters in the search bar
	}
})

$('.trait .selected').on('click', function(){
	if($('#selected-only').is(':checked')){
		if($(this).is(':checked')){
			$(this).closest('.trait-container').show()
		}
		else{
			$(this).closest('.trait-container').hide()
		}
	}
})


function fadeInImages(){
	$('.species-thumbnail').each(function(){
		$(this).imagesLoaded(function(){
			$($(this)[0].elements[0]).addClass('show');
		});
	});

	$('.background').each(function(){
		$(this).imagesLoaded(function(){
			$($(this)[0].elements[0]).addClass('show');
		});
	});
}

$(document).ready(function(){
	fadeInImages();

	// Init live search bar
	$('.traits').liveFilter(
		'.filter-traits',
		'.trait-container', {
			filterChildSelector:'.search-string',
			after:function(){
				if($('#selected-only').is(':checked')){
					$('.trait-container .selected:not(:checked)').closest('.trait-container').hide();
				}
			}
		}
	);
})
