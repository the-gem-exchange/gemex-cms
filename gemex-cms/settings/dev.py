from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# AWS Settings
# AWS_STORAGE_BUCKET_NAME = 'static.thegemexchange.net'
# AWS_S3_REGION_NAME = 'us-east-1'
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = False
# AWS_HEADERS = {
#     'Access-Control-Allow-Origin': '*'
# }

# Media Storage
MEDIAFILES_LOCATION = 'media'
# MEDIA_URL = "https://s3-{}.amazonaws.com/{}/{}/".format(AWS_S3_REGION_NAME, AWS_STORAGE_BUCKET_NAME, MEDIAFILES_LOCATION)
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

try:
    from .local import *
except ImportError:
    pass
