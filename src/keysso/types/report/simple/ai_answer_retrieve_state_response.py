# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["AIAnswerRetrieveStateResponse"]


class AIAnswerRetrieveStateResponse(BaseModel):
    ai_state: Optional[int] = None
    """
    Статус построения ИИ-отчёта Возможные значения: `0` - Не создан `10` - Создан,
    ожидает построения `20` - Строится `30` - Ошибка построения `40` - Готов
    """

    base: Optional[str] = None
    """База данных (регион)"""

    domain: Optional[str] = None
    """Имя домена"""
