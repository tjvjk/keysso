# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ToolListSiteThemesResponse", "Data"]


class Data(BaseModel):
    adscnt: Optional[int] = None
    """Количество объявлений в контексте"""

    avbid: Optional[int] = None
    """Средняя цена клика Возможность фильтровать по полю: `да`"""

    cnt: Optional[int] = None
    """Общих ключей в топ 50 Возможность фильтровать по полю: `да`"""

    docs: Optional[int] = None
    """Количество документов в выдаче Возможность фильтровать по полю: `да`"""

    isgeo: Optional[int] = None
    """Является топонимом Возможность фильтровать по полю: `да`"""

    isquest: Optional[int] = None
    """Является вопросом Возможность фильтровать по полю: `да`"""

    numwords: Optional[int] = None
    """Количество слов в запросе Возможность фильтровать по полю: `да`"""

    serpf: Optional[str] = None
    """Дата изменения позиции Возможность фильтровать по полю: `нет`"""

    superwsk: Optional[int] = None
    """\"[!Супер !точная !частотность]" Возможность фильтровать по полю: `да`"""

    url: Optional[str] = None
    """Страница, представленная в выдаче Возможность фильтровать по полю: `да`"""

    word: Optional[str] = None
    """Ключевая фраза Возможность фильтровать по полю: `да`"""

    ws: Optional[int] = None
    """Базовая частотность Возможность фильтровать по полю: `да`"""

    wsk: Optional[int] = None
    """\"!Очень !точная !частотность" Возможность фильтровать по полю: `да`"""


class ToolListSiteThemesResponse(BaseModel):
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
