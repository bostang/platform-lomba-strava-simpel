# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # STRAVA (OAUTH)
    SECRET_KEY = os.getenv('SECRET_KEY')
    STRAVA_CLIENT_ID = os.getenv('STRAVA_CLIENT_ID')
    STRAVA_CLIENT_SECRET = os.getenv('STRAVA_CLIENT_SECRET')
    STRAVA_REDIRECT_URI = os.getenv('STRAVA_REDIRECT_URI')

    # SQL Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Tambahkan ini
    SQLALCHEMY_TRACK_MODIFICATIONS = False