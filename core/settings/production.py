from .base import BASE_DIR, INSTALLED_APPS, MIDDLEWARE, TEMPLATES

# Production settings
DEBUG = False

# Replace 'yourusername' with your actual PythonAnywhere username
ALLOWED_HOSTS = ["shaymk.pythonanywhere.com"]

# Security settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Database configuration for production (SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static and media files
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"
