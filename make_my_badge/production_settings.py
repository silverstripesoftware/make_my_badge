# Development settings 

from common_settings import *
from bundle_config import config

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os

MEDIA_ROOT = os.path.join(config["core"]["data_directory"], "media")
STATIC_ROOT = os.path.join(config["core"]["data_directory"], "static")
