from contextlib import contextmanager

import pytest

from app.common.db import db


@contextmanager
def rollback_tx():
    session = db.session

    yield session


class DBTC():
    @pytest.fixture(scope='function', autouse=True)
    def tx(self, mocker):
        mocker.patch('app.common.db.TX.get', new=rollback_tx)

        yield

        db.session.rollback()
        db.session.remove()

    def insert(self, obj):
        db.session.add(obj)
