import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # STRAVA (OAUTH)
    SECRET_KEY = os.getenv('SECRET_KEY')
    STRAVA_CLIENT_ID = os.getenv('STRAVA_CLIENT_ID')
    STRAVA_CLIENT_SECRET = os.getenv('STRAVA_CLIENT_SECRET')
    STRAVA_REDIRECT_URI = os.getenv('STRAVA_REDIRECT_URI')
    