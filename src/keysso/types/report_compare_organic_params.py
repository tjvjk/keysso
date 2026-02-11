# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .report.base import Base

__all__ = ["ReportCompareOrganicParams"]


class ReportCompareOrganicParams(TypedDict, total=False):
    excl: Required[str]
    """Список доменов через запятую"""

    incl: Required[str]
    """Список доменов через запятую"""

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

    page: int
    """Порядковый номер страницы результатов"""

    per_page: int
    """Количество результатов на одной странице"""

    sort: str
    """Сортировка данных по полям.

    Формат: `field|direction`, где

    `field` - имя колонки `direction` - направление сортировки, asc - по
    возрастанию, desc - по убыванию

    Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`
    """

    view: Literal["organic", "context", "backlinks"]
    """Тип отчета `organic`"""
