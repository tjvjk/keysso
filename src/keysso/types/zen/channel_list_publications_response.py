# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ChannelListPublicationsResponse", "Data", "DataDatePublishAt"]


class DataDatePublishAt(BaseModel):
    """Дата публикации<br>Возможность фильтровать по полю: `да`"""

    date: Optional[str] = None
    """Дата"""

    timezone: Optional[str] = None
    """Таймзона"""

    timezone_type: Optional[int] = None
    """Тип таймзоны"""


class Data(BaseModel):
    canonical_url: Optional[str] = FieldInfo(alias="canonicalUrl", default=None)
    """Каноничный URL Возможность фильтровать по полю: `нет`"""

    count_comments: Optional[int] = FieldInfo(alias="countComments", default=None)
    """Подписчиков Возможность фильтровать по полю: `да`"""

    count_likes: Optional[int] = FieldInfo(alias="countLikes", default=None)
    """Лайков Возможность фильтровать по полю: `да`"""

    count_views: Optional[int] = FieldInfo(alias="countViews", default=None)
    """Комментариев Возможность фильтровать по полю: `да`"""

    count_views_till_end: Optional[int] = FieldInfo(alias="countViewsTillEnd", default=None)
    """Дочитываний Возможность фильтровать по полю: `да`"""

    date_publish_at: Optional[DataDatePublishAt] = FieldInfo(alias="datePublishAt", default=None)
    """Дата публикации Возможность фильтровать по полю: `да`"""

    description: Optional[str] = None
    """Название публикации Возможность фильтровать по полю: `да`"""

    title: Optional[str] = None
    """Подписчиков Возможность фильтровать по полю: `да`"""

    type_label: Optional[str] = FieldInfo(alias="typeLabel", default=None)
    """Тип контента Возможность фильтровать по полю: `да`"""

    url: Optional[str] = None
    """URL канала Возможность фильтровать по полю: `нет`"""


class ChannelListPublicationsResponse(BaseModel):
    current_page: Optional[int] = None
    """Текущая страница"""

    data: Optional[List[Data]] = None
    """Данные ответа"""

    last_page: Optional[int] = None
    """Последняя страница"""

    per_page: Optional[int] = None
    """Записей на странице"""

    sort: Optional[List[object]] = None

    total: Optional[int] = None
    """Всего записей"""
