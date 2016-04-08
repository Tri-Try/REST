define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./application/static/doc/main.js",
    "group": "D__workspace_api_service_application_static_doc_main_js",
    "groupTitle": "D__workspace_api_service_application_static_doc_main_js",
    "name": ""
  },
  {
    "type": "get",
    "url": "/v2/sheets/:id",
    "title": "Fetch specific sheet data",
    "version": "2.0.0",
    "name": "get_sheet",
    "group": "ExamPaper",
    "permission": [
      {
        "name": "public"
      }
    ],
    "description": "<p>Get the information of year, department or examtype about specific sheet.</p>",
    "sampleRequest": [
      {
        "url": "http://tritry.cs.nthu.edu.tw/api/v2/sheets/:sheet_id"
      }
    ],
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://tritry.cs.nthu.edu.tw/api/v2/sheets/1025",
        "type": "curl"
      }
    ],
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "message",
            "description": "<p>The message for <code>sheet_id</code> which was not found.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP 404 Not Found\n{\n    \"message\": \"Sheet #5566 doesn't exist\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Sheet's ID.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "year",
            "description": "<p>Year of the sheet.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "department",
            "description": "<p>Department of the sheet.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "subject",
            "description": "<p>Subject.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "examtype",
            "description": "<p>Exam type.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP 200 OK\n{\n   \"result\": {\n       \"department\": \"'物理系'\",\n       \"subject\": \"'應用數學'\",\n       \"type\": \"'after-graduate-exams'\",\n       \"url\": \"http://www.lib.nthu.edu.tw/library/department/ref/exam/p/phys/86/860403.pdf\",\n       \"year\": 86\n   }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./application/api/v2.py",
    "groupTitle": "ExamPaper"
  },
  {
    "type": "get",
    "url": "/v2/sheets/",
    "title": "Query on sheets information",
    "version": "2.0.0",
    "name": "query_sheets",
    "group": "ExamPaper",
    "permission": [
      {
        "name": "public"
      }
    ],
    "description": "<p>Search for sheets by year, department or examtype.</p>",
    "sampleRequest": [
      {
        "url": "http://tritry.cs.nthu.edu.tw/api/v2/test/sheets"
      }
    ],
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i \"http://tritry.cs.nthu.edu.tw/api/v2/sheets?year=102&department=物理系\"",
        "type": "curl"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "size": "84-*",
            "optional": true,
            "field": "year",
            "description": "<p>Specify year. (民國紀年)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "department",
            "description": "<p>Specify department.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "\"after-graduate-exams\"",
              "\"transfer-exams\""
            ],
            "optional": true,
            "field": "examtype",
            "description": "<p>Specify examtype.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{ \"year\": 102, \"department\": \"物理系\", \"type\": \"after-graduate-exams\" }",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Sheet's ID.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "year",
            "description": "<p>Year of the sheet.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "department",
            "description": "<p>Department of the sheet.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "subject",
            "description": "<p>Subject.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "examtype",
            "description": "<p>Exam type.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n   \"result\": [\n   {\n       \"department\": \"'物理系'\",\n       \"subject\": \"'近代物理'\",\n       \"type\": \"'after-graduate-exams'\",\n       \"url\": \"http://www.lib.nthu.edu.tw/library/department/ref/exam/p/phys/101/2003.pdf\",\n       \"year\": 101\n   },\n   ...\n   ]\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./application/api/v2.py",
    "groupTitle": "ExamPaper"
  },
  {
    "type": "get",
    "url": "/v1/sheets",
    "title": "Fetch data of all sheets",
    "version": "1.0.0",
    "name": "query_sheets",
    "group": "ExamPaper",
    "permission": [
      {
        "name": "public"
      }
    ],
    "description": "<p>Get the information of year, department or examtype of all sheets.</p>",
    "sampleRequest": [
      {
        "url": "http://tritry.cs.nthu.edu.tw/api/v1/sheets"
      }
    ],
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://tritry.cs.nthu.edu.tw/api/v1/sheets",
        "type": "curl"
      }
    ],
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Sheet's ID.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "year",
            "description": "<p>Year of the sheet.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "department",
            "description": "<p>Department of the sheet.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "subject",
            "description": "<p>Subject.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "examtype",
            "description": "<p>Exam type.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n[\n   {\n       \"department\": \"'物理系'\",\n       \"subject\": \"'近代物理'\",\n       \"type\": \"'after-graduate-exams'\",\n       \"url\": \"http://www.lib.nthu.edu.tw/library/department/ref/exam/p/phys/101/2003.pdf\",\n       \"year\": 101\n   },\n   ...\n]",
          "type": "json"
        }
      ]
    },
    "filename": "./application/api/v1.py",
    "groupTitle": "ExamPaper"
  },
  {
    "type": "get",
    "url": "/v1/lost",
    "title": "Get all lost info in library",
    "version": "1.0.0",
    "name": "get_lost_objects",
    "group": "LibraryLost",
    "permission": [
      {
        "name": "public"
      }
    ],
    "description": "<p>Get all lost objects information in library with <code>default filter</code>. This is for preview and test, you should use below one for query and search items.</p>",
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://tritry.cs.nthu.edu.tw/api/v1/lost",
        "type": "curl"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "[\n    {\n        \"description\": \"隨身碟 黑色 中間灰色\",\n        \"id\": \"1\",\n        \"place\": \"總圖 1F\",\n        \"system_id\": \"11070\",\n        \"time\": \"2015-07-25\"\n    },\n    ...\n]",
          "type": "json"
        }
      ]
    },
    "sampleRequest": [
      {
        "url": "http://tritry.cs.nthu.edu.tw/api/v1/lost"
      }
    ],
    "filename": "./application/api/v1.py",
    "groupTitle": "LibraryLost"
  },
  {
    "type": "get",
    "url": "/v1/lost",
    "title": "Query lost objects info in library",
    "version": "1.0.0",
    "name": "query_lost_objects",
    "group": "LibraryLost",
    "permission": [
      {
        "name": "public"
      }
    ],
    "description": "<p>Query lost objects information in library.</p>",
    "sampleRequest": [
      {
        "url": "http://tritry.cs.nthu.edu.tw/api/v1/lost"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "\"ALL\"",
              "\"0\"",
              "\"1\""
            ],
            "optional": true,
            "field": "place",
            "defaultValue": "ALL",
            "description": "<p>Specify which library. (<code>0</code>: 總圖, <code>1</code>:人社分館)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "date_start",
            "description": "<p>Specify start date in format (YYYY-MM-DD).</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "date_end",
            "description": "<p>Specify end date in format (YYYY-MM-DD).</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "catalog",
            "defaultValue": "ALL",
            "description": "<p>Specify catalog.</p> <ul>     <li><code>\"ALL\"</code>全部類別, </li>     <li><code>\"0\"</code>皮夾／證件／各式卡片, </li>     <li><code>\"1\"</code>眼鏡／鑰匙／手錶, </li>     <li><code>\"2\"</code>水壺／水杯, </li>     <li><code>\"3\"</code>雨具, </li>     <li><code>\"4\"</code>隨身電子產品, </li>     <li><code>\"5\"</code>背包／手提袋, </li>     <li><code>\"6\"</code>書籍／光碟, </li>     <li><code>\"7\"</code>衣物, </li>     <li><code>\"8\"</code>文具用品, </li>     <li><code>\"9\"</code>其它</li> </ul>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "keyword",
            "description": "<p>Keyword description for object.</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i \"http://tritry.cs.nthu.edu.tw/api/v1/lost?date_start=2016-03-01&date_end=2016-03-31\"",
        "type": "curl"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "[\n    {\n        \"description\": \"直傘 綠\",\n        \"id\": \"1\",\n        \"place\": \"總圖 3F\",\n        \"system_id\": \"12931\",\n        \"time\": \"2016-03-31\"\n    },\n    {\n        \"description\": \"外套 白色 白色大外套(女)\",\n        \"id\": \"2\",\n        \"place\": \"總圖 5F\",\n        \"system_id\": \"12930\",\n        \"time\": \"2016-03-31\"\n    },\n    ...\n]",
          "type": "json"
        }
      ]
    },
    "filename": "./application/api/v1.py",
    "groupTitle": "LibraryLost"
  },
  {
    "type": "get",
    "url": "/v1/space",
    "title": "Get space info of library rooms",
    "version": "1.0.0",
    "name": "get_remaining_space",
    "group": "LibraryRoom",
    "permission": [
      {
        "name": "public"
      }
    ],
    "description": "<p>Get the information remaining room space in library.</p>",
    "sampleRequest": [
      {
        "url": "http://tritry.cs.nthu.edu.tw/api/v1/space"
      }
    ],
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://tritry.cs.nthu.edu.tw/api/v1/space",
        "type": "curl"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"人社分館研究小間\": \"0\",\n    \"團體室\": \"0\",\n    \"夜讀區\": \"150\",\n    \"大團體室\": \"1\",\n    \"研究小間\": \"0\",\n    \"簡報練習室\": \"0\",\n    \"聆賞席(請洽櫃台預約)\": \"50\",\n    \"討論室\": \"5\",\n    \"語言學習區\": \"2\",\n    \"電腦共學區\": \"23\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./application/api/v1.py",
    "groupTitle": "LibraryRoom"
  },
  {
    "type": "get",
    "url": "/v2/topbooks",
    "title": "Get the single book info",
    "version": "2.0.0",
    "name": "get_top_book",
    "group": "Librarybooks",
    "permission": [
      {
        "name": "public"
      }
    ],
    "description": "<p>Get the single book information recorded in rank list</p>",
    "sampleRequest": [
      {
        "url": "http://tritry.cs.nthu.edu.tw/api/v2/topbooks/:id"
      }
    ],
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i \"http://tritry.cs.nthu.edu.tw/api/v2/topbooks/6666\"",
        "type": "curl"
      }
    ],
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Book's ID.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "year",
            "description": "<p>Year of the rank list.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "bookname",
            "description": "<p>Bookname.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "rank",
            "description": "<p>Rank in that year.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "tag",
            "description": "<p>Name of rank list.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "type",
            "description": "<p>Type of rank list.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "URL",
            "description": "<p>URL of book in the library circulation system.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "    {\n    \"result\": {\n        \"bookname\": \"如何使基金報酬最大化\",\n        \"count\": 20,\n        \"rank\": 127,\n        \"tag\": \"中文圖書借閱排行榜\",\n        \"type\": \"loaned\",\n        \"url\": \"http://webpac.lib.nthu.edu.tw/F?func=find-c&ccl_term=OYS%3D0719217&T=2&ty=ie\",\n        \"year\": 2007\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./application/api/v2.py",
    "groupTitle": "Librarybooks"
  },
  {
    "type": "get",
    "url": "/v1/newbooks",
    "title": "Query new books info in library",
    "version": "1.0.0",
    "name": "query_new_books",
    "group": "Librarybooks",
    "permission": [
      {
        "name": "public"
      }
    ],
    "description": "<p>Query new books information in library.</p>",
    "sampleRequest": [
      {
        "url": "http://tritry.cs.nthu.edu.tw/api/v1/newbooks"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "\"en\"",
              "\"zh\""
            ],
            "optional": true,
            "field": "lang",
            "description": "<p>Specify lnaguage filter.</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i \"http://tritry.cs.nthu.edu.tw/api/v1/newbooks?lang=en\"",
        "type": "curl"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "[\n    {\n        \"author\": \"Scheffel, Wolfgang.\",\n        \"author_detail\": {\n            \"name\": \"Scheffel, Wolfgang.\"\n        },\n        \"authors\": [\n            {\n                \"name\": \"Scheffel, Wolfgang.\"\n            }\n        ],\n        \"link\": \"http://140.114.72.24:80/F?func=find-b&find_code=SYS&adjacent=Y&local_base=TOP01&request=003066304\",\n        \"links\": [\n            {\n                \"href\": \"http://140.114.72.24:80/F?func=find-b&find_code=SYS&adjacent=Y&local_base=TOP01&request=003066304\",\n                \"rel\": \"alternate\",\n                \"type\": \"text/html\"\n            }\n        ],\n    ...\n]",
          "type": "json"
        }
      ]
    },
    "filename": "./application/api/v1.py",
    "groupTitle": "Librarybooks"
  },
  {
    "type": "get",
    "url": "/v2/topbooks",
    "title": "Query top books info in library",
    "version": "2.0.0",
    "name": "query_top_books",
    "group": "Librarybooks",
    "permission": [
      {
        "name": "public"
      }
    ],
    "description": "<p>Query top books information in library.</p>",
    "sampleRequest": [
      {
        "url": "http://tritry.cs.nthu.edu.tw/api/v2/topbooks"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "size": "2003-*",
            "optional": true,
            "field": "year",
            "description": "<p>Specify year.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "\"loaned\"",
              "\"reserved\""
            ],
            "optional": true,
            "field": "type",
            "defaultValue": "loaned",
            "description": "<p>Specify type of circulations.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "rank",
            "description": "<p>Specify rank.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "count",
            "description": "<p>Specify circulations to filter out results that greater than this value.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "tag",
            "description": "<p>Specify tag.</p> <ul>     <li><code>中文圖書借閱排行榜</code></li>     <li><code>中文圖書預約排行榜</code></li>     <li><code>中文小說圖書借閱排行榜</code></li>     <li><code>中文小說圖書預約排行榜</code></li>     <li><code>英文小說圖書借閱排行榜</code></li>     <li><code>西文圖書借閱排行榜</code></li>     <li><code>西文圖書預約排行榜</code></li>     <li><code>西文小說圖書借閱排行榜</code></li>     <li><code>視聽資料DVD電影片借閱排行榜</code></li>     <li><code>視聽資料DVD電影片預約排行榜</code></li>     <li><code>視聽資料借閱排行榜(不含DVD電影片)</code></li>     <li><code>視聽資料借閱排行榜(不含電影、卡通)</code></li>     <li><code>視聽資料電影、卡通借閱排行榜</code></li>     <li><code>視聽資料電影、卡通預約排行榜</code></li>     <li><code>視聽資料預約排行榜(不含DVD電影片)</code></li>     <li><code>視聽資料預約排行榜(不含電影、卡通)</code></li> </ul>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "bookname",
            "description": "<p>Specify bookname.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{ \"year\": 102, \"type\": \"reserved\", \"count\": 100 }",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i \"http://tritry.cs.nthu.edu.tw/api/v2/topbooks?year=2012&type=reserved&count=100\"",
        "type": "curl"
      }
    ],
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Book's ID.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "year",
            "description": "<p>Year of the rank list.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "bookname",
            "description": "<p>Bookname.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "rank",
            "description": "<p>Rank in that year.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "tag",
            "description": "<p>Name of rank list.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "type",
            "description": "<p>Type of rank list.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "URL",
            "description": "<p>URL of book in the library circulation system.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"result\": [\n        {\n            \"bookname\": \"飢餓遊戲\",\n            \"count\": 238,\n            \"rank\": 1,\n            \"tag\": \"中文圖書預約排行榜\",\n            \"type\": \"reserved\",\n            \"url\": \"http://webpac.lib.nthu.edu.tw/F?func=find-b&find_code=SYS&local_base=TOP01&request=1084958\",\n            \"year\": 2012\n        },\n        {\n            \"bookname\": \"別相信任何人\",\n            \"count\": 183,\n            \"rank\": 2,\n            \"tag\": \"中文圖書預約排行榜\",\n            \"type\": \"reserved\",\n            \"url\": \"http://webpac.lib.nthu.edu.tw/F?func=find-b&find_code=SYS&local_base=TOP01&request=2100053\",\n            \"year\": 2012\n        },\n    ...\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./application/api/v2.py",
    "groupTitle": "Librarybooks"
  },
  {
    "type": "get",
    "url": "/v1/topbooks",
    "title": "Get all top books info in library",
    "version": "1.0.0",
    "name": "query_top_books",
    "group": "Librarybooks",
    "permission": [
      {
        "name": "public"
      }
    ],
    "description": "<p>Get all top books information in library. <strong>Not recommend</strong>, use <code>api/v2</code> instead.</p>",
    "sampleRequest": [
      {
        "url": "http://tritry.cs.nthu.edu.tw/api/v1/topbooks"
      }
    ],
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://tritry.cs.nthu.edu.tw/api/v1/topbooks",
        "type": "curl"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "[\n    {\n        \"bookname\": \"清宮內務府造辦處檔案總匯 雍正-乾隆\",\n        \"count\": 262,\n        \"rank\": 1,\n        \"tag\": \"中文圖書借閱排行榜\",\n        \"type\": \"loaned\",\n        \"url\": \"http://webpac.lib.nthu.edu.tw/F?func=find-b&find_code=SYS&local_base=TOP01&request=272150\",\n        \"year\": 2015\n    },\n    {\n        \"bookname\": \"移動迷宮\",\n        \"count\": 197,\n        \"rank\": 2,\n        \"tag\": \"中文圖書借閱排行榜\",\n        \"type\": \"loaned\",\n        \"url\": \"http://webpac.lib.nthu.edu.tw/F?func=find-b&find_code=SYS&local_base=TOP01&request=2156152\",\n        \"year\": 2015\n    },\n    ...\n]",
          "type": "json"
        }
      ]
    },
    "filename": "./application/api/v1.py",
    "groupTitle": "Librarybooks"
  }
] });
