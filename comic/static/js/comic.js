function bindArrowKeys(){
	$(document).on('keydown.tabs', function(e){
		const arrow_left  = 37;
		const arrow_right = 39;
		const keyCode     = e.keyCode;

		if(keyCode == arrow_left){
			e.preventDefault();
			if($('.previous-page').length){
				$(".previous-page")[0].click();
			}
		}
		if(keyCode == arrow_right){
			e.preventDefault();
			if($('.next-page').length){
				$(".next-page")[0].click();
			}
		}
	})
}

$(document).ready(function(){
	bindArrowKeys();
})
