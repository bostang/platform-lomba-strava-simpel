# app/views/dashboard.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Activity, User
from app.extensions import db
from sqlalchemy import func
from datetime import datetime

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    # Ringkasan aktivitas berdasarkan tipe
    summary = db.session.query(
        Activity.type,
        func.sum(Activity.distance).label("total_distance"),
        func.sum(Activity.moving_time).label("total_time"),
        func.count().label("activity_count")
    ).filter(Activity.user_id == current_user.id).group_by(Activity.type).all()

    # Progress bulanan
    now = datetime.utcnow()
    progress_query = db.session.query(func.sum(Activity.distance)).filter(
        Activity.user_id == current_user.id,
        func.extract('month', Activity.start_date) == now.month,
        func.extract('year', Activity.start_date) == now.year
    ).scalar()
    progress_km = round((progress_query or 0) / 1000, 2)
    monthly_target_km = 100

    # Leaderboard (top 5)
    leaderboard = db.session.query(
        User.full_name,
        func.sum(Activity.distance).label("total_distance")
    ).join(Activity).group_by(User.id).order_by(func.sum(Activity.distance).desc()).limit(5).all()

    return render_template("dashboard.html",
        summary=summary,
        progress_km=progress_km,
        monthly_target_km=monthly_target_km,
        leaderboard=leaderboard
    )
