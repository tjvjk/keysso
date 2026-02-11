# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AITrackerGetStateResponse"]


class AITrackerGetStateResponse(BaseModel):
    project_id: Optional[int] = FieldInfo(alias="<projectId>", default=None)
    """
    Где ключ — ID проекта, а значение — прогресс выполнения (в процентах). Например:
    `"21": 0`
    """
