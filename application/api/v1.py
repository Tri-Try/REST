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
    'newbooks': NTHULibrary.get_newest_books,
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
    d = params.to_dict()
    return {k: v for k, v in d.items() if v != ''}


def make_job(service_id, param):
    param = clean_param(param) if param else None
    print(param)
    return route_func[service_id](**param) if param \
        else route_func[service_id]()


def query_from_db(service_id):
    return marshal(Sheet.query.all(), resource_fields) \
        if service_id == 'sheets' \
        else marshal(Circulation.query.all(), circulation_fields)


class Library(Resource):

    def get(self, service_id):
        if service_id in ['space', 'lost', 'newbooks']:
            return make_job(service_id, request.args)
        if service_id in ['sheets', 'topbooks']:
            return query_from_db(service_id)
        abort(404, message="Data {} doesn't exist".format(service_id))


api_v1.add_resource(Library, '/<string:service_id>')

docs = {
    'routes': [
        {'key': '失物招領', 'url': '/api/v1/lost'},
        {'key': '新進圖書資料', 'url': '/api/v1/newbooks'},
        {'key': '考古題', 'url': '/api/v1/sheets'},
        {'key': '空間借閱系統', 'url': '/api/v1/space'},
        {'key': '借閱排行榜', 'url': '/api/v1/topbooks'},
    ]
}


def fake_for_questions():
    """
    @api {get} /v1/sheets Fetch data of all sheets
    @apiVersion 1.0.0
    @apiName query_sheets
    @apiGroup ExamPaper
    @apiPermission public
    @apiDescription Get the information of year, department or examtype of all sheets.

    @apiSampleRequest http://tritry.cs.nthu.edu.tw/api/v1/sheets
    @apiExample {curl} Example usage:
        curl -i http://tritry.cs.nthu.edu.tw/api/v1/sheets

    @apiSuccess {Number} id               Sheet's ID.
    @apiSuccess {Number} year             Year of the sheet.
    @apiSuccess {String} department       Department of the sheet.
    @apiSuccess {String} subject          Subject.
    @apiSuccess {String} examtype         Exam type.

    @apiSuccessExample {json} Success-Response:
             HTTP/1.1 200 OK
             [
                {
                    "department": "'物理系'",
                    "subject": "'近代物理'",
                    "type": "'after-graduate-exams'",
                    "url": "http://www.lib.nthu.edu.tw/library/department/ref/exam/p/phys/101/2003.pdf",
                    "year": 101
                },
                ...
             ]
    """
    pass


def fake_for_space():
    """
    @api {get} /v1/space Get space info of library rooms
    @apiVersion 1.0.0
    @apiName get_remaining_space
    @apiGroup LibraryRoom
    @apiPermission public
    @apiDescription Get the information remaining room space in library.

    @apiSampleRequest http://tritry.cs.nthu.edu.tw/api/v1/space
    @apiExample {curl} Example usage:
        curl -i http://tritry.cs.nthu.edu.tw/api/v1/space
    @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
                "人社分館研究小間": "0",
                "團體室": "0",
                "夜讀區": "150",
                "大團體室": "1",
                "研究小間": "0",
                "簡報練習室": "0",
                "聆賞席(請洽櫃台預約)": "50",
                "討論室": "5",
                "語言學習區": "2",
                "電腦共學區": "23"
            }
    """
    pass


def fake_for_lost():
    """
    @api {get} /v1/lost Get all lost info in library
    @apiVersion 1.0.0
    @apiName get_lost_objects
    @apiGroup LibraryLost
    @apiPermission public
    @apiDescription Get all lost objects information in library with <code>default filter</code>. This is for preview and test, you should use below one for query and search items.

    @apiExample {curl} Example usage:
        curl -i http://tritry.cs.nthu.edu.tw/api/v1/lost

    @apiSuccessExample {json} Success-Response:
            [
                {
                    "description": "隨身碟 黑色 中間灰色",
                    "id": "1",
                    "place": "總圖 1F",
                    "system_id": "11070",
                    "time": "2015-07-25"
                },
                ...
            ]
    @apiSampleRequest http://tritry.cs.nthu.edu.tw/api/v1/lost
    """
    pass


def fake_for_lost_query():
    """
    @api {get} /v1/lost Query lost objects info in library
    @apiVersion 1.0.0
    @apiName query_lost_objects
    @apiGroup LibraryLost
    @apiPermission public
    @apiDescription Query lost objects information in library.

    @apiSampleRequest http://tritry.cs.nthu.edu.tw/api/v1/lost
    @apiParam {String="ALL", "0", "1"} [place="ALL"]
        Specify which library. (<code>0</code>: 總圖, <code>1</code>:人社分館)
    @apiParam {String} [date_start]   Specify start date in format (YYYY-MM-DD).
    @apiParam {String} [date_end]     Specify end date in format (YYYY-MM-DD).
    @apiParam {String} [catalog="ALL"]
        Specify catalog.
        <ul>
            <li><code>"ALL"</code>全部類別, </li>
            <li><code>"0"</code>皮夾／證件／各式卡片, </li>
            <li><code>"1"</code>眼鏡／鑰匙／手錶, </li>
            <li><code>"2"</code>水壺／水杯, </li>
            <li><code>"3"</code>雨具, </li>
            <li><code>"4"</code>隨身電子產品, </li>
            <li><code>"5"</code>背包／手提袋, </li>
            <li><code>"6"</code>書籍／光碟, </li>
            <li><code>"7"</code>衣物, </li>
            <li><code>"8"</code>文具用品, </li>
            <li><code>"9"</code>其它</li>
        </ul>
    @apiParam {String} [keyword]      Keyword description for object.

    @apiExample {curl} Example usage:
        curl -i "http://tritry.cs.nthu.edu.tw/api/v1/lost?date_start=2016-03-01&date_end=2016-03-31"

    @apiSuccessExample {json} Success-Response:
            [
                {
                    "description": "直傘 綠",
                    "id": "1",
                    "place": "總圖 3F",
                    "system_id": "12931",
                    "time": "2016-03-31"
                },
                {
                    "description": "外套 白色 白色大外套(女)",
                    "id": "2",
                    "place": "總圖 5F",
                    "system_id": "12930",
                    "time": "2016-03-31"
                },
                ...
            ]
    """
    pass


def fake_for_newbooks():
    """
    @api {get} /v1/newbooks Query new books info in library
    @apiVersion 1.0.0
    @apiName query_new_books
    @apiGroup Librarybooks
    @apiPermission public
    @apiDescription Query new books information in library.

    @apiSampleRequest http://tritry.cs.nthu.edu.tw/api/v1/newbooks
    @apiParam {String="en", "zh"} [lang]    Specify lnaguage filter.

    @apiExample {curl} Example usage:
        curl -i "http://tritry.cs.nthu.edu.tw/api/v1/newbooks?lang=en"

    @apiSuccessExample {json} Success-Response:
            [
                {
                    "author": "Scheffel, Wolfgang.",
                    "author_detail": {
                        "name": "Scheffel, Wolfgang."
                    },
                    "authors": [
                        {
                            "name": "Scheffel, Wolfgang."
                        }
                    ],
                    "link": "http://140.114.72.24:80/F?func=find-b&find_code=SYS&adjacent=Y&local_base=TOP01&request=003066304",
                    "links": [
                        {
                            "href": "http://140.114.72.24:80/F?func=find-b&find_code=SYS&adjacent=Y&local_base=TOP01&request=003066304",
                            "rel": "alternate",
                            "type": "text/html"
                        }
                    ],
                ...
            ]
    """
    pass


def fake_for_topbooks():
    """
    @api {get} /v1/topbooks Get all top books info in library
    @apiVersion 1.0.0
    @apiName query_top_books
    @apiGroup Librarybooks
    @apiPermission public
    @apiDescription Get all top books information in library. <strong>Not recommend</strong>, use <code>api/v2</code> instead.

    @apiSampleRequest http://tritry.cs.nthu.edu.tw/api/v1/topbooks

    @apiExample {curl} Example usage:
        curl -i http://tritry.cs.nthu.edu.tw/api/v1/topbooks

    @apiSuccessExample {json} Success-Response:
            [
                {
                    "bookname": "清宮內務府造辦處檔案總匯 雍正-乾隆",
                    "count": 262,
                    "rank": 1,
                    "tag": "中文圖書借閱排行榜",
                    "type": "loaned",
                    "url": "http://webpac.lib.nthu.edu.tw/F?func=find-b&find_code=SYS&local_base=TOP01&request=272150",
                    "year": 2015
                },
                {
                    "bookname": "移動迷宮",
                    "count": 197,
                    "rank": 2,
                    "tag": "中文圖書借閱排行榜",
                    "type": "loaned",
                    "url": "http://webpac.lib.nthu.edu.tw/F?func=find-b&find_code=SYS&local_base=TOP01&request=2156152",
                    "year": 2015
                },
                ...
            ]
    """
    pass
