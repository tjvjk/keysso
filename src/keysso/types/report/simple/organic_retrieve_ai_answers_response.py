# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ...._models import BaseModel

__all__ = ["OrganicRetrieveAIAnswersResponse", "Data"]


class Data(BaseModel):
    ai_content: Optional[str] = None
    """Текст ИИ-ответа, где упомянут сайт Возможность фильтровать по полю: `нет`"""

    created_at: Optional[date] = None
    """
    Дата первого обнаружения запроса в ИИ-ответах Возможность фильтровать по полю:
    `да`
    """

    pos: Optional[int] = None
    """
    Позиция сайта в органической выдаче по этому запросу Возможность фильтровать по
    полю: `да`
    """

    source_urls: Optional[List[str]] = None
    """Список URL-адресов источников в ИИ-ответе Возможность фильтровать по полю: `да`"""

    word: Optional[str] = None
    """Ключевая фраза (запрос) Возможность фильтровать по полю: `да`"""

    ws: Optional[int] = None
    """Базовая частотность Возможность фильтровать по полю: `да`"""

    wsk: Optional[int] = None
    """\"!Очень !точная !частотность" Возможность фильтровать по полю: `да`"""


class OrganicRetrieveAIAnswersResponse(BaseModel):
    current_page: Optional[int] = None
    """Текущая страница"""

    data: Optional[List[Data]] = None
    """Данные ответа"""

    last_page: Optional[int] = None
    """Последняя страница"""

    per_page: Optional[int] = None
    """Записей на странице"""

    total: Optional[int] = None
    """Всего записей"""
