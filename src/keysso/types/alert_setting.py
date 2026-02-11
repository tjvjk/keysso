# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AlertSetting"]


class AlertSetting(BaseModel):
    """Настройки уведомлений"""

    active: Optional[bool] = None
    """Флаг активации уведомлений"""

    notify_email: Optional[bool] = FieldInfo(alias="notifyEmail", default=None)
    """Флаг отправки уведомлений по email"""

    notify_telegram: Optional[bool] = FieldInfo(alias="notifyTelegram", default=None)
    """Флаг отправки уведомлений в Telegram"""
