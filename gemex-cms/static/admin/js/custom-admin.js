function initColumnSettings(){
	$('.column-options .struct-block').each(function(){
		var settingsContainer  = $(this)[0].closest('.c-sf-block');
		var streamBlockActions = $(settingsContainer).closest('.c-sf-block').find('.c-sf-block__actions');

		if(streamBlockActions.find('.column-settings-button').length == 0){
			var settingsButton = document.createElement('button');
				settingsButton.innerHTML = '<i class="icon icon-cog"></i>';
				settingsButton.title = "Settings";
				settingsButton.classList.add('column-settings-button','c-sf-block__actions__single');

			streamBlockActions.append(settingsButton);

			$(settingsButton).on('click', function(e){
				e.preventDefault();
				$(settingsContainer).find('.struct-block').toggleClass('show');
			});
		}
	});
}

function listenForChanges(){
	$('.c-sf-button').on('click', function(){
		setTimeout(function(){
			initAdmin();
		}, 300);
	});
}

function initAdmin(){
	initColumnSettings();
	listenForChanges();
}

$(document).ready(function(){
	initAdmin();
});
