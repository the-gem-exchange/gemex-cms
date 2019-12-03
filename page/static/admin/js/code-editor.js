function initCodeEditor(){
	$('.code-editor textarea').each(function(idx, el){
		CodeMirror.fromTextArea(el, {
			tabSize:        4,
			indentWithTabs: true,
			lineNumbers:    true,
			theme:          'dracula',
			mode:           'htmlmixed'
		});
	});
}
