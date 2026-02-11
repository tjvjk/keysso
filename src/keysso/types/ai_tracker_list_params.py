# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AITrackerListParams"]


class AITrackerListParams(TypedDict, total=False):
    page: int
    """Порядковый номер страницы результатов"""

    per_page: int
    """Количество результатов на одной странице"""

    search: str
    """Поиск по названию проекта или бренду"""
