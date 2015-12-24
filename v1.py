import json

from flask import Blueprint, request
from flask_restful import Resource, Api, abort, fields, marshal_with

from nthu_library import NTHULibrary
from models import Sheet

api_v1_bp = Blueprint('api_v1', __name__)
API_VERSION_V1 = 'v1'

api_v1 = Api(api_v1_bp)

library_files = ['new', 'top']


def init_load(name):
    with open('%s-library-data.json' % name, encoding='utf8') as f:
        return json.load(f, encoding='utf8')

library_resources = {
    name: init_load(name)
    for name in library_files
}


route_func = {
    'space': NTHULibrary.get_available_space,
    'lost': NTHULibrary.get_lost,
}


resource_fields = {
    'year': fields.Integer,
    'url': fields.String,
    'department': fields.String,
    'subject': fields.String,
    'examtype': fields.String
}


def clean_param(params):
    # TODO
    return params


def make_job(service_id, param):
    param = clean_param(param) if param else None
    return route_func[service_id](**param) if param \
        else route_func[service_id]()


@marshal_with(resource_fields, envelope='result')
def query_from_db(service_id):
    return Sheet.query.all()


def abort_if_doesnt_exist(service_id):
    if service_id not in library_resources:
        abort(404, message="Data {} doesn't exist".format(service_id))


class Library(Resource):

    def get(self, service_id):
        if service_id in ['space', 'lost']:
            return make_job(service_id, request.args)
        if service_id in ['questions']:
            return query_from_db(service_id)
        abort_if_doesnt_exist(service_id)
        return library_resources[service_id]


api_v1.add_resource(Library, '/<string:service_id>')
