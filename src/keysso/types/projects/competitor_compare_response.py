# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CompetitorCompareResponse", "DomainData", "Join"]


class DomainData(BaseModel):
    id: Optional[int] = None
    """Идентификатор ключа"""

    adcost: Optional[int] = None
    """Оценка бюджета без учета каких-либо таргетингов.

    Произведение точной частотности, на прогноз CTR, на стоимость клика, разделенное
    на 30 дней. Только для `view=context`
    """

    adkeyscnt: Optional[int] = None
    """Количество запросов в контексте. Только для `view=context`"""

    adscnt: Optional[int] = None
    """Количество объявлений в контексте. Только для `view=context`"""

    ad_traf: Optional[int] = FieldInfo(alias="adTraf", default=None)
    """Трафик в сутки(контекст). Только для `view=context`"""

    it1: Optional[int] = None
    """Запросов в топ 1. Только для `view=organic`"""

    it10: Optional[int] = None
    """Запросов в топ 10. Только для `view=organic`"""

    it5: Optional[int] = None
    """Запросов в топ 5. Только для `view=organic`"""

    it50: Optional[int] = None
    """Запросов в топ 50. Только для `view=organic`"""

    name: Optional[str] = None
    """Имя домена"""


class Join(BaseModel):
    sets: Optional[List[int]] = None
    """Домены в сравнении"""

    size: Optional[str] = None
    """Кол-во уникальных фраз"""


class CompetitorCompareResponse(BaseModel):
    domain_data: Optional[List[DomainData]] = FieldInfo(alias="domainData", default=None)
    """Данные по доменам"""

    joins: Optional[List[Join]] = None
    """Сравнения"""
