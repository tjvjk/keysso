# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["DirectRetrieveAdsResponse", "Data"]


class Data(BaseModel):
    description: Optional[str] = None
    """Текст найденного объявления. Возможность фильтровать по полю: `да`"""

    domain: Optional[str] = None
    """Домен. Возможность фильтровать по полю: `да`"""

    keys_count: Optional[int] = None
    """
    Количество запросов, по которым настроен показ данного объявления в Яндекс
    Директе. Возможность фильтровать по полю: `да`
    """

    link: Optional[str] = None
    """
    Ссылка на посадочную страницу из объявления. Возможность фильтровать по полю:
    `да`
    """

    regions: Optional[str] = None
    """
    Настроенные регионы показа для найденного объявления, в том числе исключенные
    местоположения. Возможность фильтровать по полю: `да`
    """

    title: Optional[str] = None
    """
    Заголовок найденного объявления в Яндекс Директе. Возможность фильтровать по
    полю: `да`
    """

    updated_at: Optional[str] = None
    """
    Дата обновления нашим сервисом данных по объявлению. Возможность фильтровать по
    полю: `нет`
    """

    uuid: Optional[str] = None
    """Идентификатор объявления. Возможность фильтровать по полю: `нет`"""


class DirectRetrieveAdsResponse(BaseModel):
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
