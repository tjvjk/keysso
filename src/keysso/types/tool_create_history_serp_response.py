# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolCreateHistorySerpResponse", "YyyyMm"]


class YyyyMm(BaseModel):
    """Год и месяц с информацией по выдаче"""

    did: Optional[int] = None
    """Идентификатор домена."""

    domain: Optional[str] = None
    """Адрес сайта"""

    pos: Optional[int] = None
    """Позиция в выдаче"""

    url: Optional[str] = None
    """Страница, представленная в выдаче"""


class ToolCreateHistorySerpResponse(BaseModel):
    yyyy_mm: Optional[YyyyMm] = FieldInfo(alias="<YYYY.MM>", default=None)
    """Год и месяц с информацией по выдаче"""
