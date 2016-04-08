from flask import Blueprint
from flask.ext import restful
from flask.ext.restful import fields, abort, marshal_with, reqparse

from application.models import Sheet, Department, Examtype, Circulation

API_VERSION_V2 = 'v2'

api_v2_bp = Blueprint('api_v2', __name__)
api_v2 = restful.Api(api_v2_bp)


sheet_resource_fields, topbooks_resource_fields = {
    'id': fields.Integer,
    'year': fields.Integer,
    'url': fields.String,
    'department': fields.String(default='無'),
    'subject': fields.String,
    'type': fields.String(attribute='examtype')
}, {
    'type': fields.String,
    'bookname': fields.String,
    'url': fields.String,
    'rank': fields.Integer,
    'tag': fields.String,
    'year': fields.Integer,
    'count': fields.Integer
}


class SheetItem(restful.Resource):

    @marshal_with(sheet_resource_fields, envelope='result')
    def get(self, sheet_id):
        """
        @api {get} /v2/sheets/:id Fetch specific sheet data
        @apiVersion 2.0.0
        @apiName get_sheet
        @apiGroup ExamPaper
        @apiPermission public
        @apiDescription Get the information of year, department or examtype
            about specific sheet.

        @apiSampleRequest http://tritry.cs.nthu.edu.tw/api/v2/sheets/:sheet_id
        @apiExample {curl} Example usage:
            curl -i http://tritry.cs.nthu.edu.tw/api/v2/sheets/1025

        @apiError message
            The message for <code>sheet_id</code> which was not found.
        @apiErrorExample {json} Error-Response:
                HTTP 404 Not Found
                {
                    "message": "Sheet #5566 doesn't exist"
                }
        @apiSuccess {Number} id         Sheet's ID.
        @apiSuccess {Number} year       Year of the sheet.
        @apiSuccess {String} department Department of the sheet.
        @apiSuccess {String} subject    Subject.
        @apiSuccess {String} examtype   Exam type.
        @apiSuccessExample {json} Success-Response:
                 HTTP 200 OK
                 {
                    "result": {
                        "department": "'物理系'",
                        "subject": "'應用數學'",
                        "type": "'after-graduate-exams'",
                        "url": "http://www.lib.nthu.edu.tw/library/department/ref/exam/p/phys/86/860403.pdf",
                        "year": 86
                    }
                 }
        """
        sheet = Sheet.query.get(sheet_id)
        if sheet is None:
            abort(404, message="Sheet #{} doesn't exist".format(sheet_id))
        return sheet


class SheetList(restful.Resource):

    def _query(self, args):
        q = Sheet.query
        if args.get('year'):
            q = q.filter_by(year=args.get('year'))
        if args.get('department'):
            q = q.join(Department).filter_by(name=args.get('department'))
        if args.get('examtype'):
            q = q.join(Examtype).filter_by(name=args.get('examtype'))
        return q.all()

    @marshal_with(sheet_resource_fields, envelope='result')
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('year', type=int)
        parser.add_argument('department')
        parser.add_argument('examtype')

        args = parser.parse_args()
        return self._query(args)


class SheetListForAPI(SheetList):

    @marshal_with(sheet_resource_fields, envelope='result')
    def get(self):
        """
        @api {get} /v2/sheets/ Query on sheets information
        @apiVersion 2.0.0
        @apiName query_sheets
        @apiGroup ExamPaper
        @apiPermission public
        @apiDescription Search for sheets by year, department or examtype.

        @apiSampleRequest http://tritry.cs.nthu.edu.tw/api/v2/test/sheets
        @apiExample {curl} Example usage:
            curl -i "http://tritry.cs.nthu.edu.tw/api/v2/sheets?year=102&department=物理系"

        @apiParam {Number{84-*}} [year]         Specify year. (民國紀年)
        @apiParam {String} [department]   Specify department.
        @apiParam {String="after-graduate-exams", "transfer-exams"} [examtype]
            Specify examtype.

        @apiSuccess {Number} id               Sheet's ID.
        @apiSuccess {Number} year             Year of the sheet.
        @apiSuccess {String} department       Department of the sheet.
        @apiSuccess {String} subject          Subject.
        @apiSuccess {String} examtype         Exam type.

        @apiParamExample {json} Request-Example:
                 { "year": 102, "department": "物理系", "type": "after-graduate-exams" }
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
        ''' No need to check the type for testing '''
        ''' `apidoc` will request with empty parameters, like `?year=&...` '''
        parser.add_argument('year')
        parser.add_argument('department')
        parser.add_argument('examtype')

        args = parser.parse_args()
        return self._query(args)


class Topbook(restful.Resource):

    @marshal_with(topbooks_resource_fields, envelope='result')
    def get(self, book_id):
        """
        @api {get} /v2/topbooks Get the single book info
        @apiVersion 2.0.0
        @apiName get_top_book
        @apiGroup Librarybooks
        @apiPermission public
        @apiDescription Get the single book information recorded in rank list

        @apiSampleRequest http://tritry.cs.nthu.edu.tw/api/v2/topbooks/:id
        @apiExample {curl} Example usage:
            curl -i "http://tritry.cs.nthu.edu.tw/api/v2/topbooks/6666"

        @apiSuccess {Number} id               Book's ID.
        @apiSuccess {Number} year             Year of the rank list.
        @apiSuccess {String} bookname         Bookname.
        @apiSuccess {Number} rank             Rank in that year.
        @apiSuccess {String} tag              Name of rank list.
        @apiSuccess {String} type             Type of rank list.
        @apiSuccess {String} URL              URL of book in the library circulation system.

        @apiSuccessExample {json} Success-Response:
                {
                "result": {
                    "bookname": "如何使基金報酬最大化",
                    "count": 20,
                    "rank": 127,
                    "tag": "中文圖書借閱排行榜",
                    "type": "loaned",
                    "url": "http://webpac.lib.nthu.edu.tw/F?func=find-c&ccl_term=OYS%3D0719217&T=2&ty=ie",
                    "year": 2007
                }
            }
        """
        book = Circulation.query.get(book_id)
        if book is None:
            abort(404, message="Book #{} doesn't exist".format(book_id))
        return book


class TopbooksList(restful.Resource):

    def _query(self, args):
        q = Circulation.query
        if args.get('year'):
            q = q.filter_by(year=args.get('year'))
        if args.get('type'):
            q = q.filter_by(type=args.get('type'))
        if args.get('rank'):
            q = q.filter_by(rank=args.get('rank'))
        if args.get('count'):
            q = q.filter(Circulation.count >= args.get('count'))
        if args.get('tag'):
            q = q.filter_by(tag=args.get('tag'))
        if args.get('bookname'):
            q = q.filter_by(bookname=args.get('bookname'))
        return q.all()

    @marshal_with(topbooks_resource_fields, envelope='result')
    def get(self):
        """
        @api {get} /v2/topbooks Query top books info in library
        @apiVersion 2.0.0
        @apiName query_top_books
        @apiGroup Librarybooks
        @apiPermission public
        @apiDescription Query top books information in library.

        @apiSampleRequest http://tritry.cs.nthu.edu.tw/api/v2/topbooks
        @apiParam {Number{2003-*}} [year]    Specify year.
        @apiParam {String="loaned", "reserved"} [type="loaned"]
            Specify type of circulations.
        @apiParam {Number} [rank]           Specify rank.
        @apiParam {Number} [count]          Specify circulations to filter out results that greater than this value.
        @apiParam {String} [tag]
            Specify tag.
            <ul>
                <li><code>中文圖書借閱排行榜</code></li>
                <li><code>中文圖書預約排行榜</code></li>
                <li><code>中文小說圖書借閱排行榜</code></li>
                <li><code>中文小說圖書預約排行榜</code></li>
                <li><code>英文小說圖書借閱排行榜</code></li>
                <li><code>西文圖書借閱排行榜</code></li>
                <li><code>西文圖書預約排行榜</code></li>
                <li><code>西文小說圖書借閱排行榜</code></li>
                <li><code>視聽資料DVD電影片借閱排行榜</code></li>
                <li><code>視聽資料DVD電影片預約排行榜</code></li>
                <li><code>視聽資料借閱排行榜(不含DVD電影片)</code></li>
                <li><code>視聽資料借閱排行榜(不含電影、卡通)</code></li>
                <li><code>視聽資料電影、卡通借閱排行榜</code></li>
                <li><code>視聽資料電影、卡通預約排行榜</code></li>
                <li><code>視聽資料預約排行榜(不含DVD電影片)</code></li>
                <li><code>視聽資料預約排行榜(不含電影、卡通)</code></li>
            </ul>
        @apiParam {String} [bookname]       Specify bookname.

        @apiParamExample {json} Request-Example:
                 { "year": 102, "type": "reserved", "count": 100 }
        @apiExample {curl} Example usage:
            curl -i "http://tritry.cs.nthu.edu.tw/api/v2/topbooks?year=2012&type=reserved&count=100"

        @apiSuccess {Number} id               Book's ID.
        @apiSuccess {Number} year             Year of the rank list.
        @apiSuccess {String} bookname         Bookname.
        @apiSuccess {Number} rank             Rank in that year.
        @apiSuccess {String} tag              Name of rank list.
        @apiSuccess {String} type             Type of rank list.
        @apiSuccess {String} URL              URL of book in the library circulation system.

        @apiSuccessExample {json} Success-Response:
                {
                    "result": [
                        {
                            "bookname": "飢餓遊戲",
                            "count": 238,
                            "rank": 1,
                            "tag": "中文圖書預約排行榜",
                            "type": "reserved",
                            "url": "http://webpac.lib.nthu.edu.tw/F?func=find-b&find_code=SYS&local_base=TOP01&request=1084958",
                            "year": 2012
                        },
                        {
                            "bookname": "別相信任何人",
                            "count": 183,
                            "rank": 2,
                            "tag": "中文圖書預約排行榜",
                            "type": "reserved",
                            "url": "http://webpac.lib.nthu.edu.tw/F?func=find-b&find_code=SYS&local_base=TOP01&request=2100053",
                            "year": 2012
                        },
                    ...
                }
        """
        parser = reqparse.RequestParser()
        ''' No need to check the type for testing '''
        ''' `apidoc` will request with empty parameters, like `?year=&...` '''
        parser.add_argument('year')
        parser.add_argument('type')
        parser.add_argument('rank')
        parser.add_argument('count')
        parser.add_argument('tag')
        parser.add_argument('bookname')

        args = parser.parse_args()
        return self._query(args)


api_v2.add_resource(SheetList, '/sheets', endpoint='sheets')
api_v2.add_resource(SheetItem, '/sheets/<sheet_id>')
api_v2.add_resource(SheetListForAPI, '/test/sheets')

api_v2.add_resource(TopbooksList, '/topbooks', endpoint='topbooks')
api_v2.add_resource(Topbook, '/topbooks/<book_id>')
