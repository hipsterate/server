from datetime import datetime

from sqlalchemy.types import DateTime, TypeDecorator
from flask_sqlalchemy import SQLAlchemy

from app.common.util import utc, localtz


db = SQLAlchemy()


class DateTimeUTC(TypeDecorator):
    """ https://github.com/spoqa/sqlalchemy-utc
    Almost equivalent to :class:`~sqlalchemy.types.DateTime` with
    ``timezone=True`` option, but it differs from that by:
    - Never silently take naive :class:`~datetime.datetime`, instead it
      always raise :exc:`ValueError` unless time zone aware value.
    - :class:`~datetime.datetime` value's :attr:`~datetime.datetime.tzinfo`
      is always converted to UTC.
    - Unlike SQLAlchemy's built-in :class:`~sqlalchemy.types.DateTime`,
      it never return naive :class:`~datetime.datetime`, but time zone
      aware value, even with SQLite or MySQL.
    """

    impl = DateTime(timezone=True)

    def process_bind_param(self, value, dialect):
        if value is not None:
            if not isinstance(value, datetime):
                raise TypeError('expected datetime.datetime, not ' +
                                repr(value))
            elif value.tzinfo is None:
                raise ValueError('naive datetime is disallowed')
            return value.astimezone(utc)

    def process_result_value(self, value, dialect):
        if value is not None and value.tzinfo is None:
            value = value.astimezone(localtz)
        return value
