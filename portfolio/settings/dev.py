from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '149nr&xp8c3r7j0*9f*wli8^#9e)jxm9ni9f78csw@5aa!sox9'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['188.166.41.132', 'rafrasenberg.nl', 'www.rafrasenberg.nl']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
