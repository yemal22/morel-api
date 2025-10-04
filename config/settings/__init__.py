from .base import *

# Import dev or prod settings based on environment
import os

env = os.environ.get('DEPLOYMENT_ENV', 'development')

if env == 'production':
    from .prod import *
else:
    from .dev import *
