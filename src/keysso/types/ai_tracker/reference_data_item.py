# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ReferenceDataItem", "Chart"]


class Chart(BaseModel):
    """Динамика упоминаний по датам (ключ — дата, значение — количество)"""

    date: Optional[int] = FieldInfo(alias="<date>", default=None)


class ReferenceDataItem(BaseModel):
    brand: Optional[str] = None
    """Наименование бренда"""

    chart: Optional[Chart] = None
    """Динамика упоминаний по датам (ключ — дата, значение — количество)"""

    delta_percent: Optional[float] = None
    """Дельта процентов видимости в ИИ"""

    diff_empty: Optional[float] = None
    """Дельта без упоминаний"""

    diff_negative: Optional[float] = None
    """Дельта отрицательных"""

    diff_neutral: Optional[float] = None
    """Дельта нейтральных"""

    diff_positive: Optional[float] = None
    """Дельта положительных"""

    diff_reference: Optional[float] = None
    """Дельта упоминаний"""

    diff_total: Optional[float] = None
    """Дельта общего количества возможных упоминаний"""

    empty: Optional[float] = None
    """Без упоминаний"""

    is_competitor: Optional[bool] = None
    """Флаг, указывающий, является ли бренд конкурентом"""

    negative: Optional[float] = None
    """Отрицательных"""

    neutral: Optional[float] = None
    """Нейтральных"""

    percent: Optional[float] = None
    """Процент упоминаний"""

    positive: Optional[float] = None
    """Положительных"""

    total: Optional[float] = None
    """Общее количество возможных упоминаний"""

    total_reference: Optional[float] = None
    """Упоминаний"""

    updated_at: Optional[str] = None
    """Дата последнего обновления"""
