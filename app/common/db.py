import datetime

import pytz
from sqlalchemy.types import DateTime, TypeDecorator
from flask_sqlalchemy import SQLAlchemy


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
            if not isinstance(value, datetime.datetime):
                raise TypeError('expected datetime.datetime, not ' +
                                repr(value))
            elif value.tzinfo is None:
                raise ValueError('naive datetime is disallowed')
            return value.astimezone(utc)

    def process_result_value(self, value, dialect):
        if value is not None and value.tzinfo is None:
            value = value.astimezone(self.local_tz)
        return value


class UTC(datetime.tzinfo):

    zero = datetime.timedelta(0)

    def utcoffset(self, _):
        return self.zero

    def dst(self, _):
        return self.zero

    def tzname(self, _):
        return 'UTC'


try:
    utc = datetime.timezone.utc
except AttributeError:
    utc = UTC()


local_tz = pytz.timezone('Asia/Seoul')