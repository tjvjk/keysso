# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ToolDeleteDoubleParams"]


class ToolDeleteDoubleParams(TypedDict, total=False):
    list: Required[Iterable[object]]
    """Массив фраз для чистки дублей"""
