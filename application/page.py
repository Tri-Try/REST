from flask import render_template, send_file
from flask.blueprints import Blueprint

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
