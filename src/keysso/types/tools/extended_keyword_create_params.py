# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..report.base import Base

__all__ = ["ExtendedKeywordCreateParams", "Config"]


class ExtendedKeywordCreateParams(TypedDict, total=False):
    list: Required[SequenceNotStr[str]]
    """Массив фраз"""

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

    config: Config
    """Массив фраз"""


class Config(TypedDict, total=False):
    """Массив фраз"""

    additions: bool
    """Добавить "хвосты" исходных фраз"""

    delete_duplicate: Annotated[bool, PropertyInfo(alias="deleteDuplicate")]
    """Без повторов"""

    similarity: int
    """Похожесть (от 5 до 100, шаг 1)"""
