from flask import render_template
from flask.blueprints import Blueprint

from nthu_library import NTHULibrary

page_bp = Blueprint('page', __name__)


@page_bp.route("/")
def index_service():
    return render_template('index.html')


@page_bp.route("/hi")
def hello_service():
    return 'hello'


@page_bp.route("/update_sheets")
def crawl_sheets_service():
    lib = NTHULibrary()
    NTHULibrary.get_past_year_questions()
    lib.get_top_circulated_materials(type='loaned')
    lib.get_top_circulated_materials(type='reserved')
    return '抓抓抓抓抓完啦'
