# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WordstatReportResponse", "Data", "DataWsGraph"]


class DataWsGraph(BaseModel):
    count: Optional[int] = None
    """Счетчик"""

    date: Optional[str] = None
    """Дата"""


class Data(BaseModel):
    id: Optional[str] = None
    """Запрос Возможность фильтровать по полю: `нет`"""

    bdg100: Optional[int] = None
    """Бюджет в месяц 100%(объем трафика) Возможность фильтровать по полю: `да`"""

    bdg5: Optional[int] = None
    """Бюджет в месяц 5%(объем трафика) Возможность фильтровать по полю: `да`"""

    bdg62: Optional[int] = None
    """Бюджет в месяц 62%(объем трафика) Возможность фильтровать по полю: `да`"""

    bdg85: Optional[int] = None
    """Бюджет в месяц 85%(объем трафика) Возможность фильтровать по полю: `да`"""

    bdg9: Optional[int] = None
    """Бюджет в месяц 9%(объем трафика) Возможность фильтровать по полю: `да`"""

    cpc100: Optional[int] = None
    """Цена клика 100%(объем трафика) Возможность фильтровать по полю: `да`"""

    cpc5: Optional[int] = None
    """Цена клика 5%(объем трафика) Возможность фильтровать по полю: `да`"""

    cpc62: Optional[int] = None
    """Цена клика 62%(объем трафика) Возможность фильтровать по полю: `да`"""

    cpc85: Optional[int] = None
    """Цена клика 85%(объем трафика) Возможность фильтровать по полю: `да`"""

    cpc9: Optional[int] = None
    """Цена клика 9%(объем трафика) Возможность фильтровать по полю: `да`"""

    initial_word: Optional[str] = None
    """Исходная фраза Возможность фильтровать по полю: `да`"""

    numwords: Optional[int] = None
    """Количество слов Возможность фильтровать по полю: `да`"""

    qwsk: Optional[int] = None
    """
    Фразовая частотность без учета дополнительных слов Возможность фильтровать по
    полю: `да`
    """

    reason: Optional[str] = None
    """Ошибка парсинга Возможность фильтровать по полю: `нет`"""

    swsk: Optional[int] = None
    """Точная частотность с учётом порядка слов Возможность фильтровать по полю: `да`"""

    type: Optional[str] = None
    """Источник Возможность фильтровать по полю: `да`"""

    updated_at: Optional[str] = None
    """Дата обновления фразы Возможность фильтровать по полю: `да`"""

    word: Optional[str] = None
    """Запрос Возможность фильтровать по полю: `да`"""

    ws: Optional[int] = None
    """Широкая частотность запроса Возможность фильтровать по полю: `да`"""

    ws_graph: Optional[List[DataWsGraph]] = FieldInfo(alias="wsGraph", default=None)
    """Граф Возможность фильтровать по полю: `нет`"""

    wsk: Optional[int] = None
    """
    Частотность с учетом количества слов и их формы(число, падеж, время) Возможность
    фильтровать по полю: `да`
    """


class WordstatReportResponse(BaseModel):
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
