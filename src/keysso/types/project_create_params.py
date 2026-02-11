# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ProjectCreateParams"]


class ProjectCreateParams(TypedDict, total=False):
    domain: Required[str]
    """Адрес сайта"""

    competitors: SequenceNotStr[str]
    """Конкуренты"""

    name: str
    """Название проекта"""
