"""
This is a module demonstrating reST code documentation features.

Most part of this documentation is using Python type hinting.
"""

from typing import AnyStr, Generator, Union, List, Dict


def demo_fields_docstring_arguments(m, b):  # type: ignore
    """
    Fields are used to describe specific properties of a documented object.

    This function can be used in conjuction with `demo_typing_arguments` to
    find an arbitrary function's zeros.

    :type  m: number
    :param m: The slope of the line.
    :type  b: number
    :param b: The y intercept of the line.
    :rtype:   number
    :return:  the x intercept of the line M{y=m*x+b}.
    """
    return -b/m

def demo_consolidated_fields(a:float, b):  # type: ignore
    """
    Fields can be condensed into one "consolidated" field. Looks better in plain text.

    :Parameters:
        - `a`: The size of the fox (in meters)
        - `b`: The weight of the fox (in stones)
    :rtype: str
    :return: The number of foxes
    """
    return -b/a

def demo_typing_arguments(name: str, size: bytes) -> bool:
    """
    Type documentation can be extracted from standard Python type hints.

    :param name: The human readable name for something.
    :param size: How big the name should be.
    :return: Always `True`.
    """
    return True

def demo_long_function_and_parameter_names__this_indeed_very_long(
        this_is_a_very_long_parameter_name_aahh: str, 
        what__another_super_super_long_name__ho_no: Generator[Union[List[AnyStr], Dict[str, AnyStr]], None, None]) -> bool:
    """
    Long names and annotations should display on several lines when they don't fit in a single line. 
    """
    return True

def demo_cross_reference() -> None:
    r"""
    The inline markup construct ```object``` is used to create links to the documentation for other Python objects.
    'text' is the text that should be displayed for the link, and 'object' is the name of the Python object that should be linked to.

    If you wish to use the name of the Python object as the text for the link, you can simply write ```object``` -> `object`.

    - `demo_typing_arguments`
    """



class _PrivateClass:
    """
    This is the docstring of a private class.
    """

    def method_inside_private(self) -> bool:
        """
        A public method inside a private class.

        :return: Something.
        """
        return True


    def _private_inside_private(self) -> bool:
        """
        A private method inside a private class.

        :return: Something.
        """
        return True


class DemoClass:
    """
    This is the docstring of this class.
    """

    def __init__(self, one: str, two: bytes) -> None:
        """
        Documentation for class initialization.

        :param one: Docs for first argument.
        :param two: Docs for second argument.
        """

    @property
    def read_only(self) -> int:
        """
        This is a read-only property.
        """
        return 1

    @property
    def read_and_write(self) -> int:
        """
        This is a read-write property.
        """
        return 1

    @read_and_write.setter
    def read_and_write(self, value: int) -> None:
        """
        This is a docstring for setter.
        """

    @property
    def read_and_write_delete(self) -> int:
        """
        This is a read-write-delete property.
        """
        return 1

    @read_and_write_delete.setter
    def read_and_write_delete(self, value: int) -> None:
        """
        This is a docstring for setter.
        """

    @read_and_write_delete.deleter
    def read_and_write_delete(self) -> None:
        """
        This is a docstring for deleter.
        """
