import pytest
from flask import url_for


@pytest.mark.options(debug=False)
def test_app(app):
    assert not app.debug, 'Ensure the app not in debug mode'


class TestApp:

    def test_page(self, client):
        assert client.get(
            url_for('page.index_service')).status_code == 200
        assert client.get(
            url_for('page.doc_service', path='doc')).status_code == 200

    def _check_json(self, r):
        assert r.status_code == 200
        assert r.mimetype == 'application/json'

    def test_api_v1(self, client):
        self._check_json(client.get('/api/v1/sheets'))
        self._check_json(client.get('/api/v1/topbooks'))

    def test_api_v1_proxy_services(self, client):
        self._check_json(client.get('/api/v1/lost'))
        self._check_json(client.get('/api/v1/newbooks'))
        self._check_json(client.get('/api/v1/space'))

    def test_api_v2(self, client):
        self._check_json(client.get('/api/v2/sheets'))
        self._check_json(client.get('/api/v2/topbooks'))
