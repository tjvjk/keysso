# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["LinkRetrievePagesResponse", "Data"]


class Data(BaseModel):
    numdomain: Optional[int] = None
    """Доменов"""

    numip: Optional[int] = None
    """IP-адресов"""

    numlink: Optional[int] = None
    """Ссылок"""

    numurl: Optional[int] = None
    """Страниц"""

    url: Optional[str] = None
    """URL"""


class LinkRetrievePagesResponse(BaseModel):
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
