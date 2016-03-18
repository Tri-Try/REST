import os
from flask import Flask

from application.page import page_bp
from application.api.v1 import api_v1_bp, API_VERSION_V1
from application.api.v2 import api_v2_bp, API_VERSION_V2
from application.models import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../sqlite3.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    app.register_blueprint(page_bp)

    app.register_blueprint(
        api_v1_bp,
        url_prefix='/{prefix}/{version}'.
        format(prefix='api', version=API_VERSION_V1)
    )
    app.register_blueprint(
        api_v2_bp,
        url_prefix='/{prefix}/{version}'.
        format(prefix='api', version=API_VERSION_V2)
    )

    return app
