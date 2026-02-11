# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CompetitorListResponse",
    "CompetitorListResponseItem",
    "CompetitorListResponseItemProperty",
    "CompetitorListResponseItemPropertyChecked",
    "CompetitorListResponseItemPropertyColors",
    "CompetitorListResponseItemPropertyDomain",
    "CompetitorListResponseItemPropertyGData",
    "CompetitorListResponseItemPropertyGDataDomainID",
    "CompetitorListResponseItemPropertyLinks",
    "CompetitorListResponseItemPropertyLinksDomainID",
]


class CompetitorListResponseItemPropertyChecked(BaseModel):
    """Включение/выключения домена на графике соответствующего параметра"""

    domain_id: Optional[bool] = FieldInfo(alias="<domainID>", default=None)


class CompetitorListResponseItemPropertyColors(BaseModel):
    """Цвет домена на графике"""

    domain_id: Optional[str] = FieldInfo(alias="<domainID>", default=None)


class CompetitorListResponseItemPropertyDomain(BaseModel):
    did: Optional[int] = None
    """Идентификатор домена"""

    main: Optional[bool] = None
    """Признак, что домен основной, а не поддомен"""

    name: Optional[str] = None
    """Имя домена"""


class CompetitorListResponseItemPropertyGDataDomainID(BaseModel):
    yyyy_mm: Optional[int] = FieldInfo(alias="<YYYY:MM>", default=None)


class CompetitorListResponseItemPropertyGData(BaseModel):
    """Информация для графика разбитая по доменам, а внутри по месяцам"""

    domain_id: Optional[CompetitorListResponseItemPropertyGDataDomainID] = FieldInfo(alias="<domainID>", default=None)


class CompetitorListResponseItemPropertyLinksDomainID(BaseModel):
    yyyy_mm: Optional[str] = FieldInfo(alias="<YYYY:MM>", default=None)


class CompetitorListResponseItemPropertyLinks(BaseModel):
    """Ссылки на дашборды конкурентов"""

    domain_id: Optional[CompetitorListResponseItemPropertyLinksDomainID] = FieldInfo(alias="<domainID>", default=None)


class CompetitorListResponseItemProperty(BaseModel):
    """Возвращается массив свойств.

    Структура у каждого из свойств одинаковая.<br> `vis` - Оценка трафика с поиска<br> `it50` - Запросов в топ 50<br> `it10`- Запросов в топ 10<br> `it3` - Запросов в топ 3<br> `pagesInIndex` - Количество страниц сайта, найденных в выдаче<br> `adTraf` - Трафик в сутки(контекст)<br> `adKeysCount` - Запросов в контексте<br> `adsCount` - Трафик в сутки(органика)<br> `adCost` - Бюджет<br> `rsyAdsCount` - Объявления РСЯ<br> `backlinksCount` - Входящие ссылки<br> `outlinksCount` - Исходящие ссылки<br> `uniqBackdomainsCount` - Ссылающиеся домены<br> `uniqBackipsCount` - Ссылки по IP<br> `dr` - DR<br> `compare` - Сравнение
    """

    checked: Optional[CompetitorListResponseItemPropertyChecked] = None
    """Включение/выключения домена на графике соответствующего параметра"""

    colors: Optional[CompetitorListResponseItemPropertyColors] = None
    """Цвет домена на графике"""

    domains: Optional[List[CompetitorListResponseItemPropertyDomain]] = None
    """Информация по домену конкуренту"""

    g_data: Optional[CompetitorListResponseItemPropertyGData] = FieldInfo(alias="gData", default=None)
    """Информация для графика разбитая по доменам, а внутри по месяцам"""

    links: Optional[CompetitorListResponseItemPropertyLinks] = None
    """Ссылки на дашборды конкурентов"""

    name: Optional[str] = None
    """Название свойства"""

    show_property: Optional[bool] = FieldInfo(alias="showProperty", default=None)
    """Признак показа свойства"""

    views: Optional[List[str]] = None
    """Отображать в органике, контексте."""

    x_axis: Optional[List[str]] = FieldInfo(alias="xAxis", default=None)
    """Интервал для горизонтальной оси графика"""


class CompetitorListResponseItem(BaseModel):
    property: Optional[CompetitorListResponseItemProperty] = FieldInfo(alias="<property>", default=None)
    """Возвращается массив свойств.

    Структура у каждого из свойств одинаковая. `vis` - Оценка трафика с поиска
    `it50` - Запросов в топ 50 `it10`- Запросов в топ 10 `it3` - Запросов в топ 3
    `pagesInIndex` - Количество страниц сайта, найденных в выдаче `adTraf` - Трафик
    в сутки(контекст) `adKeysCount` - Запросов в контексте `adsCount` - Трафик в
    сутки(органика) `adCost` - Бюджет `rsyAdsCount` - Объявления РСЯ
    `backlinksCount` - Входящие ссылки `outlinksCount` - Исходящие ссылки
    `uniqBackdomainsCount` - Ссылающиеся домены `uniqBackipsCount` - Ссылки по IP
    `dr` - DR `compare` - Сравнение
    """


CompetitorListResponse: TypeAlias = List[CompetitorListResponseItem]
