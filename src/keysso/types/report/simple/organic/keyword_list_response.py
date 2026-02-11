# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["KeywordListResponse", "Data", "DataWizards"]


class DataWizards(BaseModel):
    """Колдунщики<br>Возможность фильтровать по полю: `да`"""

    id: Optional[str] = None


class Data(BaseModel):
    adscnt: Optional[int] = None
    """Количество объявлений в контексте Возможность фильтровать по полю: `да`"""

    avbid: Optional[int] = None
    """Средняя цена клика Возможность фильтровать по полю: `да`"""

    churl: Optional[int] = None
    """Устаревший параметр Возможность фильтровать по полю: `нет`"""

    delta: Optional[int] = None
    """Изменение позиции Возможность фильтровать по полю: `да`"""

    did: Optional[int] = None
    """Идентификатор домена. Возможность фильтровать по полю: `нет`"""

    docs: Optional[int] = None
    """Количество документов в выдаче Возможность фильтровать по полю: `да`"""

    isgeo: Optional[int] = None
    """Является топонимом Возможность фильтровать по полю: `да`"""

    isquest: Optional[int] = None
    """Является вопросом Возможность фильтровать по полю: `да`"""

    kid: Optional[int] = None
    """Идентификатор фразы Возможность фильтровать по полю: `нет`"""

    numwords: Optional[int] = None
    """Количество слов в запросе Возможность фильтровать по полю: `да`"""

    nw: Optional[int] = None
    """Новый запрос Возможность фильтровать по полю: `да`"""

    pos: Optional[int] = None
    """Позиция в контексте Возможность фильтровать по полю: `да`"""

    serpf: Optional[str] = None
    """Дата изменения позиции Возможность фильтровать по полю: `да`"""

    url: Optional[str] = None
    """Страница, представленная в выдаче Возможность фильтровать по полю: `да`"""

    wizards: Optional[DataWizards] = None
    """Колдунщики Возможность фильтровать по полю: `да`"""

    wizardscount: Optional[int] = None
    """Число колдунщиков Возможность фильтровать по полю: `да`"""

    word: Optional[str] = None
    """Ключевая фраза Возможность фильтровать по полю: `да`"""

    ws: Optional[int] = None
    """Базовая частотность Возможность фильтровать по полю: `да`"""

    wsk: Optional[int] = None
    """\"!Очень !точная !частотность" Возможность фильтровать по полю: `да`"""


class KeywordListResponse(BaseModel):
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
