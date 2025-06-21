# app/extensions.py
    # Inisialisasi SQLAlchemy & Migrate

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
