# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RobotRetrieveDataResponse"]


class RobotRetrieveDataResponse(BaseModel):
    content: Optional[str] = None
    """Содержимое файла"""

    date_update: Optional[str] = FieldInfo(alias="dateUpdate", default=None)
    """Дата изменения файла"""

    error: Optional[str] = None
    """Текст ошибки при запросе файла"""

    robots_lines: Optional[int] = FieldInfo(alias="robotsLines", default=None)
    """Строк в файле"""

    robots_size: Optional[int] = FieldInfo(alias="robotsSize", default=None)
    """Размер файла, в байтах"""

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)
    """Код ответа"""
