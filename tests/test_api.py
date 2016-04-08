import pytest


@pytest.mark.options(debug=False)
def test_app(app):
    assert not app.debug, 'Ensure the app not in debug mode'


class TestApp:

    def _check_json(self, r):
        assert r.status_code == 200
        assert r.mimetype == 'application/json'

    def test_api_v1_with_param(self, client):
        self._check_json(client.get(
            '/api/v1/lost?%s' % 'date_start=2016-03-01&date_end=2016-03-31'))
        self._check_json(client.get(
            '/api/v1/lost?%s' % 'place=0'))
        self._check_json(client.get(
            '/api/v1/lost?%s' % 'place=1'))
        self._check_json(client.get(
            '/api/v1/lost?%s' % 'catalog=1'))
