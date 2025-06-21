from app.extensions import db
from app.models import User

from datetime import datetime

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

    access_token = token_response['access_token']
    refresh_token = token_response['refresh_token']
    expires_at = datetime.fromtimestamp(token_response['expires_at'])

    client.access_token = access_token
    athlete = client.get_athlete()

    # Cek apakah user sudah ada
    user = User.query.filter_by(strava_id=athlete.id).first()

    if user:
        # Update token
        user.access_token = access_token
        user.refresh_token = refresh_token
        user.token_expires_at = expires_at
    else:
        # Buat user baru
        user = User(
            strava_id=athlete.id,
            username=athlete.username,
            full_name=f"{athlete.firstname} {athlete.lastname}",
            access_token=access_token,
            refresh_token=refresh_token,
            token_expires_at=expires_at,
        )
        db.session.add(user)

    db.session.commit()

    session['user_id'] = user.id
    return f"Login berhasil! Halo, {user.full_name} (ID lokal: {user.id})"


# @auth_bp.route('/authorize')
# def authorize():
#     code = request.args.get('code')
#     if not code:
#         return "Authorization failed", 400

#     client = Client()
#     token_response = client.exchange_code_for_token(
#         client_id=os.getenv('STRAVA_CLIENT_ID'),
#         client_secret=os.getenv('STRAVA_CLIENT_SECRET'),
#         code=code
#     )

#     session['access_token'] = token_response['access_token']
#     athlete = client.get_athlete()
#     return f"Login berhasil! Halo, {athlete.firstname} {athlete.lastname} (Strava ID: {athlete.id})"
