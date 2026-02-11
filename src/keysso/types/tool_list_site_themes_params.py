# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .report.base import Base

__all__ = ["ToolListSiteThemesParams"]


class ToolListSiteThemesParams(TypedDict, total=False):
    site: Required[str]

    base: Base
    """
    Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
    `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
    Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
    Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
    `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
    Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
    `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
    Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
    Минск `tom` - Яндекс: Томск `gny` - Google: New York
    """

    filter: str
    """
    Подробнее про фильтрацию смотрите в разделе
    [Фильтрация данных](#tag/Filtraciya-dannyh)
    """

    like: str
    """Похож"""

    max_pos: Annotated[int, PropertyInfo(alias="maxPos")]
    """Позиция до"""

    max_ws: Annotated[int, PropertyInfo(alias="maxWs")]
    """Частотность не более"""

    max_wsk: Annotated[int, PropertyInfo(alias="maxWsk")]
    """[!Частотность] не более"""

    min_pos: Annotated[int, PropertyInfo(alias="minPos")]
    """Позиция от"""

    min_ws: Annotated[int, PropertyInfo(alias="minWs")]
    """Частотность не менее"""

    min_wsk: Annotated[int, PropertyInfo(alias="minWsk")]
    """[!Частотность] не менее"""

    not_like: Annotated[str, PropertyInfo(alias="notLike")]
    """Не похож"""

    page: int
    """Порядковый номер страницы результатов"""

    per_page: int
    """Количество результатов на одной странице"""

    qby_url: Annotated[int, PropertyInfo(alias="qbyUrl")]
    """Запросов с одной страницы"""

    sort: str
    """Сортировка данных по полям.

    Формат: `field|direction`, где

    `field` - имя колонки `direction` - направление сортировки, asc - по
    возрастанию, desc - по убыванию

    Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`
    """

    words: str
    """Частотность не более"""
