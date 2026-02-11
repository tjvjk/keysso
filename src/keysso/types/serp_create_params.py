# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .engine import Engine
from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SerpCreateParams", "Data"]


class SerpCreateParams(TypedDict, total=False):
    data: Required[Data]
    """Данные для парсинга"""


class Data(TypedDict, total=False):
    """Данные для парсинга"""

    name: str
    """Имя проекта"""

    region_id: Annotated[int, PropertyInfo(alias="regionId")]
    """
    [ID региона для Яндекс](https://yandex.ru/dev/xml/doc/ru/reference/regions) или
    [ID региона для Google](https://analyticscodes.com/)
    """

    search_engine: Annotated[Engine, PropertyInfo(alias="searchEngine")]
    """
    Идентификатор поисковой системы: `0` - Яндекс (десктоп) `1` - Яндекс (мобильный)
    `3` - Google (мобильный) `4` - Google (десктоп)
    """

    top_number: Annotated[int, PropertyInfo(alias="topNumber")]
    """Глубина выдачи (10, 20, 50)"""

    words: SequenceNotStr[str]
    """Список фраз"""
