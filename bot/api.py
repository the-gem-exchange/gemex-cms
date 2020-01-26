from wagtail.api.v2.endpoints import BaseAPIEndpoint

from bot.models import BotCommand

class BotCommandAPIEndpoint(BaseAPIEndpoint):
	model = BotCommand
