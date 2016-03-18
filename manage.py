from flask.ext.script import Command, Manager

from application.api_service import create_app
from application.models import db

from nthu_library import NTHULibrary


app = create_app()
manager = Manager(app)


@manager.command
def syncdb():
    with app.app_context():
        db.create_all()


@manager.command
def crawl():
    lib = NTHULibrary()
    NTHULibrary.get_past_year_questions()
    lib.get_top_circulated_materials(type='loaned')
    lib.get_top_circulated_materials(type='reserved')


@manager.command
def routes():
    import urllib
    output = []
    from flask import url_for, current_app as app
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = ("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == "__main__":
    manager.run()
