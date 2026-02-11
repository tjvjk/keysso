# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["KeywordsByListCreateResponse"]


class KeywordsByListCreateResponse(BaseModel):
    uid: Optional[str] = None
    """Идентификатор отчета"""
