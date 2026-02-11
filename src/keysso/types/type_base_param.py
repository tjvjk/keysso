# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["TypeBaseParam"]


class TypeBaseParam(TypedDict, total=False):
    name: str
    """Имя проекта"""

    region_id: Annotated[int, PropertyInfo(alias="regionId")]
    """[ID региона для Яндекс](https://yandex.ru/dev/xml/doc/ru/reference/regions)"""

    words: SequenceNotStr[str]
    """Список фраз"""
