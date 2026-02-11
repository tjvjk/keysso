# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RobotRetrieveDataParams"]


class RobotRetrieveDataParams(TypedDict, total=False):
    domain: Required[str]
    """Имя домена"""

    date: str
    """Дата изменения, если не указана - последнее изменение"""
