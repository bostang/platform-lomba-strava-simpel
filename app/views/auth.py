from flask import Blueprint, redirect, request, session, url_for, render_template
from stravalib.client import Client
import os

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def login_page():
    return render_template('login.html')

@auth_bp.route('/login')
def login():
    client = Client()
    redirect_uri = os.getenv('STRAVA_REDIRECT_URI')
    auth_url = client.authorization_url(
        client_id=os.getenv('STRAVA_CLIENT_ID'),
        redirect_uri=redirect_uri,
        scope=['read', 'activity:read']
    )
    return redirect(auth_url)

@auth_bp.route('/authorize')
def authorize():
    code = request.args.get('code')
    if not code:
        return "Authorization failed", 400

    client = Client()
    token_response = client.exchange_code_for_token(
        client_id=os.getenv('STRAVA_CLIENT_ID'),
        client_secret=os.getenv('STRAVA_CLIENT_SECRET'),
        code=code
    )

    session['access_token'] = token_response['access_token']
    athlete = client.get_athlete()
    return f"Login berhasil! Halo, {athlete.firstname} {athlete.lastname} (Strava ID: {athlete.id})"
