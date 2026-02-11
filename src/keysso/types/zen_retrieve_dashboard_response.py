# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ZenRetrieveDashboardResponse", "ParsedAt"]


class ParsedAt(BaseModel):
    """Дата парсинга"""

    date: Optional[str] = None
    """Дата парсинга"""

    timezone: Optional[str] = None
    """Таймзона"""

    timezone_type: Optional[int] = None
    """Тип таймзоны"""


class ZenRetrieveDashboardResponse(BaseModel):
    count_posts: Optional[int] = FieldInfo(alias="countPosts", default=None)
    """Количество постов"""

    count_till_end: Optional[int] = FieldInfo(alias="countTillEnd", default=None)
    """Дочитываний"""

    count_till_end_rank: Optional[int] = FieldInfo(alias="countTillEndRank", default=None)
    """По дочитываниям рейтинг"""

    count_views: Optional[int] = FieldInfo(alias="countViews", default=None)
    """Количество просмотров"""

    count_views_rank: Optional[int] = FieldInfo(alias="countViewsRank", default=None)
    """По просмотрам рейтинг"""

    description: Optional[str] = None
    """Описание канала"""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)
    """Активность канала"""

    logo: Optional[str] = None
    """Логотип канала"""

    name: Optional[str] = None
    """Имя канала"""

    parsed_at: Optional[ParsedAt] = FieldInfo(alias="parsedAt", default=None)
    """Дата парсинга"""

    subscribers: Optional[int] = None
    """Подписчики"""

    url: Optional[str] = None
    """Урл канала"""
