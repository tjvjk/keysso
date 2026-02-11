# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .engine import Engine
from .._utils import PropertyInfo

__all__ = ["SearchSettingParam"]


class SearchSettingParam(TypedDict, total=False):
    engine: Required[Engine]
    """
    Идентификатор поисковой системы: `0` - Яндекс (десктоп) `1` - Яндекс (мобильный)
    `3` - Google (мобильный) `4` - Google (десктоп)
    """

    region_id: Required[Annotated[int, PropertyInfo(alias="regionId")]]
    """
    [ID региона для Яндекс](https://yandex.ru/dev/xml/doc/ru/reference/regions) или
    [ID региона для Google](https://analyticscodes.com/)
    """
