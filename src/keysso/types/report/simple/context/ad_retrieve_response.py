# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["AdRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[int] = None
    """Идентификатор объявления Возможность фильтровать по полю: `нет`"""

    facts: Optional[List[str]] = None
    """Массив фактов Возможность фильтровать по полю: `да`"""

    header: Optional[str] = None
    """Заголовок объявления Возможность фильтровать по полю: `да`"""

    keys: Optional[List[str]] = None
    """Массив ключевых слов, поле доступно при добавлении параметра full (см.

    параметры запроса) Возможность фильтровать по полю: `нет`
    """

    keyscnt: Optional[int] = None
    """Количество запросов Возможность фильтровать по полю: `да`"""

    legal: Optional[str] = None
    """Рекламодатель Возможность фильтровать по полю: `да`"""

    links: Optional[List[str]] = None
    """Массив быстрых ссылок Возможность фильтровать по полю: `да`"""

    serp: Optional[str] = None
    """Дата обновления Возможность фильтровать по полю: `да`"""

    txt: Optional[str] = None
    """Текст объявления Возможность фильтровать по полю: `да`"""

    url: Optional[str] = None
    """URL Возможность фильтровать по полю: `да`"""


class AdRetrieveResponse(BaseModel):
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
