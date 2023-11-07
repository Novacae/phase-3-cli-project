"""from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'home/aman/Development/code/phase3/phase 3 project 1/expenses'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from . import models
        from .views import bp

        db.create_all()

        app.register_blueprint(bp)

        return app"""