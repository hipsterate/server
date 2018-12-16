from datetime import datetime, timedelta, tzinfo

import pytz


class UTC(tzinfo):
    zero = timedelta(0)

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


localtz = pytz.timezone('Asia/Seoul')


def utcnow():
    return datetime.now().astimezone(utc)
