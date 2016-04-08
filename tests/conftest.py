import os
import sys
import pytest

# Hacky way to import application/
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')

from application.api_service import create_app


@pytest.fixture
def app():
    app = create_app()
    return app
