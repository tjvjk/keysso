# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["OrganicRetrieveConcurentsResponse", "Data"]


class Data(BaseModel):
    id: Optional[int] = None
    """Идентификатор домена Возможность фильтровать по полю: `нет`"""

    adcost: Optional[int] = None
    """Оценка бюджета без учета каких-либо таргетингов.

    Произведение точной частотности, на прогноз CTR, на стоимость клика, разделенное
    на 30 дней Возможность фильтровать по полю: `нет`
    """

    adkeyscnt: Optional[int] = None
    """Количество запросов в контексте Возможность фильтровать по полю: `да`"""

    adscnt: Optional[int] = None
    """Количество объявлений в контексте Возможность фильтровать по полю: `да`"""

    adtraf: Optional[int] = None
    """Оценка трафика из контекста без учета каких-либо таргетингов.

    Произведение точной частотности, на прогноз CTR, разделенное на 30 дней
    Возможность фильтровать по полю: `нет`
    """

    cnt: Optional[int] = None
    """Общих ключей в топ 50 Возможность фильтровать по полю: `да`"""

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

    name: Optional[str] = None
    """Имя домена Возможность фильтровать по полю: `да`"""

    pagesinindex: Optional[int] = None
    """
    Количество страниц сайта, найденных в выдаче Возможность фильтровать по полю:
    `да`
    """

    perc: Optional[float] = None
    """
    Степень похожести домена (% общих ключей от ключей домена) Возможность
    фильтровать по полю: `да`
    """

    theme: Optional[float] = None
    """
    Тематичность домена (% ключей анализируемого домена в ключах домена) Возможность
    фильтровать по полю: `да`
    """

    vis: Optional[int] = None
    """Оценка трафика с поиска Возможность фильтровать по полю: `нет`"""


class OrganicRetrieveConcurentsResponse(BaseModel):
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
