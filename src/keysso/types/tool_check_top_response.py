# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolCheckTopResponse", "Keyword", "KeywordCount"]


class KeywordCount(BaseModel):
    """Всегда нулевые данные, используются на стороне фронта"""

    domain: Optional[int] = None

    url: Optional[int] = None


class Keyword(BaseModel):
    count: Optional[KeywordCount] = None
    """Всегда нулевые данные, используются на стороне фронта"""

    domain: Optional[str] = None
    """Адрес сайта"""

    pos: Optional[int] = None

    url: Optional[str] = None
    """Адрес страницы сайта"""


class ToolCheckTopResponse(BaseModel):
    keyword: Optional[List[Keyword]] = FieldInfo(alias="<keyword>", default=None)
    """Список ключевых фраз"""
