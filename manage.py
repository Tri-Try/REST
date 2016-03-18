from flask.ext.script import Command, Manager
from application.api_service import create_app


app = create_app()
manager = Manager(app)


class Hello(Command):
    "prints hello world"

    def run(self):
        print("apidoc --input application/ --output application/static/doc/")

manager.add_command('hello', Hello())


if __name__ == "__main__":
    manager.run()
