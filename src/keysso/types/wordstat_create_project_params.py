# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .wordstat.item import Item
from .type_base_param import TypeBaseParam

__all__ = ["WordstatCreateProjectParams", "DataType1", "DataType0"]


class WordstatCreateProjectParams(TypedDict, total=False):
    data: Required[Union[DataType1, DataType0]]
    """Данные для парсинга"""


class DataType1(TypeBaseParam, total=False):
    source: int
    """Источник `0` - Wordstat, `1` - Direct"""

    type: Literal[1]
    """Тип проекта `0` - сбор фраз, `1` - сбор частотности"""

    ws_types: Iterable[Item]
    """
    Типы частотности: `0` - Wordstat `3` - "Wordstat" `1` - "!Wordstat" `2` -
    "[!Wordstat]"
    """


class DataType0(TypeBaseParam, total=False):
    type: Literal[0]
    """Тип проекта `0` - сбор фраз, `1` - сбор частотности"""
