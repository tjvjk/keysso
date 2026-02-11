# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CompetitorCompareParams"]


class CompetitorCompareParams(TypedDict, total=False):
    domains: Required[SequenceNotStr[str]]
    """Конкуренты"""

    view: Required[Literal["organic", "context"]]
    """Отчет вернет результаты для органики(`organic`) или контекста(`context`)"""

    type: int
