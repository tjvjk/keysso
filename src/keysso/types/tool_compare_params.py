# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ToolCompareParams"]


class ToolCompareParams(TypedDict, total=False):
    left: Required[SequenceNotStr[str]]
    """Список поисковых фраз"""

    options: Required[Literal["present_right", "uniq", "union", "present_left"]]
    """Тип сравнения"""

    right: Required[SequenceNotStr[str]]
    """Список поисковых фраз"""
