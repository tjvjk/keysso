# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WordstatGetProjectsCompletedResponse", "Data"]


class Data(BaseModel):
    id: Optional[int] = None
    """Идентификатор проекта"""

    base: Optional[int] = None
    """[ID региона для Вордстат](https://yandex.ru/dev/xml/doc/ru/reference/regions)"""

    batches: Optional[int] = None
    """Выполнившихся частей для парсинга"""

    batches_total: Optional[int] = None
    """Всего частей для парсинга"""

    created_at: Optional[str] = None
    """Дата создания проекта"""

    name: Optional[str] = None
    """Именование проекта"""

    swsk_sum: Optional[int] = None
    """Сумма "[!WS]" """

    updated_at: Optional[str] = None
    """Дата последнего обновления проекта"""

    words_count: Optional[int] = None
    """Фраз в проекте"""

    ws_sum: Optional[int] = None
    """Сумма "WS" """


class WordstatGetProjectsCompletedResponse(BaseModel):
    current_page: Optional[int] = None
    """Текущая страница"""

    data: Optional[List[Data]] = None
    """Данные ответа"""

    last_page: Optional[int] = None
    """Последняя страница"""

    per_page: Optional[int] = None
    """Записей на странице"""

    total: Optional[int] = None
    """Всего записей"""
