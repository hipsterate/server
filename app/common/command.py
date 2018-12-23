import functools
import types

from app.common.db import TX


class Command():
    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if not isinstance(attr, types.MethodType):
            return super().__getattribute__(name)

        @functools.wraps(attr)
        def wrapped(*args, **kwargs):
            session = kwargs.get('session')
            if session is None:
                # use new transaction per function
                with TX.get() as session:
                    setattr(self, 'session', session)
                    return attr(*args, **kwargs)

            # use injected transaction
            setattr(self, 'session', session)
            return attr(*args, **kwargs)

        return wrapped

    def insert(self, obj):
        self.session.add(obj)
