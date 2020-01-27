from .models import BotCommand, get_all_commands

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

def get_command(request, command):
	if command == 'commands':
		return JsonResponse(
			{
				'command': command,
				'text':    get_all_commands()
			},
		)

	else:
		data  = get_object_or_404(BotCommand, command=command)
		image = data.get_image()

		if data.text and image:
				return JsonResponse({
					'command': data.command,
					'text':    data.text,
					'image':   image
				},
				safe=False,
				json_dumps_params={
					'ensure_ascii':False
				}
			)

		elif data.text:
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

		elif image:
			return JsonResponse({
				'command': data.command,
				'image':   image
			})
