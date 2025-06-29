# app/__init__.py

from flask import Flask
from app.config import Config
from app.extensions import db, migrate

from app import models  # pastikan model terbaca oleh Flask-Migrate
from app.models import User

# from flask_login import LoginManager
from app.extensions import db, login_manager


# login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)  # inisiasi login manager
    login_manager.login_view = "auth.login"  # supaya redirect ke /login saat belum login
    

    # registrasi blueprint auth.py
    from app.views.auth import auth_bp
    app.register_blueprint(auth_bp)

    # activities.py
    from app.views.activities import activities_bp
    app.register_blueprint(activities_bp)

    # dashboard.py
    from app.views.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp)

    # home.py
    from app.views.home import home_bp  # pastikan import ini ada
    app.register_blueprint(home_bp)

    return app


from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

