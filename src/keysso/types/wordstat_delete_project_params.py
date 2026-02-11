# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WordstatDeleteProjectParams", "Data"]


class WordstatDeleteProjectParams(TypedDict, total=False):
    data: Required[Data]
    """Данные"""


class Data(TypedDict, total=False):
    """Данные"""

    project_id: Annotated[int, PropertyInfo(alias="projectId")]
    """Идентификатор проекта"""
