# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SimpleRetrieveDomainAdHistoryResponse", "SimpleRetrieveDomainAdHistoryResponseItem"]


class SimpleRetrieveDomainAdHistoryResponseItem(BaseModel):
    ad_cost: int = FieldInfo(alias="adCost")
    """Стоимость рекламы за период"""

    ad_keys_count: int = FieldInfo(alias="adKeysCount")
    """Количество рекламных ключевых слов"""

    ads_count: int = FieldInfo(alias="adsCount")
    """Количество рекламных объявлений"""

    ad_traf: int = FieldInfo(alias="adTraf")
    """Рекламный трафик"""


SimpleRetrieveDomainAdHistoryResponse: TypeAlias = Dict[str, SimpleRetrieveDomainAdHistoryResponseItem]
