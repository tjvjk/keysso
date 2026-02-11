# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "LimitListResponse",
    "Analysis",
    "APIRequest",
    "CheckTop",
    "Clustering",
    "ConcurrentByKeywords",
    "DomainsBatch",
    "DomainsBatchPerDay",
    "DomainsBatchPerMonth",
    "Dzen",
    "ExtendedKeywords",
    "GroupReport",
    "KeysReportLimit",
    "KeywordsByList",
    "KeywordsByListPerDay",
    "KeywordsByListPerMonth",
    "Projects",
    "RecordsExportPerReport",
    "RecordsPerReport",
    "Rsya",
    "RsyaPerDay",
    "SearchKeys",
    "SearchKeysPerDay",
    "SearchKeysPerMonth",
    "SerpMaxActiveProjects",
    "SitesCompare",
    "Suggest",
    "SuggestPerDay",
    "TreePages",
    "Users",
    "Wordstat",
    "WordstatPerMonth",
    "WordstatMaxActiveProjects",
    "WordstatWord",
    "WordstatWordPerMonth",
]


class Analysis(BaseModel):
    """Анализируемых доменов в сутки"""

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class APIRequest(BaseModel):
    """Запросов к апи"""

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class CheckTop(BaseModel):
    """Подсветка топов"""

    max_words: Optional[int] = FieldInfo(alias="maxWords", default=None)
    """Максимальный запрос, строк"""


class Clustering(BaseModel):
    """Лимиты по инструменту 'Кластеризатор'."""

    at_time: Optional[int] = FieldInfo(alias="atTime", default=None)
    """Кластеризаций единовременно"""

    number_limit: Optional[int] = FieldInfo(alias="numberLimit", default=None)
    """Семантических ядер"""

    words_limit: Optional[int] = FieldInfo(alias="wordsLimit", default=None)
    """Макс.количество фраз"""


class ConcurrentByKeywords(BaseModel):
    """Лимиты по инструменту 'Доля конкурентов по фразам'."""

    concurrent_by_keywords_limit: Optional[int] = FieldInfo(alias="concurrentByKeywordsLimit", default=None)
    """Доступно строк для создания отчета"""


class DomainsBatchPerDay(BaseModel):
    """Дневные лимиты"""

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class DomainsBatchPerMonth(BaseModel):
    """Месячные лимиты"""

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class DomainsBatch(BaseModel):
    """Лимиты по инструменту 'Пакетный анализ'"""

    list_limit: Optional[int] = FieldInfo(alias="listLimit", default=None)
    """Доступно строк для создания отчета"""

    per_day: Optional[DomainsBatchPerDay] = FieldInfo(alias="perDay", default=None)
    """Дневные лимиты"""

    per_month: Optional[DomainsBatchPerMonth] = FieldInfo(alias="perMonth", default=None)
    """Месячные лимиты"""


class Dzen(BaseModel):
    """Лимиты по инструменту 'Дзен каналы'."""

    new_top_publications_export_row: Optional[int] = FieldInfo(alias="newTopPublicationsExportRow", default=None)
    """Максимально кол-во строк для экспорта топа публикаций"""

    publications_export_row: Optional[int] = FieldInfo(alias="publicationsExportRow", default=None)
    """Максимально кол-во строк для экспорта публикаций"""

    top_channels_export_row: Optional[int] = FieldInfo(alias="topChannelsExportRow", default=None)
    """Максимально кол-во строк для экспорта каналов"""


class ExtendedKeywords(BaseModel):
    """Лимиты по инструменту 'Расширение ключевых слов'."""

    records_per_list_limit: Optional[int] = FieldInfo(alias="recordsPerListLimit", default=None)
    """Доступно строк для создания отчета"""


class GroupReport(BaseModel):
    """Лимиты по инструменту 'Групповые отчеты'."""

    max_domains_number: Optional[int] = FieldInfo(alias="maxDomainsNumber", default=None)
    """Максимальное кол-во доменов."""

    max_requests: Optional[int] = FieldInfo(alias="maxRequests", default=None)
    """Максимум запросов."""


class KeysReportLimit(BaseModel):
    """Максимальное значение ключей в отчете.

    Если в блоке с инструментом нет отдельного значения, используется этот лимит
    """

    limit: Optional[int] = None
    """Доступный лимит"""


class KeywordsByListPerDay(BaseModel):
    """Дневные лимиты"""

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class KeywordsByListPerMonth(BaseModel):
    """Месячные лимиты"""

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class KeywordsByList(BaseModel):
    """Лимиты по инструменту 'Массовая проверка запросов'"""

    list_limit: Optional[int] = FieldInfo(alias="listLimit", default=None)
    """Доступно строк для создания отчета"""

    per_day: Optional[KeywordsByListPerDay] = FieldInfo(alias="perDay", default=None)
    """Дневные лимиты"""

    per_month: Optional[KeywordsByListPerMonth] = FieldInfo(alias="perMonth", default=None)
    """Месячные лимиты"""


class Projects(BaseModel):
    """Лимиты по инструменту 'Проекты'"""

    limit: Optional[int] = None
    """Доступный лимит проектов"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class RecordsExportPerReport(BaseModel):
    """Записей для экспорта в отчете.

    Если в блоке с инструментом нет отдельного значения, используется этот лимит
    """

    limit: Optional[int] = None
    """Доступный лимит"""


class RecordsPerReport(BaseModel):
    """Записей в отчете.

    Если в блоке с инструментом нет отдельного значения, используется этот лимит
    """

    limit: Optional[int] = None
    """Доступный лимит"""


class RsyaPerDay(BaseModel):
    """Дневные лимиты"""

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class Rsya(BaseModel):
    """Лимиты по инструментам 'РСЯ'"""

    per_day: Optional[RsyaPerDay] = FieldInfo(alias="perDay", default=None)
    """Дневные лимиты"""

    records_export_per_report: Optional[int] = FieldInfo(alias="recordsExportPerReport", default=None)
    """Строк для экспорта в отчете"""


class SearchKeysPerDay(BaseModel):
    """Дневные лимиты"""

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class SearchKeysPerMonth(BaseModel):
    """Месячные лимиты"""

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class SearchKeys(BaseModel):
    """Лимиты по инструменту 'База запросов'"""

    per_day: Optional[SearchKeysPerDay] = FieldInfo(alias="perDay", default=None)
    """Дневные лимиты"""

    per_month: Optional[SearchKeysPerMonth] = FieldInfo(alias="perMonth", default=None)
    """Месячные лимиты"""

    request_lines_limit: Optional[int] = FieldInfo(alias="requestLinesLimit", default=None)
    """Максимальный запрос, строк"""


class SerpMaxActiveProjects(BaseModel):
    """Лимиты по инструментам 'Онлайн парсинг выдачи'.

    Максимальное кол-во активных проектов.
    """

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Использованный лимит активных проектов"""


class SitesCompare(BaseModel):
    """Лимиты по инструменту 'Сравнение сайтов'"""

    limit: Optional[int] = None
    """Доступный лимит"""

    max_requests_in_top50: Optional[int] = FieldInfo(alias="maxRequestsInTop50", default=None)
    """Максимальное значение ключей в отчете"""


class SuggestPerDay(BaseModel):
    """Дневные лимиты"""

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class Suggest(BaseModel):
    """Лимиты по инструментам 'Сбор поисковых подсказок'"""

    list_limit: Optional[int] = FieldInfo(alias="listLimit", default=None)
    """Доступно строк для создания отчета"""

    per_day: Optional[SuggestPerDay] = FieldInfo(alias="perDay", default=None)
    """Дневные лимиты"""


class TreePages(BaseModel):
    """Лимиты по инструменту 'Дерево страниц'."""

    tree_pages_rows: Optional[int] = FieldInfo(alias="treePagesRows", default=None)
    """Максимально кол-во строк для экспорта"""


class Users(BaseModel):
    """Доступно пользователей в подписке"""

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class WordstatPerMonth(BaseModel):
    """Месячные лимиты"""

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class Wordstat(BaseModel):
    """Лимиты по инструментам 'Онлайн парсер Wordstat'"""

    per_month: Optional[WordstatPerMonth] = FieldInfo(alias="perMonth", default=None)
    """Месячные лимиты"""


class WordstatMaxActiveProjects(BaseModel):
    """Лимиты по инструментам 'Онлайн парсер Wordstat'.

    Максимальное кол-во активных проектов.
    """

    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Использованный лимит активных проектов"""


class WordstatWordPerMonth(BaseModel):
    limit: Optional[int] = None
    """Доступный лимит"""

    used_limit: Optional[int] = FieldInfo(alias="usedLimit", default=None)
    """Лимитов использовано"""


class WordstatWord(BaseModel):
    """Лимиты по инструментам 'Онлайн парсер Wordstat'. Максимальное кол-во фраз."""

    per_month: Optional[WordstatWordPerMonth] = FieldInfo(alias="perMonth", default=None)


class LimitListResponse(BaseModel):
    analysis: Optional[Analysis] = None
    """Анализируемых доменов в сутки"""

    api_request: Optional[APIRequest] = FieldInfo(alias="apiRequest", default=None)
    """Запросов к апи"""

    check_top: Optional[CheckTop] = FieldInfo(alias="checkTop", default=None)
    """Подсветка топов"""

    clustering: Optional[Clustering] = None
    """Лимиты по инструменту 'Кластеризатор'."""

    concurrent_by_keywords: Optional[ConcurrentByKeywords] = FieldInfo(alias="concurrentByKeywords", default=None)
    """Лимиты по инструменту 'Доля конкурентов по фразам'."""

    domains_batch: Optional[DomainsBatch] = FieldInfo(alias="domainsBatch", default=None)
    """Лимиты по инструменту 'Пакетный анализ'"""

    dzen: Optional[Dzen] = None
    """Лимиты по инструменту 'Дзен каналы'."""

    extended_keywords: Optional[ExtendedKeywords] = FieldInfo(alias="extendedKeywords", default=None)
    """Лимиты по инструменту 'Расширение ключевых слов'."""

    group_report: Optional[GroupReport] = FieldInfo(alias="groupReport", default=None)
    """Лимиты по инструменту 'Групповые отчеты'."""

    keys_report_limit: Optional[KeysReportLimit] = FieldInfo(alias="keysReportLimit", default=None)
    """Максимальное значение ключей в отчете.

    Если в блоке с инструментом нет отдельного значения, используется этот лимит
    """

    keywords_by_list: Optional[KeywordsByList] = FieldInfo(alias="keywordsByList", default=None)
    """Лимиты по инструменту 'Массовая проверка запросов'"""

    projects: Optional[Projects] = None
    """Лимиты по инструменту 'Проекты'"""

    records_export_per_report: Optional[RecordsExportPerReport] = FieldInfo(
        alias="recordsExportPerReport", default=None
    )
    """Записей для экспорта в отчете.

    Если в блоке с инструментом нет отдельного значения, используется этот лимит
    """

    records_per_report: Optional[RecordsPerReport] = FieldInfo(alias="recordsPerReport", default=None)
    """Записей в отчете.

    Если в блоке с инструментом нет отдельного значения, используется этот лимит
    """

    rsya: Optional[Rsya] = None
    """Лимиты по инструментам 'РСЯ'"""

    search_keys: Optional[SearchKeys] = FieldInfo(alias="searchKeys", default=None)
    """Лимиты по инструменту 'База запросов'"""

    serp_max_active_projects: Optional[SerpMaxActiveProjects] = FieldInfo(alias="serpMaxActiveProjects", default=None)
    """Лимиты по инструментам 'Онлайн парсинг выдачи'.

    Максимальное кол-во активных проектов.
    """

    sites_compare: Optional[SitesCompare] = FieldInfo(alias="sitesCompare", default=None)
    """Лимиты по инструменту 'Сравнение сайтов'"""

    suggest: Optional[Suggest] = None
    """Лимиты по инструментам 'Сбор поисковых подсказок'"""

    tree_pages: Optional[TreePages] = FieldInfo(alias="treePages", default=None)
    """Лимиты по инструменту 'Дерево страниц'."""

    users: Optional[Users] = None
    """Доступно пользователей в подписке"""

    wordstat: Optional[Wordstat] = None
    """Лимиты по инструментам 'Онлайн парсер Wordstat'"""

    wordstat_max_active_projects: Optional[WordstatMaxActiveProjects] = FieldInfo(
        alias="wordstatMaxActiveProjects", default=None
    )
    """Лимиты по инструментам 'Онлайн парсер Wordstat'.

    Максимальное кол-во активных проектов.
    """

    wordstat_word: Optional[WordstatWord] = FieldInfo(alias="wordstatWord", default=None)
    """Лимиты по инструментам 'Онлайн парсер Wordstat'. Максимальное кол-во фраз."""
