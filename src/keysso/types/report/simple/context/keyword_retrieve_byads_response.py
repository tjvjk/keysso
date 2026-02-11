# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["KeywordRetrieveByadsResponse", "Data"]


class Data(BaseModel):
    adscnt: Optional[int] = None
    """Количество объявлений в контексте Возможность фильтровать по полю: `да`"""

    avbid: Optional[int] = None
    """Средняя цена клика Возможность фильтровать по полю: `да`"""

    docs: Optional[int] = None
    """Количество документов в выдаче Возможность фильтровать по полю: `да`"""

    header: Optional[str] = None
    """Заголовок объявления Возможность фильтровать по полю: `да`"""

    isgeo: Optional[int] = None
    """Является топонимом Возможность фильтровать по полю: `да`"""

    isquest: Optional[int] = None
    """Является вопросом Возможность фильтровать по полю: `да`"""

    numwords: Optional[int] = None
    """Количество слов в запросе Возможность фильтровать по полю: `да`"""

    pos: Optional[int] = None
    """Позиция в контексте Возможность фильтровать по полю: `да`"""

    serp: Optional[str] = None
    """Дата обновления Возможность фильтровать по полю: `да`"""

    sr: Optional[int] = None
    """
    Блок размещения объявлений Возможные значения: `1` - Блок премиум показов `0` -
    Блок остальных показов Возможность фильтровать по полю: `да`
    """

    superwsk: Optional[int] = None
    """\"[!Супер !точная !частотность]" Возможность фильтровать по полю: `да`"""

    txt: Optional[str] = None
    """Текст объявления Возможность фильтровать по полю: `да`"""

    word: Optional[str] = None
    """Ключевая фраза Возможность фильтровать по полю: `да`"""

    ws: Optional[int] = None
    """Базовая частотность Возможность фильтровать по полю: `да`"""

    wsk: Optional[int] = None
    """\"!Очень !точная !частотность" Возможность фильтровать по полю: `да`"""


class KeywordRetrieveByadsResponse(BaseModel):
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
