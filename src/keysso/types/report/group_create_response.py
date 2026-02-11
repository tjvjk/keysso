# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GroupCreateResponse"]


class GroupCreateResponse(BaseModel):
    rid: Optional[str] = None
    """Идентификатор отчета"""
