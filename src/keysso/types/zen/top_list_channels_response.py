# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TopListChannelsResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Идентификатор канала Возможность фильтровать по полю: `нет`"""

    count_posts: Optional[int] = FieldInfo(alias="countPosts", default=None)
    """Постов Возможность фильтровать по полю: `да`"""

    name: Optional[str] = None
    """Название канала Возможность фильтровать по полю: `да`"""

    subscribers: Optional[int] = None
    """Подписчиков Возможность фильтровать по полю: `да`"""

    url: Optional[str] = None
    """URL канала Возможность фильтровать по полю: `нет`"""

    views: Optional[int] = None
    """Просмотров Возможность фильтровать по полю: `да`"""

    views_rank: Optional[int] = FieldInfo(alias="viewsRank", default=None)
    """По просмотрам рейтинг Возможность фильтровать по полю: `да`"""

    views_till_end: Optional[int] = FieldInfo(alias="viewsTillEnd", default=None)
    """Дочитываний Возможность фильтровать по полю: `да`"""

    views_till_end_rank: Optional[int] = FieldInfo(alias="viewsTillEndRank", default=None)
    """Рейтинг по просмотрам Возможность фильтровать по полю: `да`"""


class TopListChannelsResponse(BaseModel):
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
