# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .system_item import SystemItem
from .ai_tracker.reference_data_item import ReferenceDataItem

__all__ = ["AITrackerListResponse", "Data"]


class Data(BaseModel):
    id: Optional[int] = None
    """Идентификатор проекта"""

    brand: Optional[str] = None
    """Наименование бренда"""

    created_at: Optional[str] = None
    """Дата создания проекта"""

    in_progress: Optional[bool] = None
    """Статус проекта"""

    name: Optional[str] = None
    """Название проекта"""

    next_start_at: Optional[str] = None
    """Дата следующего запуска проекта"""

    reference_data: Optional[List[ReferenceDataItem]] = FieldInfo(alias="referenceData", default=None)
    """Справочная информация по брендам"""

    systems: Optional[List[SystemItem]] = None
    """
    Массив идентификаторов систем ИИ: `1` - GigaChat `3` - DeepSeek `6` - OpenAI
    `7` - Grok
    """


class AITrackerListResponse(BaseModel):
    current_page: Optional[int] = None
    """Порядковый номер страницы результатов"""

    data: Optional[List[Data]] = None
    """Данные ответа"""

    last_page: Optional[int] = None
    """Последняя страница"""

    per_page: Optional[int] = None
    """Количество результатов на одной странице"""

    total: Optional[int] = None
    """Всего записей"""
