# app/models.py
    # Definisi ORM tabel

import uuid
from datetime import datetime
from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    strava_id = db.Column(db.BigInteger, unique=True, nullable=False)
    username = db.Column(db.String)
    full_name = db.Column(db.String)
    access_token = db.Column(db.Text, nullable=False)
    refresh_token = db.Column(db.Text, nullable=False)
    token_expires_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
