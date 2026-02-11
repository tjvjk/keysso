# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["SitepageListResponse", "Data"]


class Data(BaseModel):
    found_date: Optional[str] = None
    """Дата обнаружения Возможность фильтровать по полю: `да`"""

    it1: Optional[int] = None
    """Запросов в топ 1 Возможность фильтровать по полю: `да`"""

    it10: Optional[int] = None
    """Запросов в топ 10 Возможность фильтровать по полю: `да`"""

    it3: Optional[int] = None
    """Запросов в топ 3 Возможность фильтровать по полю: `да`"""

    it5: Optional[int] = None
    """Запросов в топ 5 Возможность фильтровать по полю: `да`"""

    it50: Optional[int] = None
    """Запросов в топ 50 Возможность фильтровать по полю: `да`"""

    new_url: Optional[int] = None
    """Новый урл Возможность фильтровать по полю: `да`"""

    url: Optional[str] = None
    """Адрес страницы сайта Возможность фильтровать по полю: `да`"""

    vis: Optional[int] = None
    """Оценка видимости страницы в поиске.

    Чем больше - тем больше потенциал трафика на страницу Возможность фильтровать по
    полю: `нет`
    """


class SitepageListResponse(BaseModel):
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
