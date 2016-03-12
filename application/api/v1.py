from flask import Blueprint, request
from flask_restful import Resource, Api, abort, fields, marshal

from nthu_library import NTHULibrary
from application.models import Sheet, Circulation

api_v1_bp = Blueprint('api_v1', __name__)
api_v1 = Api(api_v1_bp)
API_VERSION_V1 = 'v1'


route_func, resource_fields, circulation_fields = {
    'space': NTHULibrary.get_available_space,
    'lost': NTHULibrary.get_lost,
    'new': NTHULibrary.get_newest_books,
}, {
    'year': fields.Integer,
    'url': fields.String,
    'department': fields.String,
    'subject': fields.String,
    'examtype': fields.String
}, {
    'type': fields.String,
    'bookname': fields.String,
    'url': fields.String,
    'tag': fields.String,
    'year': fields.Integer,
    'rank': fields.Integer,
    'count': fields.Integer,
}


def clean_param(params):
    return params.to_dict()


def make_job(service_id, param):
    param = clean_param(param) if param else None
    return route_func[service_id](**param) if param \
        else route_func[service_id]()


def query_from_db(service_id):
    return marshal(Sheet.query.all(), resource_fields) \
        if service_id == 'questions' \
        else marshal(Circulation.query.all(), circulation_fields)


class Library(Resource):

    def get(self, service_id):
        if service_id in ['space', 'lost', 'new']:
            return make_job(service_id, request.args)
        if service_id in ['questions', 'top']:
            return query_from_db(service_id)
        abort(404, message="Data {} doesn't exist".format(service_id))


api_v1.add_resource(Library, '/<string:service_id>')
