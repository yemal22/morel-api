"""
Production settings for morel-api project.
"""

from .base import *

DEBUG = False

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = "DENY"

# CORS - Strict settings for production
CORS_ALLOW_ALL_ORIGINS = False

# Database connection pooling (optional, requires psycopg2 pool support)
DATABASES["default"]["CONN_MAX_AGE"] = 60

# Logging - more structured for production
LOGGING["handlers"]["file"] = {
    "class": "logging.handlers.RotatingFileHandler",
    "filename": "/var/log/django/morel-api.log",
    "maxBytes": 1024 * 1024 * 10,  # 10 MB
    "backupCount": 10,
    "formatter": "verbose",
}

LOGGING["root"]["handlers"] = ["console", "file"]
LOGGING["loggers"]["django"]["handlers"] = ["console", "file"]
LOGGING["root"]["level"] = "WARNING"
LOGGING["loggers"]["django"]["level"] = "WARNING"

# Email backend for production
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
