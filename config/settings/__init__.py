# Import dev or prod settings based on environment
import os

from .base import *

env = os.environ.get("DEPLOYMENT_ENV", "development")

if env == "production":
    from .prod import *
else:
    from .dev import *
