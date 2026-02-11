# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ToolCheckTopConcurentsDomainsResponse", "Data"]


class Data(BaseModel):
    cnt: Optional[int] = None
    """Количество запросов"""

    did: Optional[int] = None
    """Идентификатор домена"""

    name: Optional[str] = None
    """Домен"""


class ToolCheckTopConcurentsDomainsResponse(BaseModel):
    data: Optional[List[Data]] = None
    """Массив объектов данных по сайтам"""

    total: Optional[int] = None
    """Общее количество доменов"""
