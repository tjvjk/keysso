# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RobotListDatesResponse", "RobotListDatesResponseItem"]


class RobotListDatesResponseItem(BaseModel):
    first_update: Optional[str] = FieldInfo(alias="firstUpdate", default=None)
    """Дата первого обновления"""

    last_update: Optional[str] = FieldInfo(alias="lastUpdate", default=None)
    """Дата последней проверки, файл без изменений"""

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)
    """Код ответа"""


RobotListDatesResponse: TypeAlias = List[RobotListDatesResponseItem]
