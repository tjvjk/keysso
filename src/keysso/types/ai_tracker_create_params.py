# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .system_item import SystemItem

__all__ = ["AITrackerCreateParams", "Prompt"]


class AITrackerCreateParams(TypedDict, total=False):
    brand: Required[str]
    """Название бренда"""

    description: Required[SequenceNotStr[str]]
    """Вид деятельности, чем занимается"""

    systems: Required[Iterable[SystemItem]]
    """
    Массив идентификаторов систем ИИ: `1` - GigaChat `3` - DeepSeek `6` - OpenAI
    `7` - Grok
    """

    competitors: SequenceNotStr[str]
    """Список конкурентов (названия брендов)"""

    prompts: Iterable[Prompt]
    """
    Список промтов для генерации запросов Каждый элемент может содержать фразу и
    необязательные группы.
    """

    start: bool
    """Флаг автозапуска проекта после создания"""

    synonyms: SequenceNotStr[str]
    """Синонимы бренда, варианты написания"""


class Prompt(TypedDict, total=False):
    groups: SequenceNotStr[str]
    """Необязательные группы промта"""

    prompt: str
    """Текст промта"""
