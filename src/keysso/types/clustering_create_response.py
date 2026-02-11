# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ClusteringCreateResponse", "Skipped"]


class Skipped(BaseModel):
    phrase: Optional[str] = None
    """Фраза"""

    reason: Optional[str] = None
    """Причина пропуска фразы"""


class ClusteringCreateResponse(BaseModel):
    skipped: Optional[List[Skipped]] = None
    """
    Фразы, которые не прошли проверку (присутствует в ответе только в случае, если
    были пропущены фразы)
    """

    skipped_count: Optional[int] = None
    """
    Количество пропущенных фраз (присутствует в ответе только в случае, если были
    пропущены фразы)
    """

    uid: Optional[str] = None
    """Идентификатор отчета"""
