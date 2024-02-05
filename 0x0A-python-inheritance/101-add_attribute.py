#!/usr/bin/python3
"""101-add_attribute module"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible.
    Args:
        obj: the object, instance of the class
        name: attribute name
        value: value of the attribute
    Raise:
        TypeError: can't add new attribute
    """
    if hasattr(obj, "__dict__"):
        return setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
