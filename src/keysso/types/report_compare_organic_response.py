# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ReportCompareOrganicResponse", "Data"]


class Data(BaseModel):
    adscnt: Optional[int] = None
    """Количество объявлений в контексте"""

    avbid: Optional[int] = None
    """Средняя цена клика"""

    docs: Optional[int] = None
    """Количество документов в выдаче"""

    isgeo: Optional[int] = None
    """Является топонимом"""

    isquest: Optional[int] = None
    """Является вопросом"""

    numwords: Optional[int] = None
    """Количество слов в запросе"""

    serpf: Optional[str] = None
    """Дата изменения выдачи SERP"""

    superwsk: Optional[int] = None
    """\"[!Супер !точная !частотность]" """

    word: Optional[str] = None
    """Ключевая фраза"""

    ws: Optional[int] = None
    """Базовая частотность"""

    wsk: Optional[int] = None
    """\"!Очень !точная !частотность" """


class ReportCompareOrganicResponse(BaseModel):
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
