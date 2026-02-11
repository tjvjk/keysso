# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ToolCreateUniqueResponse"]


class ToolCreateUniqueResponse(BaseModel):
    count: Optional[int] = None
    """Кол-во вхождений"""

    keys: Optional[List[str]] = None
    """Ключевые фразы"""

    open: Optional[bool] = None

    words: Optional[List[str]] = None
    """Словоформы"""
