# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ReportCreateSystemKeywordsResponse", "Data"]


class Data(BaseModel):
    adscnt: Optional[int] = None
    """Количество объявлений в контексте Возможность фильтровать по полю: `да`"""

    avbid: Optional[int] = None
    """Цена клика.

    Данный параметр в ответе будет присутствовать, только при наличии фильтра в
    запросе. Возможность фильтровать по полю: `да`
    """

    docs: Optional[int] = None
    """Количество документов в выдаче Возможность фильтровать по полю: `да`"""

    gamn: Optional[int] = None
    """Цена клика.

    Данный параметр в ответе будет присутствовать, только при наличии фильтра в
    запросе. Возможность фильтровать по полю: `да`
    """

    gctr: Optional[int] = None
    """Клики к числу показов в процентном соотношении.

    Данный параметр в ответе будет присутствовать, только при наличии фильтра в
    запросе. Возможность фильтровать по полю: `да`
    """

    isadult: Optional[bool] = None
    """Является ли запросом 18+.

    Данный параметр в ответе будет присутствовать, только при наличии фильтра в
    запросе. Возможность фильтровать по полю: `да`
    """

    isgeo: Optional[int] = None
    """Является топонимом Возможность фильтровать по полю: `да`"""

    isquest: Optional[int] = None
    """Является вопросом Возможность фильтровать по полю: `да`"""

    numwords: Optional[int] = None
    """Количество слов в запросе Возможность фильтровать по полю: `да`"""

    superwsk: Optional[int] = None
    """\"[!Супер !точная !частотность]" Возможность фильтровать по полю: `да`"""

    updated_at: Optional[str] = None
    """
    Дата, когда мы повторно встретили данную пару ссылок. Возможность фильтровать по
    полю: `да`
    """

    word: Optional[str] = None
    """Фраза Возможность фильтровать по полю: `да`"""

    ws: Optional[int] = None
    """Базовая частотность Возможность фильтровать по полю: `да`"""

    wsk: Optional[int] = None
    """\"!Очень !точная !частотность" Возможность фильтровать по полю: `да`"""


class ReportCreateSystemKeywordsResponse(BaseModel):
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
