# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ZenRetrieveDashboardParams"]


class ZenRetrieveDashboardParams(TypedDict, total=False):
    channel: Required[str]
    """Имя или урл канала"""
