import os

# Test if running in google cloud
if os.getenv('GAE_APPLICATION', None):
    from .production_gcp import *
else:
    from .local_settings_loader import *
