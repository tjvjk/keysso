# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..report.base import Base

__all__ = ["DictionaryExtByPageCreateParams", "Config"]


class DictionaryExtByPageCreateParams(TypedDict, total=False):
    config: Required[Config]
    """Настройки"""

    url: Required[str]
    """URL исходной страницы"""

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


class Config(TypedDict, total=False):
    """Настройки"""

    list: SequenceNotStr[str]
    """Список поисковых фраз"""

    more: bool
    """Глубокий анализ"""

    pages: SequenceNotStr[str]
    """Список страниц конкурентов"""

    use_list: Annotated[bool, PropertyInfo(alias="useList")]
    """Использовать свой список ключевых фраз"""

    use_pages: Annotated[bool, PropertyInfo(alias="usePages")]
    """Добавить свой список страниц конкурентов"""
