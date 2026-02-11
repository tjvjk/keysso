# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ToolSuggestResponse"]


class ToolSuggestResponse(BaseModel):
    link: Optional[str] = None
    """Ссылка на скачивание файла с подсказками"""
