# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ToolCreateUniqueParams"]


class ToolCreateUniqueParams(TypedDict, total=False):
    list: Required[SequenceNotStr[str]]
    """Список поисковых фраз"""
