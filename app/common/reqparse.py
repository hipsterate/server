from flask_restplus import reqparse


base_parser = reqparse.RequestParser(bundle_errors=True)


class Inputs():
    @classmethod
    def enum(cls, enum_cls):
        def validate(value):
            return enum_cls(value.upper())

        return validate
