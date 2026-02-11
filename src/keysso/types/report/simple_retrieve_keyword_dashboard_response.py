# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SimpleRetrieveKeywordDashboardResponse", "Ad", "Similar", "Top"]


class Ad(BaseModel):
    amn: Optional[int] = None
    """Прогноз списываемой суммы на первом месте"""

    bid: Optional[int] = None
    """Средняя цена клика"""

    cpc_max: Optional[str] = None
    """Макс. Цена клика"""

    cpc_min: Optional[str] = None
    """Мин. Цена клика"""

    did: Optional[int] = None
    """Идентификатор домена"""

    domain: Optional[str] = None
    """Домен"""

    facts: Optional[List[str]] = None
    """Массив фактов"""

    header: Optional[str] = None
    """Заголовок объявления"""

    links: Optional[List[str]] = None
    """Массив быстрых ссылок"""

    txt: Optional[str] = None
    """Текст объявления"""


class Similar(BaseModel):
    avbid: Optional[int] = None
    """Средняя цена клик"""

    cnt: Optional[str] = None
    """Степень похожести запроса на исходный"""

    docs: Optional[int] = None
    """Количество документов в выдаче"""

    kid: Optional[int] = None
    """Идентификатор"""

    word: Optional[str] = None
    """Ключевая фраза"""

    ws: Optional[int] = None
    """Базовая частотность"""

    wsk: Optional[int] = None
    """\"!Очень !точная !частотность" """


class Top(BaseModel):
    adsenseid: Optional[str] = None
    """Идентификатор издателя Google Adsense"""

    analytics: Optional[str] = None
    """Идентификатор в Google Analytics"""

    churl: Optional[int] = None
    """Устаревший параметр"""

    delta: Optional[int] = None
    """Изменение позиции"""

    did: Optional[int] = None
    """Идентификатор домена"""

    domain: Optional[str] = None
    """Название домена"""

    it1: Optional[int] = None
    """Запросов сайта в топ 1"""

    it10: Optional[int] = None
    """Запросов сайта в топ 10"""

    it3: Optional[int] = None
    """Запросов сайта в топ 3"""

    it5: Optional[int] = None
    """Запросов сайта в топ 5"""

    it50: Optional[int] = None
    """Запросов сайта в топ 50"""

    pit1: Optional[str] = None
    """Запросов страниц в топ 1"""

    pit10: Optional[str] = None
    """Запросов страниц в топ 10"""

    pit5: Optional[str] = None
    """Запросов страниц в топ 5"""

    pit50: Optional[str] = None
    """Запросов страниц в топ 50"""

    pos: Optional[int] = None
    """Позиция"""

    url: Optional[str] = None
    """Целевая страница"""

    vis: Optional[int] = None
    """Оценка трафика с поиска"""


class SimpleRetrieveKeywordDashboardResponse(BaseModel):
    id: Optional[int] = None
    """Идентификатор ключевого слова"""

    ads: Optional[List[Ad]] = None
    """Контекстная реклама"""

    isgeo: Optional[int] = None
    """Является топонимом"""

    isquest: Optional[int] = None
    """Является вопросом"""

    similar: Optional[List[Similar]] = None
    """Дополняющие фразы, первые 20 записей"""

    top: Optional[List[Top]] = None
    """Органическая выдача"""

    word: Optional[str] = None
    """Ключевая фраза"""

    ws: Optional[int] = None
    """Базовая частотность"""

    wsk: Optional[int] = None
    """\"!Очень !точная !частотность" """
