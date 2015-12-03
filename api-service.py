from flask import Flask, render_template

from v1 import api_v1_bp, API_VERSION_V1

app = Flask(__name__)


@app.route("/")
def index_service():
    return render_template('index.html')


app.register_blueprint(
    api_v1_bp,
    url_prefix='/{prefix}/{version}'.format(prefix='api', version=API_VERSION_V1)
)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
