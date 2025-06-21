# app/views/activities.py

from app.extensions import db
from app.models import User, Activity

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from stravalib.client import Client

from datetime import datetime
from app.models import Activity, db
import uuid


activities_bp = Blueprint('activities', __name__)

# submit semua activity secara langsung
@activities_bp.route('/fetch-activities')
@login_required
def fetch_activities():
    client = Client(access_token=current_user.access_token)
    activities = client.get_activities(limit=10)

    saved = 0
    for act in activities:
        if Activity.query.filter_by(strava_id=act.id).first():
            continue

        activity = Activity(
            strava_id=act.id,
            user_id=current_user.id,
            name=act.name,
            distance=float(act.distance),
            moving_time=int(act.moving_time),
            elapsed_time=int(act.elapsed_time),
            type=str(act.type).split("=")[1].strip("'"),
            start_date=act.start_date,
        )
        db.session.add(activity)
        saved += 1

    db.session.commit()
    return f"{saved} aktivitas berhasil disimpan."

@activities_bp.route('/choose-activities', methods=['GET'])
@login_required
def choose_activities():
    client = Client()
    client.access_token = current_user.access_token

    activities = list(client.get_activities(limit=10))

    # Ambil semua strava_id aktivitas yang sudah disimpan oleh user
    saved_activities = Activity.query.with_entities(Activity.strava_id).filter_by(user_id=current_user.id).all()
    saved_ids = set(str(a.strava_id) for a in saved_activities)

    return render_template('choose_activities.html', activities=activities, saved_ids=saved_ids)

@activities_bp.route('/submit-activity', methods=['POST'])
@login_required
def submit_activity():
    strava_id = request.form['strava_id']

    client = Client()
    client.access_token = current_user.access_token

    act = client.get_activity(strava_id)

    # Cek kalau sudah pernah ada
    if Activity.query.filter_by(strava_id=act.id).first():
        flash('Aktivitas ini sudah disubmit sebelumnya.')
        return redirect(url_for('activities.choose_activities'))

    activity = Activity(
            strava_id=act.id,
            user_id=current_user.id,
            name=act.name,
            distance=float(act.distance),
            moving_time=int(act.moving_time),
            elapsed_time=int(act.elapsed_time),
            type=str(act.type).split("=")[1].strip("'"),
            start_date=act.start_date,
        )

    db.session.add(activity)
    db.session.commit()
    flash('Aktivitas berhasil disubmit.')
    return redirect(url_for('activities.choose_activities'))

@activities_bp.route('/my-activities')
@login_required
def my_activities():
    user_activities = Activity.query.filter_by(user_id=current_user.id).order_by(Activity.start_date.desc()).all()
    return render_template('my_activities.html', activities=user_activities)
