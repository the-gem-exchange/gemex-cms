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

$('.trait').on('click', function(){
	let rarity = $(this).data('rarity');
		rarity = rarity.charAt(0).toUpperCase() + rarity.slice(1);

	let sex = $(this).data('sex');
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
		name:        $(this).data('name'),
		species:     $(this).data('species'),
		type:        $(this).data('type'),
		sex:         sex,
		rarity:      rarity,
		image:       $(this).find('img').attr('src'),
		description: $(this).find('.trait-description')[0].innerHTML
	});
});

$(document).ready(function(){
	$('.traits').liveFilter('.filter-traits', '.trait', {filterChildSelector:'.search-string'});
})
