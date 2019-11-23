const isFirefox = navigator.userAgent.toLowerCase().indexOf('firefox') > -1;

$(document).ready(function(){
	// Prevents FA from converting <i> tags to <svg> and breaking CSS
	window.FontAwesomeConfig = { autoReplaceSvg: false }
})
