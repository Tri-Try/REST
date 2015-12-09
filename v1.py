import json

from flask import Blueprint
from flask_restful import Resource, Api, abort

from nthu_library import NTHULibrary

api_v1_bp = Blueprint('api_v1', __name__)
API_VERSION_V1 = 'v1'

api_v1 = Api(api_v1_bp)

library_files = ['lost', 'new', 'personal', 'questions', 'space', 'top']


def init_load(name):
    with open('%s-library-data.json' % name, encoding='utf8') as f:
        return json.load(f, encoding='utf8')

library_resources = {
    name: init_load(name)
    for name in library_files
}


def make_job(service_id):
    return NTHULibrary.get_available_space()


def abort_if_doesnt_exist(service_id):
    if service_id not in library_resources:
        abort(404, message="Data {} doesn't exist".format(service_id))


class Library(Resource):
    def get(self, service_id):
        abort_if_doesnt_exist(service_id)
        if service_id in ['space']:
            return make_job(service_id)
        return library_resources[service_id]


api_v1.add_resource(Library, '/<string:service_id>')
