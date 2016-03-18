define({ "api": [
  {
    "type": "get",
    "url": "/sheets/",
    "title": "Request sheets information",
    "version": "2.0.0",
    "name": "get_sheet",
    "group": "Sheet",
    "description": "<p>Query for sheets by year, department and examtype.</p>",
    "sampleRequest": [
      {
        "url": "https://flaskapi-weering.c9users.io/api/v2/sheets"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "year",
            "description": "<p>Specify year.</p>"
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
            "optional": true,
            "field": "examtype",
            "description": "<p>Specify examtype.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{ \"year\": 102, \"department\": \"物理系\" }",
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
            "description": "<p>Year.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "department",
            "description": "<p>Department.</p>"
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
    "filename": "application/api/v2.py",
    "groupTitle": "Sheet"
  },
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
    "filename": "application/static/doc/main.js",
    "group": "_home_ubuntu_workspace_application_static_doc_main_js",
    "groupTitle": "_home_ubuntu_workspace_application_static_doc_main_js",
    "name": ""
  }
] });
