# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SimpleRetrieveTopDomainVisibilityResponse", "Data"]


class Data(BaseModel):
    id: Optional[int] = None
    """Идентификатор домена"""

    adcost: Optional[int] = None
    """Оценка бюджета без учета каких-либо таргетингов.

    Произведение точной частотности, на прогноз CTR, на стоимость клика, разделенное
    на 30 дней
    """

    adkeyscnt: Optional[int] = None
    """Количество запросов в контексте"""

    adscnt: Optional[int] = None
    """Количество объявлений в контексте"""

    adtraf: Optional[int] = None
    """Оценка трафика из контекста без учета каких-либо таргетингов.

    Произведение точной частотности, на прогноз CTR, разделенное на 30 дней
    """

    it10: Optional[int] = None
    """Запросов в топ 10"""

    it3: Optional[int] = None
    """Запросов в топ 3"""

    it5: Optional[int] = None
    """Запросов в топ 5"""

    it50: Optional[int] = None
    """Запросов в топ 50"""

    name: Optional[str] = None
    """Домен"""

    pagesinindex: Optional[int] = None
    """Количество страниц сайта, найденных в выдаче"""

    topvis: Optional[int] = None
    """По видимости"""


class SimpleRetrieveTopDomainVisibilityResponse(BaseModel):
    current_page: Optional[int] = None
    """Текущая страница"""

    data: Optional[List[Data]] = None
    """Данные ответа"""

    last_page: Optional[int] = None
    """Последняя страница"""

    per_page: Optional[int] = None
    """Записей на странице"""

    total: Optional[int] = None
    """Всего записей"""
