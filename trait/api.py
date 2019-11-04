from wagtail.api.v2.endpoints import BaseAPIEndpoint

from trait.models import Trait

class TraitsAPIEndpoint(BaseAPIEndpoint):
	model = Trait
