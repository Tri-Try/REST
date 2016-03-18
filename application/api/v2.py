from flask import Blueprint
from flask.ext import restful
from flask.ext.restful import abort, fields, marshal_with, reqparse

from nthu_library import NTHULibrary
from application.models import Sheet, Department, Examtype

API_VERSION_V2 = 'v2'

api_v2_bp = Blueprint('api_v2', __name__)
api_v2 = restful.Api(api_v2_bp)




resource_fields = {
    'year': fields.Integer,
    'url': fields.String,
    'department': fields.String(default='無'),
    'subject': fields.String,
    'type': fields.String(attribute='examtype')
}


class SheetResource(restful.Resource):

    @marshal_with(resource_fields, envelope='result')
    def get(self):
        """
        @api {get} /sheets/ Request sheets information
        @apiVersion 2.0.0
        @apiName get_sheet
        @apiGroup Sheet
        @apiDescription Query for sheets by year, department and examtype.

        @apiSampleRequest /api/v2/sheets

        @apiParam {Number} [year]         Specify year.
        @apiParam {String} [department]   Specify department.
        @apiParam {String} [examtype]     Specify examtype.

        @apiSuccess {Number} id         Sheet's ID.
        @apiSuccess {Number} year       Year.
        @apiSuccess {String} department Department.
        @apiSuccess {String} subject    Subject.
        @apiSuccess {String} examtype   Exam type.

        @apiParamExample {json} Request-Example:
                 { "year": 102, "department": "物理系" }
        @apiSuccessExample {json} Success-Response:
                 HTTP/1.1 200 OK
                 {
                    "result": [
                    {
                        "department": "'物理系'",
                        "subject": "'近代物理'",
                        "type": "'after-graduate-exams'",
                        "url": "http://www.lib.nthu.edu.tw/library/department/ref/exam/p/phys/101/2003.pdf",
                        "year": 101
                    },
                    ...
                    ]
                 }
        """
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
