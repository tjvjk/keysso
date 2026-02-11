# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .report.base import Base
from .clustering.items import Items
from .search_setting_param import SearchSettingParam

__all__ = ["MonitoringCreateParams"]


class MonitoringCreateParams(TypedDict, total=False):
    search_settings: Required[Annotated[Iterable[SearchSettingParam], PropertyInfo(alias="searchSettings")]]
    """Список настроек поисковых систем и регионов"""

    tracking_item: Required[Annotated[str, PropertyInfo(alias="trackingItem")]]
    """Элемент отслеживания (домен/url)"""

    track_sub_domains: Required[Annotated[bool, PropertyInfo(alias="trackSubDomains")]]
    """Флаг отслеживания поддоменов"""

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

    cluster_uuid: Annotated[str, PropertyInfo(alias="clusterUuid")]
    """Уникальный идентификатор кластеризатора"""

    keywords: SequenceNotStr[str]
    """Список фраз"""

    name: str
    """Название проекта"""

    serp: bool
    """Флаг для включения SERP"""

    wordstat: bool
    """Флаг для включения статистики слов"""

    ws_types: Iterable[Items]
    """Типы частотности: `0` - Wordstat `1` - "!Wordstat" `2` - "[!Wordstat]" """
