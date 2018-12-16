import pytest

from app import create_app


@pytest.fixture(scope='session', autouse=True)
def flask_app():
    app = create_app()
    app_context = app.app_context()
    app_context.push()

    yield app

    app_context.pop()


@pytest.fixture(scope='session', autouse=True)
def test_client(flask_app):
    yield flask_app.test_client()
