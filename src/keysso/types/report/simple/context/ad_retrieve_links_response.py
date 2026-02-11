# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["AdRetrieveLinksResponse", "Data"]


class Data(BaseModel):
    links: Optional[List[str]] = None
    """Уникальные ссылки Возможность фильтровать по полю: `да`"""


class AdRetrieveLinksResponse(BaseModel):
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
