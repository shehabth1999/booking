import firebase_admin
from firebase_admin import credentials
from core import settings
import os


cred = credentials.Certificate(os.path.join(settings.BASE_DIR,"firebase_config.json"))
firebase_admin.initialize_app(cred, {'storageBucket': 'booking-c4e6b.appspot.com'})

