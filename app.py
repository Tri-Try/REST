import os
from application.api_service import create_app
from application.models import db

app = create_app()


def setup_database(app):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':

    if not os.path.isfile('../sqlite3.db'):
        setup_database(app)

    app.run(
        debug=True,
        host=os.environ['IP'],
        port=int(os.environ['PORT'])
    )