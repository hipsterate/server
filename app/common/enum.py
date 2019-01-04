from enum import Enum
from json import JSONEncoder


# monkey patches default JSONEncoder to make Enum json serializable
stdlib_default = JSONEncoder().default


def serializable_enum(self, obj):
    if isinstance(obj, Enum):
        return obj.name.lower()

    return stdlib_default


JSONEncoder.default = serializable_enum


class BaseEnum(Enum):
    @classmethod
    def values(cls):
        return [enum_obj.value for enum_obj in list(cls)]

    @classmethod
    def lower_values(cls):
        return [enum_obj.value.lower() for enum_obj in list(cls)]


class StringEnum(BaseEnum):
    def _generate_next_value_(name, start, count, last_values):
        return name
