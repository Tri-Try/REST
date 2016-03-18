from flask import render_template, send_file
from flask.blueprints import Blueprint

from nthu_library import NTHULibrary
from application.api.v1 import docs as v1_docs

page_bp = Blueprint('page', __name__)


@page_bp.route("/")
def index_service():
    return render_template('index.html', v1_docs=v1_docs)


@page_bp.route("/<path:path>")
def doc_service(path):
    if path == 'doc':
        path = 'index.html'
    return send_file('static/doc/%s' % path)


@page_bp.route("/update_sheets")
def crawl_sheets_service():
    lib = NTHULibrary()
    NTHULibrary.get_past_year_questions()
    lib.get_top_circulated_materials(type='loaned')
    lib.get_top_circulated_materials(type='reserved')
    return '抓抓抓抓抓完啦'


@page_bp.route('/map')
def list_routes():
    import urllib
    output = []
    from flask import url_for,  current_app as app
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

    return '<br>'.join(output)