# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["LinkDomainsBatchResponse", "Data"]


class Data(BaseModel):
    id: Optional[int] = None
    """Идентификатор домена Возможность фильтровать по полю: `нет`"""

    dr: Optional[int] = None
    """
    Рейтинг домена — метрика, которая показывает общую силу ссылочного профиля
    домена в сравнении со всеми остальными сайтами. Возможность фильтровать по полю:
    `да`
    """

    it10: Optional[int] = None
    """Запросов в топ 10 Возможность фильтровать по полю: `да`"""

    it50: Optional[int] = None
    """Запросов в топ 50 Возможность фильтровать по полю: `да`"""

    name: Optional[str] = None
    """Имя домена Возможность фильтровать по полю: `да`"""

    numdomain: Optional[int] = None
    """Ссылающихся доменов Возможность фильтровать по полю: `да`"""

    numip: Optional[int] = None
    """Ссылающихся IP. Возможность фильтровать по полю:`да`"""

    numlink: Optional[int] = None
    """Исходящих ссылок Возможность фильтровать по полю: `да`"""

    numurl: Optional[int] = None
    """Входящих ссылок Возможность фильтровать по полю: `да`"""

    vis: Optional[int] = None
    """Оценка трафика с поиска Возможность фильтровать по полю: `да`"""


class LinkDomainsBatchResponse(BaseModel):
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
