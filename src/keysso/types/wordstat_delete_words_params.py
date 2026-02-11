# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WordstatDeleteWordsParams", "Data"]


class WordstatDeleteWordsParams(TypedDict, total=False):
    data: Required[Data]
    """Данные для парсинга"""


class Data(TypedDict, total=False):
    """Данные для парсинга"""

    project_id: Annotated[int, PropertyInfo(alias="projectId")]
    """Идентификатор проекта"""

    words: SequenceNotStr[str]
    """Список фраз"""
