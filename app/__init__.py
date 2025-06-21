# app/__init__.py

from flask import Flask
from app.config import Config
from app.extensions import db, migrate

from app import models  # pastikan model terbaca oleh Flask-Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.views.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app

