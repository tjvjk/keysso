# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolCreateDomainsBatchResponse", "Data", "MessageCollapse"]


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

    adskeys: Optional[int] = None
    """Запросов на объявление Возможность фильтровать по полю: `да`"""

    adtraf: Optional[int] = None
    """Оценка трафика из контекста без учета каких-либо таргетингов.

    Произведение точной частотности, на прогноз CTR, разделенное на 30 дней
    Возможность фильтровать по полю: `нет`
    """

    ai_state: Optional[int] = None
    """
    Статус построения ИИ-отчёта Возможные значения: `0` - Не создан `10` - Создан,
    ожидает построения `20` - Строится `30` - Ошибка построения `40` - Готов
    Возможность фильтровать по полю: `да`
    """

    aianswerscnt: Optional[int] = None
    """
    Количество упоминаний сайта в Алисе по запросам за последние 30 дней Возможность
    фильтровать по полю: `да`
    """

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

    keyspage: Optional[int] = None
    """Запросов на страницу Возможность фильтровать по полю: `да`"""

    name: Optional[str] = None
    """Имя домена Возможность фильтровать по полю: `да`"""

    pagesinindex: Optional[int] = None
    """
    Количество страниц сайта, найденных в выдаче Возможность фильтровать по полю:
    `да`
    """

    result: Optional[int] = None
    """Результативность(в процентах) Возможность фильтровать по полю: `да`"""

    topkeys: Optional[int] = None
    """По охвату ключей Возможность фильтровать по полю: `да`"""

    topvis: Optional[int] = None
    """По видимости Возможность фильтровать по полю: `да`"""

    traf: Optional[int] = None
    """Трафик Возможность фильтровать по полю: `да`"""

    vis: Optional[int] = None
    """Оценка трафика с поиска Возможность фильтровать по полю: `да`"""


class MessageCollapse(BaseModel):
    """Дополнительное сообщение по результатам"""

    text: Optional[str] = None
    """Информационное сообщение"""

    title: Optional[str] = None
    """Заголовок"""


class ToolCreateDomainsBatchResponse(BaseModel):
    current_page: Optional[int] = None
    """Текущая страница"""

    data: Optional[List[Data]] = None
    """Данные ответа"""

    last_page: Optional[int] = None
    """Последняя страница"""

    message_collapse: Optional[MessageCollapse] = FieldInfo(alias="messageCollapse", default=None)
    """Дополнительное сообщение по результатам"""

    per_page: Optional[int] = None
    """Записей на странице"""

    total: Optional[int] = None
    """Всего записей"""
