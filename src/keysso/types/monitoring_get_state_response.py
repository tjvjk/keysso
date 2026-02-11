# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MonitoringGetStateResponse", "ProjectID", "ProjectIDDetail"]


class ProjectIDDetail(BaseModel):
    name: Optional[str] = None
    """Название проекта"""

    progress: Optional[int] = None
    """Прогресс конкретного проекта"""

    type: Optional[Literal["serp", "ws"]] = None
    """Тип проекта (может быть "serp" или "ws")"""


class ProjectID(BaseModel):
    """ID проекта"""

    details: Optional[List[ProjectIDDetail]] = None

    progress: Optional[int] = None
    """Прогресс проекта, берется по минимальному значению details.progress"""


class MonitoringGetStateResponse(BaseModel):
    project_id: Optional[ProjectID] = FieldInfo(alias="<projectId>", default=None)
    """ID проекта"""
