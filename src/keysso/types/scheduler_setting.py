# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SchedulerSetting"]


class SchedulerSetting(BaseModel):
    """Настройки планировщика"""

    check_hour: Optional[int] = FieldInfo(alias="checkHour", default=None)
    """Час для проверки"""

    check_minute: Optional[int] = FieldInfo(alias="checkMinute", default=None)
    """Минута для проверки"""

    days_of_month: Optional[List[int]] = FieldInfo(alias="daysOfMonth", default=None)
    """Дни месяца для планировщика"""

    days_of_week: Optional[str] = FieldInfo(alias="daysOfWeek", default=None)
    """
    Дни недели для планировщика, представленные числами от 1 до 7 (1 — Понедельник,
    7 — Воскресенье)
    """

    type: Optional[int] = None
    """Тип планировщика"""
