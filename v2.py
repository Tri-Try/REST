import json

from flask import Blueprint
from flask.ext import restful
from flask.ext.restful import abort, fields, marshal_with, reqparse

from nthu_library import NTHULibrary
from models import Sheet, Department, Examtype

API_VERSION_V2 = 'v2'

api_v2_bp = Blueprint('api_v2', __name__)
api_v2 = restful.Api(api_v2_bp)


resource_fields = {
    'year': fields.Integer,
    'url': fields.String,
    'department': fields.String,
    'subject': fields.String,
    'examtype': fields.String
}


class SheetResource(restful.Resource):


    @marshal_with(resource_fields, envelope='result')
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('year', type=int)
        parser.add_argument('department')
        parser.add_argument('examtype')

        args = parser.parse_args()

        q = Sheet.query
        if args.get('year'):
            q = q.filter_by(year=args.get('year'))
        if args.get('department'):
            q = q.join(Department).filter_by(name=args.get('department'))
        if args.get('examtype'):
            q = q.join(Examtype).filter_by(name=args.get('examtype'))

        return q.all()


api_v2.add_resource(SheetResource, '/sheets', endpoint='sheets')
