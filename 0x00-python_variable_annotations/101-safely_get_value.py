#!/usr/bin/env python3
"""
Module contains safely_get_value fun
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """AI is creating summary for safely_get_value

    Args:
        dct (Mapping): a dictionary
        key (Any): key of the value to be searched for
        default (Union[T, None], optional): TypeVar. Defaults to None.

    Returns:
        Union[Any, T]: default or value of dct[key]
    """
    if key in dct:
        return dct[key]
    else:
        return default
