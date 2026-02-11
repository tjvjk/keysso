# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SimpleRetrieveDomainDashboardResponse",
    "Adconc",
    "Adkey",
    "Ad",
    "Conc",
    "History",
    "HistoryHistoryItem",
    "Key",
    "LinksHistory",
    "Page",
]


class Adconc(BaseModel):
    adkeyscnt: Optional[int] = None
    """Количество запросов в контексте"""

    adscnt: Optional[int] = None
    """Количество объявлений в контексте"""

    cnt: Optional[int] = None
    """Общих ключей в топ 50"""

    did: Optional[int] = None
    """Идентификатор домена"""

    name: Optional[str] = None
    """Имя домена"""

    vis: Optional[int] = None
    """Оценка трафика с поиска"""


class Adkey(BaseModel):
    avbid: Optional[int] = None
    """Стоимость клика на входе в остальные показы"""

    p: Optional[List[int]] = None

    pos: Optional[int] = None
    """Позиция в выдаче"""

    sr: Optional[int] = None
    """
    Блок размещения объявлений Возможные значения: `1` - Блок премиум показов `0` -
    Блок остальных показов
    """

    word: Optional[str] = None
    """Ключевая фраза"""

    ws: Optional[int] = None
    """Базовая частотность"""

    wsk: Optional[int] = None
    """\"!Очень !точная !частотность" """


class Ad(BaseModel):
    id: Optional[int] = None
    """Идентификатор объявления"""

    facts: Optional[str] = None
    """Факты"""

    header: Optional[str] = None
    """Заголовок объявления"""

    keyscnt: Optional[int] = None
    """Количество запросов"""

    links: Optional[str] = None
    """Быстрые ссылки"""

    txt: Optional[str] = None
    """Текст объявления"""


class Conc(BaseModel):
    cnt: Optional[int] = None
    """Общих ключей в топ 50"""

    did: Optional[int] = None
    """Идентификатор домена"""

    name: Optional[str] = None
    """Имя домена"""

    perc: Optional[object] = None
    """Степень похожести домена (% общих ключей от ключей домена)"""

    vis: Optional[int] = None
    """Оценка трафика с поиска"""


class HistoryHistoryItem(BaseModel):
    ad_keys_count: Optional[int] = FieldInfo(alias="adKeysCount", default=None)
    """Количество запросов в контексте"""

    ads_count: Optional[int] = FieldInfo(alias="adsCount", default=None)
    """Количество объявлений в контексте"""

    ai_cnt: Optional[int] = FieldInfo(alias="aiCnt", default=None)
    """Количество ответов ИИ за последний месяц"""

    it1: Optional[int] = None
    """Количество запросов в топ-1"""

    it10: Optional[int] = None
    """Количество запросов в топ-10"""

    it3: Optional[int] = None
    """Количество запросов в топ-3"""

    it5: Optional[int] = None
    """Количество запросов в топ-5"""

    it50: Optional[int] = None
    """Количество запросов в топ-50"""

    pages_in_index: Optional[int] = FieldInfo(alias="pagesInIndex", default=None)
    """Страниц в поисковом индексе"""

    vis_avg: Optional[int] = FieldInfo(alias="visAvg", default=None)
    """Ориентировочное значение трафика (усреднённое)"""


class History(BaseModel):
    """
    История изменения параметров сайта `{"Дата обновления": ["топ 1", "топ 3", "топ 5", "топ 10", "топ 50", "Страниц", “Объявлений“, “Запросов в контексте“, “Трафик с поиска“, "Упоминания в ИИ-ответах Алисы"]}`
    """

    yyyy_mm: Optional[List[str]] = FieldInfo(alias="<YYYY.MM>", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, HistoryHistoryItem] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> HistoryHistoryItem: ...
    else:
        __pydantic_extra__: Dict[str, HistoryHistoryItem]


class Key(BaseModel):
    pos: Optional[int] = None
    """Позиция в выдаче"""

    word: Optional[str] = None
    """Ключевая фраза"""

    ws: Optional[int] = None
    """Базовая частотность"""

    wsk: Optional[int] = None
    """\"!Очень !точная !частотность" """


class LinksHistory(BaseModel):
    """
    История по активным ссылкам `{"Дата обновления": ["входящие ссылки", "исходящие ссылки", "ссылающееся домены", "исходящие домены", "ссылки по IP"]}`
    """

    yyyy_mm: Optional[List[str]] = FieldInfo(alias="<YYYY.MM>", default=None)


class Page(BaseModel):
    it50: Optional[str] = None
    """Общих ключей в топ 50"""

    url: Optional[str] = None
    """URL страницы"""


class SimpleRetrieveDomainDashboardResponse(BaseModel):
    id: Optional[int] = None
    """Идентификатор домена"""

    adconcs: Optional[List[Adconc]] = None
    """Контекстная реклама, конкуренты, первые 20 записей"""

    adcost: Optional[int] = None
    """Оценка бюджета без учета каких-либо таргетингов.

    Произведение точной частотности, на прогноз CTR, на стоимость клика, разделенное
    на 30 дней
    """

    adkeys: Optional[List[Adkey]] = None
    """Контекстная реклама, ключевые слова сайта, первые 20 записей"""

    adkeyscnt: Optional[int] = None
    """Количество запросов в контексте"""

    ads: Optional[List[Ad]] = None
    """Органическая выдача, страницы, первые 20 записей"""

    adscnt: Optional[int] = None
    """Количество объявлений в контексте"""

    adtraf: Optional[int] = None
    """Оценка трафика из контекста без учета каких-либо таргетингов.

    Произведение точной частотности, на прогноз CTR, разделенное на 30 дн
    """

    ai_answers_cnt: Optional[int] = FieldInfo(alias="aiAnswersCnt", default=None)
    """Количество упоминаний сайта в ИИ-ответах Алисы по запросам за последние 30 дней"""

    ai_state: Optional[int] = FieldInfo(alias="aiState", default=None)
    """
    Статус построения ИИ-отчёта Возможные значения: `0` - Не создан `10` - Создан,
    ожидает построения `20` - Строится `30` - Ошибка построения `40` - Готов
    """

    childs_count: Optional[int] = FieldInfo(alias="childsCount", default=None)
    """Количество поддоменов сайта"""

    concs: Optional[List[Conc]] = None
    """Органическая выдача, конкуренты, первые 20 записей"""

    dr: Optional[int] = None
    """Рейтинг домена"""

    history: Optional[History] = None
    """
    История изменения параметров сайта
    `{"Дата обновления": ["топ 1", "топ 3", "топ 5", "топ 10", "топ 50", "Страниц", “Объявлений“, “Запросов в контексте“, “Трафик с поиска“, "Упоминания в ИИ-ответах Алисы"]}`
    """

    icon_url: Optional[str] = FieldInfo(alias="iconUrl", default=None)
    """Урл иконки домена"""

    it1: Optional[int] = None
    """Запросов в топ 1"""

    it10: Optional[int] = None
    """Запросов в топ 10"""

    it3: Optional[int] = None
    """Запросов в топ 3"""

    it5: Optional[int] = None
    """Запросов в топ 5"""

    it50: Optional[int] = None
    """Запросов в топ 50"""

    keys: Optional[List[Key]] = None
    """Органическая выдача, ключевые фразы, первые 20 записей"""

    links_history: Optional[LinksHistory] = FieldInfo(alias="linksHistory", default=None)
    """
    История по активным ссылкам
    `{"Дата обновления": ["входящие ссылки", "исходящие ссылки", "ссылающееся домены", "исходящие домены", "ссылки по IP"]}`
    """

    name: Optional[str] = None
    """Название домена"""

    pages: Optional[List[Page]] = None
    """Органическая выдача, страницы, первые 20 записей"""

    pagesinindex: Optional[int] = None
    """Страниц в выдаче"""

    parentid: Optional[int] = None
    """Идентификатор родительского домена, если домен является поддоменом"""

    parent_name: Optional[str] = FieldInfo(alias="parentName", default=None)
    """Имя родительского домена, если домен является поддоменом"""

    restop5: Optional[int] = None
    """Процент ключей из ТОП50, занимающий позиции в ТОП5"""

    topkeys: Optional[int] = None
    """По охвату ключей"""

    topvis: Optional[int] = None
    """По видимости"""

    vis: Optional[int] = None
    """Ориентировочное количество пользователей из органического поиска в сутки"""
