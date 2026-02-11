# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolCheckTopConcurentsURLsResponse", "Data"]


class Data(BaseModel):
    cnt: Optional[int] = None
    """Количество запросов"""

    did: Optional[int] = None
    """Идентификатор домена"""

    full_url: Optional[str] = FieldInfo(alias="fullUrl", default=None)
    """Полный url страницы"""

    name: Optional[str] = None
    """Домен"""

    url: Optional[str] = None
    """url страницы"""


class ToolCheckTopConcurentsURLsResponse(BaseModel):
    data: Optional[List[Data]] = None
    """Массив объектов данных по страницам"""

    total: Optional[int] = None
    """Общее количество страниц"""
