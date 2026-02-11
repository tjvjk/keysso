# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ToolDeleteDoubleResponse"]


class ToolDeleteDoubleResponse(BaseModel):
    exclude: Optional[List[str]] = None
    """Ключи, которые были исключены"""

    keys: Optional[List[str]] = None
    """Ключи"""
