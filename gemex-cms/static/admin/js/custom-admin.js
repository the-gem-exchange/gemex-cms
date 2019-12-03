/**
 * Converts a string from "123456" to "#123456" if it's missing a "#"
 */
function convertToHex(str){
	if(str[0] == "#") return str
	else return "#"+str
}

/**
 * Works on any FieldPanel with classname "use-colorpicker" set
 * Initializes a spectrum colorpicker, helps sanitize input, and tweaks the DOM to make it fit in our admin theme
 */
function initColorpickers(){
	let colorpicker_inputs = $('.use-colorpicker input');

	// Init Spectrum Colorpicker
	// See more config options here: http://bgrins.github.io/spectrum/
	colorpicker_inputs.spectrum({
		preferredFormat: "hex",
		showInput: true,
	});

	// Live update the chooser preview when hex value is manually typed
	// Wait a moment with setTimeout so the user doesn't feel like they are fighting the input
	colorpicker_inputs.on('input',function(e) {
		let this_input      = $(this);
		let input_container = this_input.closest('li');
		let error_message   = '<p class="error-message"><span>Invalid HEX code.</span></p>';
		setTimeout(function(){
			let hex_string   = convertToHex(e.target.value);
			let is_hex_value = /^#([0-9a-f]{6}|[0-9a-f]{3})$/i.test(hex_string);

			if(!is_hex_value && hex_string.length > 1){
				input_container.addClass('error');
				if(input_container.has('.error-message').length == 0){
					input_container.append(error_message);
				}
			}
			// String is valid HEX and is the proper length (ie #000 or #000000)
			// Remove errors, update colorpicker value
			else if(is_hex_value) {
				this_input.spectrum("set", hex_string); // This is what updates the colorpicker
				input_container.removeClass('error');
				input_container.children('.error-message').remove();
			}
			// Remove errors if empty
			else if(hex_string.length <= 1){
				input_container.removeClass('error');
				input_container.children('.error-message').remove();
			}
		},1000)
	});

	// Show Input Text Box
	colorpicker_inputs.show();

	// Add/remove a helper class on input focus to style the picker
	colorpicker_inputs.on('focus', function(){
		$(this).siblings('.sp-replacer').addClass('focused');
	});
	colorpicker_inputs.on('blur', function(){
		$(this).siblings('.sp-replacer').removeClass('focused');
	});
}

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
	$('.c-sf-button, [id*="-ADD"]').on('click', function(){
		setTimeout(function(){
			initAdmin();
		}, 300);
	});
}

function initAdmin(){
	initColorpickers();
	initColumnSettings();
	listenForChanges();
	initCodeEditor();
}

$(document).ready(function(){
	initAdmin();
});
