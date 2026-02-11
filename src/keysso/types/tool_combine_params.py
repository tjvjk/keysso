# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ToolCombineParams"]


class ToolCombineParams(TypedDict, total=False):
    lists: Required[Iterable[Iterable[object]]]
    """Список поисковых фраз"""

    options: SequenceNotStr[str]
    """
    Дополнительные настройки: `Заключить в " "` - quotes `Заключить в «[ ]»` -
    brackets `Добавить комбинации без операторов` - simple
    `Добавить «+» к стоп-словам` - simple
    """
