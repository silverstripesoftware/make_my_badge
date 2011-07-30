# Development settings 

from common_settings import *
from bundle_config import config

DEBUG = False
TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = config["core"]["data_directory"]
