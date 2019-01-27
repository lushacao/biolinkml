import re

from dataclasses import field


def empty_list():
    return field(default_factory=list)


def empty_dict():
    return field(default_factory=dict)


def empty_set():
    return field(default_factory=set)


class NCName(str):
    """ Wrapper for NCName class

    See: <https://www.w3.org/TR/1999/REC-xml-names-19990114/#NT-NCName>
    """
    ncname_pattern = re.compile(r'[a-zA-Z][a-zA-Z0-9._-]*$')

    def __init__(self, v: str) -> None:
        if not self.is_valid(v):
            raise ValueError(f"{v}: invalid prefix")

    @classmethod
    def is_valid(cls, v: str) -> bool:
        return bool(cls.ncname_pattern.match(v))


class Uri(str):
    # TODO: Implement this
    pass


class Bool:
    """ Wrapper for boolean class """
    bool_true = re.compile(r'([Tt]rue)|(1)$')
    bool_false = re.compile(r'([Ff]alse)|(0)$')

    def __new__(cls, v):
        if isinstance(v, bool):
            return v
        if cls.bool_true.match(str(v)):
            return True
        if cls.bool_false.match(str(v)):
            return False
        raise ValueError(f"{v}: Must be a boolean value")
