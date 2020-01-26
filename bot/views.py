from .models import BotCommand

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

def get_all_commands():
	commands = BotCommand.objects.order_by('command').all() # All commands in alphabetical order
	reply    = ''

	# Try to get the intro text message from the site, otherwise fall back to a standard intro
	try:
		commands_message = BotCommand.objects.get(command='commands')
		if commands_message:
			reply += commands_message.text + '\\n\\n'
	except:
		reply += 'Available commands for Discord Chan:\\n\\n'

	# Build the list in markdown with newline characters
	for c in commands:
		reply += c._command()+'\\n'

	return reply

def get_command(request, command):
	if command == 'commands':
		return JsonResponse(
			{
				'command': command,
				'text':    get_all_commands()
			},
		)

	else:
		data = get_object_or_404(BotCommand, command=command)

		if data.type =='text' and data.text:
			return JsonResponse(
				{
					'command': data.command,
					'text':    data.text
				},
				safe=False,
				json_dumps_params={
					'ensure_ascii':False
				}
			)

		if data.type == 'image':
			image = data.get_image()
			if image:
				return JsonResponse({
					'command': data.command,
					'image':   image.image.file.url
				})
