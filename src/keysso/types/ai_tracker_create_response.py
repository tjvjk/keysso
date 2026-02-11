# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .system_item import SystemItem
from .alert_setting import AlertSetting

__all__ = ["AITrackerCreateResponse", "SchedulerSetting"]


class SchedulerSetting(BaseModel):
    check_hour: Optional[Literal[0]] = FieldInfo(alias="checkHour", default=None)
    """Час проверки (фиксированное значение 0)"""

    check_minute: Optional[Literal[0]] = FieldInfo(alias="checkMinute", default=None)
    """Минуты проверки (фиксированное значение 0)"""

    days_of_month: Optional[List[object]] = FieldInfo(alias="daysOfMonth", default=None)
    """Дни месяца для проверки (фиксированное значение null)"""

    days_of_week: Optional[List[object]] = FieldInfo(alias="daysOfWeek", default=None)
    """Дни недели для проверки (фиксированное значение null)"""

    type: Optional[Literal[0]] = None
    """Тип настройки (фиксированное значение 0)"""


class AITrackerCreateResponse(BaseModel):
    id: Optional[int] = None
    """Идентификатор созданного проекта"""

    alert_setting: Optional[AlertSetting] = FieldInfo(alias="alertSetting", default=None)
    """Настройки уведомлений"""

    brand: Optional[str] = None
    """Название бренда"""

    in_progress: Optional[bool] = FieldInfo(alias="inProgress", default=None)
    """Статус проекта"""

    name: Optional[str] = None
    """Название бренда"""

    next_start_at: Optional[datetime] = None
    """Дата следующего запуска проекта"""

    prompts: Optional[List[object]] = None

    reference_data: Optional[List[object]] = FieldInfo(alias="referenceData", default=None)

    scheduler_setting: Optional[SchedulerSetting] = FieldInfo(alias="schedulerSetting", default=None)

    systems: Optional[List[SystemItem]] = None
    """
    Массив идентификаторов систем ИИ: `1` - GigaChat `3` - DeepSeek `6` - OpenAI
    `7` - Grok
    """
