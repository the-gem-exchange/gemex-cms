function fadeInImages(){
	$('#parallax-background').imagesLoaded(function(){
			$('#parallax-background').addClass('show');
	});
}

function fadeInLogo(){
	fontsLoaded(['Verbena'], function() {
		$('#homepage-title').addClass('show');
	});
}

$(document).ready(function(){
	fadeInImages();
	fadeInLogo();
});
