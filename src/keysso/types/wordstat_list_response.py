# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WordstatListResponse", "Data"]


class Data(BaseModel):
    id: Optional[int] = None
    """Идентификатор проекта"""

    base: Optional[int] = None
    """[ID региона для Яндекс](https://yandex.ru/dev/xml/doc/ru/reference/regions)"""

    batches: Optional[int] = None
    """Выполнившихся частей для парсинга"""

    batches_total: Optional[int] = None
    """Всего частей для парсинга"""

    cluster_name: Optional[str] = None
    """Название родительского проекта кластеризатора"""

    cluster_uid: Optional[str] = None
    """UID родительского проекта кластеризатора"""

    created_at: Optional[str] = None
    """Дата создания проекта"""

    monitoring_id: Optional[int] = None
    """ID родительского проекта мониторинга"""

    monitoring_name: Optional[str] = None
    """Название родительского проекта мониторинга"""

    name: Optional[str] = None
    """Название проекта"""

    source: Optional[int] = None
    """Источник `0` - Wordstat, `1` - Direct"""

    swsk_sum: Optional[int] = None
    """Сумма "[!WS]" """

    updated_at: Optional[str] = None
    """Дата последнего обновления проекта"""

    words_count: Optional[int] = None
    """Фраз в проекте"""

    ws_sum: Optional[int] = None
    """Сумма "WS" """


class WordstatListResponse(BaseModel):
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
