import os
from flask import Flask

from page import page_bp
from v1 import api_v1_bp, API_VERSION_V1
from v2 import api_v2_bp, API_VERSION_V2
from database import db

from flask.ext.restless import APIManager


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
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


def setup_database(app):
    with app.app_context():
        db.create_all()


app = create_app()

if not os.path.isfile('sqlite3.db'):
    setup_database(app)

app.run(
    host=os.environ['IP'],
    port=int(os.environ['PORT'])
)
