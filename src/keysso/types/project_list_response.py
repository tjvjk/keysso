# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ProjectListResponse",
    "ProjectListResponseItem",
    "ProjectListResponseItemColors",
    "ProjectListResponseItemCompetitor",
    "ProjectListResponseItemData",
    "ProjectListResponseItemDataIndex",
    "ProjectListResponseItemDomain",
    "ProjectListResponseItemExtSettings",
    "ProjectListResponseItemExtSettingsNotifications",
    "ProjectListResponseItemGData",
    "ProjectListResponseItemGDataYyyyMm",
    "ProjectListResponseItemLastNotifyData",
    "ProjectListResponseItemLastNotifyDataGru",
    "ProjectListResponseItemLastNotifyDataGruContext",
    "ProjectListResponseItemLastNotifyDataGruContextAdCost",
    "ProjectListResponseItemLastNotifyDataGruContextAdKeysCount",
    "ProjectListResponseItemLastNotifyDataGruContextAdsCount",
    "ProjectListResponseItemLastNotifyDataGruContextAdTraf",
    "ProjectListResponseItemLastNotifyDataGruContextRsyAdsCount",
    "ProjectListResponseItemLastNotifyDataGruOrganic",
    "ProjectListResponseItemLastNotifyDataGruOrganicIt10",
    "ProjectListResponseItemLastNotifyDataGruOrganicIt3",
    "ProjectListResponseItemLastNotifyDataGruOrganicIt50",
    "ProjectListResponseItemLastNotifyDataGruOrganicPagesInIndex",
    "ProjectListResponseItemLastNotifyDataGruOrganicVis",
    "ProjectListResponseItemLastNotifyDataLink",
    "ProjectListResponseItemLastNotifyDataLinkBacklinksCount",
    "ProjectListResponseItemLastNotifyDataLinkDrgru",
    "ProjectListResponseItemLastNotifyDataLinkDrmsk",
    "ProjectListResponseItemLastNotifyDataLinkOutlinksCount",
    "ProjectListResponseItemLastNotifyDataLinkUniqBackdomainsCount",
    "ProjectListResponseItemLastNotifyDataLinkUniqBackipsCount",
    "ProjectListResponseItemLastNotifyDataMsk",
    "ProjectListResponseItemLastNotifyDataMskContext",
    "ProjectListResponseItemLastNotifyDataMskContextAdCost",
    "ProjectListResponseItemLastNotifyDataMskContextAdKeysCount",
    "ProjectListResponseItemLastNotifyDataMskContextAdsCount",
    "ProjectListResponseItemLastNotifyDataMskContextAdTraf",
    "ProjectListResponseItemLastNotifyDataMskContextRsyAdsCount",
    "ProjectListResponseItemLastNotifyDataMskOrganic",
    "ProjectListResponseItemLastNotifyDataMskOrganicIt10",
    "ProjectListResponseItemLastNotifyDataMskOrganicIt3",
    "ProjectListResponseItemLastNotifyDataMskOrganicIt50",
    "ProjectListResponseItemLastNotifyDataMskOrganicPagesInIndex",
    "ProjectListResponseItemLastNotifyDataMskOrganicVis",
    "ProjectListResponseItemPeriodicityData",
    "ProjectListResponseItemSettings",
    "ProjectListResponseItemSettingsChartSettings",
    "ProjectListResponseItemSettingsNotificationSettings",
    "ProjectListResponseItemSettingsNotificationSettingsDatabases",
]


class ProjectListResponseItemColors(BaseModel):
    """Цветовая схема для дашборда проекта"""

    ad_cost: Optional[str] = FieldInfo(alias="adCost", default=None)
    """Бюджет"""

    ad_keys_count: Optional[str] = FieldInfo(alias="adKeysCount", default=None)
    """Запросов в контексте"""

    ads_count: Optional[str] = FieldInfo(alias="adsCount", default=None)
    """Трафик в сутки(органика)"""

    ad_traf: Optional[str] = FieldInfo(alias="adTraf", default=None)
    """Трафик в сутки(контекст)"""

    backlinks_count: Optional[str] = FieldInfo(alias="backlinksCount", default=None)
    """Входящие ссылки"""

    dr: Optional[str] = None
    """DR"""

    it10: Optional[str] = None
    """Запросов в топ 10"""

    it3: Optional[str] = None
    """Запросов в топ 3"""

    it50: Optional[str] = None
    """Запросов в топ 50"""

    outlinks_count: Optional[str] = FieldInfo(alias="outlinksCount", default=None)
    """Исходящие ссылки"""

    pages_in_index: Optional[str] = FieldInfo(alias="pagesInIndex", default=None)
    """Количество страниц сайта, найденных в выдаче"""

    rsy_ads_count: Optional[str] = FieldInfo(alias="rsyAdsCount", default=None)
    """Объявления РСЯ"""

    uniq_backdomains_count: Optional[str] = FieldInfo(alias="uniqBackdomainsCount", default=None)
    """Ссылающиеся домены"""

    uniq_backips_count: Optional[str] = FieldInfo(alias="uniqBackipsCount", default=None)
    """Ссылки по IP"""

    vis: Optional[str] = None
    """Оценка трафика с поиска"""


class ProjectListResponseItemCompetitor(BaseModel):
    did: Optional[int] = None
    """Идентификатор домена"""

    main: Optional[bool] = None
    """Признак, что домен основной, а не поддомен"""

    name: Optional[str] = None
    """Имя домена"""


class ProjectListResponseItemDataIndex(BaseModel):
    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    link: Optional[str] = None
    """Ссылка на отчет"""

    name: Optional[str] = None
    """Название свойства"""

    type: Optional[str] = None
    """Тип свойства. Его код(органика, контекст или ссылки)."""

    value: Optional[int] = None
    """Значение"""


class ProjectListResponseItemData(BaseModel):
    """Данне по проекту.

    Кол-во возвращаемых элементов постоянно(15, по 5 на органику, контекст и ссылки)
    """

    index: Optional[ProjectListResponseItemDataIndex] = FieldInfo(alias="<index>", default=None)


class ProjectListResponseItemDomain(BaseModel):
    """Информация по домену"""

    did: Optional[int] = None
    """Идентификатор домена"""

    main: Optional[bool] = None
    """Признак, что домен основной, а не поддомен"""

    name: Optional[str] = None
    """Имя домена"""


class ProjectListResponseItemExtSettingsNotifications(BaseModel):
    is_notify_muted: Optional[bool] = FieldInfo(alias="isNotifyMuted", default=None)
    """Не присылать уведомления"""

    notify_email: Optional[bool] = FieldInfo(alias="notifyEmail", default=None)
    """Уведомлять по email"""

    notify_telegram: Optional[bool] = FieldInfo(alias="notifyTelegram", default=None)
    """Уведомлять через Telegram"""

    periodicity: Optional[int] = None
    """Период уведомлений `1` - при изменении `2` - раз в 14 дней `3` - раз в месяц"""


class ProjectListResponseItemExtSettings(BaseModel):
    """Расширенные настройки уведомлений"""

    notifications: Optional[ProjectListResponseItemExtSettingsNotifications] = None


class ProjectListResponseItemGDataYyyyMm(BaseModel):
    """Данные за месяц указанный в индексе"""

    ad_cost: Optional[int] = FieldInfo(alias="adCost", default=None)
    """Бюджет"""

    ad_keys_count: Optional[int] = FieldInfo(alias="adKeysCount", default=None)
    """Запросов в контексте"""

    ads_count: Optional[int] = FieldInfo(alias="adsCount", default=None)
    """Трафик в сутки(органика)"""

    ad_traf: Optional[int] = FieldInfo(alias="adTraf", default=None)
    """Трафик в сутки(контекст)"""

    backlinks_count: Optional[int] = FieldInfo(alias="backlinksCount", default=None)
    """Входящие ссылки"""

    dr: Optional[int] = None
    """DR"""

    it10: Optional[int] = None
    """Запросов в топ 10"""

    it3: Optional[int] = None
    """Запросов в топ 3"""

    it50: Optional[int] = None
    """Запросов в топ 50"""

    outlinks_count: Optional[int] = FieldInfo(alias="outlinksCount", default=None)
    """Исходящие ссылки"""

    pages_in_index: Optional[int] = FieldInfo(alias="pagesInIndex", default=None)
    """Количество страниц сайта, найденных в выдаче"""

    rsy_ads_count: Optional[int] = FieldInfo(alias="rsyAdsCount", default=None)
    """Объявления РСЯ"""

    uniq_backdomains_count: Optional[int] = FieldInfo(alias="uniqBackdomainsCount", default=None)
    """Ссылающиеся домены"""

    uniq_backips_count: Optional[int] = FieldInfo(alias="uniqBackipsCount", default=None)
    """Ссылки по IP"""

    vis: Optional[int] = None
    """Оценка трафика с поиска"""


class ProjectListResponseItemGData(BaseModel):
    """Информация для построения графика"""

    yyyy_mm: Optional[ProjectListResponseItemGDataYyyyMm] = FieldInfo(alias="<YYYY.MM>", default=None)
    """Данные за месяц указанный в индексе"""


class ProjectListResponseItemLastNotifyDataGruContextAdCost(BaseModel):
    """Бюджет"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataGruContextAdKeysCount(BaseModel):
    """Запросов в контексте"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataGruContextAdsCount(BaseModel):
    """Трафик в сутки(органика)"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataGruContextAdTraf(BaseModel):
    """Трафик в сутки(контекст)"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataGruContextRsyAdsCount(BaseModel):
    """Объявления РСЯ"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataGruContext(BaseModel):
    ad_cost: Optional[ProjectListResponseItemLastNotifyDataGruContextAdCost] = FieldInfo(alias="adCost", default=None)
    """Бюджет"""

    ad_keys_count: Optional[ProjectListResponseItemLastNotifyDataGruContextAdKeysCount] = FieldInfo(
        alias="adKeysCount", default=None
    )
    """Запросов в контексте"""

    ads_count: Optional[ProjectListResponseItemLastNotifyDataGruContextAdsCount] = FieldInfo(
        alias="adsCount", default=None
    )
    """Трафик в сутки(органика)"""

    ad_traf: Optional[ProjectListResponseItemLastNotifyDataGruContextAdTraf] = FieldInfo(alias="adTraf", default=None)
    """Трафик в сутки(контекст)"""

    rsy_ads_count: Optional[ProjectListResponseItemLastNotifyDataGruContextRsyAdsCount] = FieldInfo(
        alias="rsyAdsCount", default=None
    )
    """Объявления РСЯ"""


class ProjectListResponseItemLastNotifyDataGruOrganicIt10(BaseModel):
    """Запросов в топ 10"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataGruOrganicIt3(BaseModel):
    """Запросов в топ 3"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataGruOrganicIt50(BaseModel):
    """Запросов в топ 50"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataGruOrganicPagesInIndex(BaseModel):
    """Количество страниц сайта, найденных в выдаче"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataGruOrganicVis(BaseModel):
    """Оценка трафика с поиска"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataGruOrganic(BaseModel):
    it10: Optional[ProjectListResponseItemLastNotifyDataGruOrganicIt10] = None
    """Запросов в топ 10"""

    it3: Optional[ProjectListResponseItemLastNotifyDataGruOrganicIt3] = None
    """Запросов в топ 3"""

    it50: Optional[ProjectListResponseItemLastNotifyDataGruOrganicIt50] = None
    """Запросов в топ 50"""

    pages_in_index: Optional[ProjectListResponseItemLastNotifyDataGruOrganicPagesInIndex] = FieldInfo(
        alias="pagesInIndex", default=None
    )
    """Количество страниц сайта, найденных в выдаче"""

    vis: Optional[ProjectListResponseItemLastNotifyDataGruOrganicVis] = None
    """Оценка трафика с поиска"""


class ProjectListResponseItemLastNotifyDataGru(BaseModel):
    context: Optional[ProjectListResponseItemLastNotifyDataGruContext] = None

    organic: Optional[ProjectListResponseItemLastNotifyDataGruOrganic] = None


class ProjectListResponseItemLastNotifyDataLinkBacklinksCount(BaseModel):
    """Входящие ссылки"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataLinkDrgru(BaseModel):
    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataLinkDrmsk(BaseModel):
    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataLinkOutlinksCount(BaseModel):
    """Исходящие ссылки"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataLinkUniqBackdomainsCount(BaseModel):
    """Ссылающиеся домены"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataLinkUniqBackipsCount(BaseModel):
    """Ссылки по IP"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataLink(BaseModel):
    backlinks_count: Optional[ProjectListResponseItemLastNotifyDataLinkBacklinksCount] = FieldInfo(
        alias="backlinksCount", default=None
    )
    """Входящие ссылки"""

    drgru: Optional[ProjectListResponseItemLastNotifyDataLinkDrgru] = None

    drmsk: Optional[ProjectListResponseItemLastNotifyDataLinkDrmsk] = None

    outlinks_count: Optional[ProjectListResponseItemLastNotifyDataLinkOutlinksCount] = FieldInfo(
        alias="outlinksCount", default=None
    )
    """Исходящие ссылки"""

    uniq_backdomains_count: Optional[ProjectListResponseItemLastNotifyDataLinkUniqBackdomainsCount] = FieldInfo(
        alias="uniqBackdomainsCount", default=None
    )
    """Ссылающиеся домены"""

    uniq_backips_count: Optional[ProjectListResponseItemLastNotifyDataLinkUniqBackipsCount] = FieldInfo(
        alias="uniqBackipsCount", default=None
    )
    """Ссылки по IP"""


class ProjectListResponseItemLastNotifyDataMskContextAdCost(BaseModel):
    """Бюджет"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataMskContextAdKeysCount(BaseModel):
    """Запросов в контексте"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataMskContextAdsCount(BaseModel):
    """Трафик в сутки(органика)"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataMskContextAdTraf(BaseModel):
    """Трафик в сутки(контекст)"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataMskContextRsyAdsCount(BaseModel):
    """Объявления РСЯ"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataMskContext(BaseModel):
    ad_cost: Optional[ProjectListResponseItemLastNotifyDataMskContextAdCost] = FieldInfo(alias="adCost", default=None)
    """Бюджет"""

    ad_keys_count: Optional[ProjectListResponseItemLastNotifyDataMskContextAdKeysCount] = FieldInfo(
        alias="adKeysCount", default=None
    )
    """Запросов в контексте"""

    ads_count: Optional[ProjectListResponseItemLastNotifyDataMskContextAdsCount] = FieldInfo(
        alias="adsCount", default=None
    )
    """Трафик в сутки(органика)"""

    ad_traf: Optional[ProjectListResponseItemLastNotifyDataMskContextAdTraf] = FieldInfo(alias="adTraf", default=None)
    """Трафик в сутки(контекст)"""

    rsy_ads_count: Optional[ProjectListResponseItemLastNotifyDataMskContextRsyAdsCount] = FieldInfo(
        alias="rsyAdsCount", default=None
    )
    """Объявления РСЯ"""


class ProjectListResponseItemLastNotifyDataMskOrganicIt10(BaseModel):
    """Запросов в топ 10"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataMskOrganicIt3(BaseModel):
    """Запросов в топ 3"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataMskOrganicIt50(BaseModel):
    """Запросов в топ 50"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataMskOrganicPagesInIndex(BaseModel):
    """Количество страниц сайта, найденных в выдаче"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataMskOrganicVis(BaseModel):
    """Оценка трафика с поиска"""

    delta: Optional[int] = None
    """Дельта. Значение относительно последнего показателя"""

    value: Optional[int] = None


class ProjectListResponseItemLastNotifyDataMskOrganic(BaseModel):
    it10: Optional[ProjectListResponseItemLastNotifyDataMskOrganicIt10] = None
    """Запросов в топ 10"""

    it3: Optional[ProjectListResponseItemLastNotifyDataMskOrganicIt3] = None
    """Запросов в топ 3"""

    it50: Optional[ProjectListResponseItemLastNotifyDataMskOrganicIt50] = None
    """Запросов в топ 50"""

    pages_in_index: Optional[ProjectListResponseItemLastNotifyDataMskOrganicPagesInIndex] = FieldInfo(
        alias="pagesInIndex", default=None
    )
    """Количество страниц сайта, найденных в выдаче"""

    vis: Optional[ProjectListResponseItemLastNotifyDataMskOrganicVis] = None
    """Оценка трафика с поиска"""


class ProjectListResponseItemLastNotifyDataMsk(BaseModel):
    context: Optional[ProjectListResponseItemLastNotifyDataMskContext] = None

    organic: Optional[ProjectListResponseItemLastNotifyDataMskOrganic] = None


class ProjectListResponseItemLastNotifyData(BaseModel):
    gru: Optional[List[ProjectListResponseItemLastNotifyDataGru]] = None

    link: Optional[List[ProjectListResponseItemLastNotifyDataLink]] = None
    """Информация по ссылкам"""

    msk: Optional[List[ProjectListResponseItemLastNotifyDataMsk]] = None


class ProjectListResponseItemPeriodicityData(BaseModel):
    api_1: Optional[str] = FieldInfo(alias="1", default=None)

    api_2: Optional[str] = FieldInfo(alias="2", default=None)

    api_3: Optional[str] = FieldInfo(alias="3", default=None)


class ProjectListResponseItemSettingsChartSettings(BaseModel):
    """Признак отображения блока на дашборде проекта"""

    ad_cost: Optional[bool] = FieldInfo(alias="adCost", default=None)
    """Бюджет"""

    ad_keys_count: Optional[bool] = FieldInfo(alias="adKeysCount", default=None)
    """Запросов в контексте"""

    ads_count: Optional[bool] = FieldInfo(alias="adsCount", default=None)
    """Трафик в сутки(органика)"""

    ad_traf: Optional[bool] = FieldInfo(alias="adTraf", default=None)
    """Трафик в сутки(контекст)"""

    backlinks_count: Optional[bool] = FieldInfo(alias="backlinksCount", default=None)
    """Входящие ссылки"""

    dr: Optional[bool] = None
    """DR"""

    it10: Optional[bool] = None
    """Запросов в топ 10"""

    it3: Optional[bool] = None
    """Запросов в топ 3"""

    it50: Optional[bool] = None
    """Запросов в топ 50"""

    outlinks_count: Optional[bool] = FieldInfo(alias="outlinksCount", default=None)
    """Исходящие ссылки"""

    pages_in_index: Optional[bool] = FieldInfo(alias="pagesInIndex", default=None)
    """Количество страниц сайта, найденных в выдаче"""

    rsy_ads_count: Optional[bool] = FieldInfo(alias="rsyAdsCount", default=None)
    """Объявления РСЯ"""

    uniq_backdomains_count: Optional[bool] = FieldInfo(alias="uniqBackdomainsCount", default=None)
    """Ссылающиеся домены"""

    uniq_backips_count: Optional[bool] = FieldInfo(alias="uniqBackipsCount", default=None)
    """Ссылки по IP"""

    vis: Optional[bool] = None
    """Оценка трафика с поиска"""


class ProjectListResponseItemSettingsNotificationSettingsDatabases(BaseModel):
    gru: Optional[bool] = None
    """Уведомления по базе Google Москва"""

    msk: Optional[bool] = None
    """Уведомления по базе Яндекс Москва"""


class ProjectListResponseItemSettingsNotificationSettings(BaseModel):
    """Настройки уведомлений по проектам"""

    context: Optional[bool] = None
    """Контекст"""

    databases: Optional[ProjectListResponseItemSettingsNotificationSettingsDatabases] = None

    links: Optional[bool] = None
    """Ссылки"""

    organic: Optional[bool] = None
    """Органика"""


class ProjectListResponseItemSettings(BaseModel):
    """Настройки по проекту"""

    chart_settings: Optional[ProjectListResponseItemSettingsChartSettings] = FieldInfo(
        alias="chartSettings", default=None
    )
    """Признак отображения блока на дашборде проекта"""

    is_demo: Optional[bool] = FieldInfo(alias="isDemo", default=None)
    """Является ли проект демострационным"""

    notification_settings: Optional[ProjectListResponseItemSettingsNotificationSettings] = FieldInfo(
        alias="notificationSettings", default=None
    )
    """Настройки уведомлений по проектам"""


class ProjectListResponseItem(BaseModel):
    colors: Optional[ProjectListResponseItemColors] = None
    """Цветовая схема для дашборда проекта"""

    competitors: Optional[List[ProjectListResponseItemCompetitor]] = None

    data: Optional[List[ProjectListResponseItemData]] = None

    domain: Optional[ProjectListResponseItemDomain] = None
    """Информация по домену"""

    exist: Optional[bool] = None
    """Наличие в базе"""

    ext_settings: Optional[ProjectListResponseItemExtSettings] = FieldInfo(alias="extSettings", default=None)
    """Расширенные настройки уведомлений"""

    g_data: Optional[ProjectListResponseItemGData] = FieldInfo(alias="gData", default=None)
    """Информация для построения графика"""

    hidden: Optional[bool] = None

    hide_items: Optional[List[object]] = FieldInfo(alias="hideItems", default=None)
    """Скрытые элементы на дашборде"""

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """Иконка проекта"""

    is_free: Optional[bool] = FieldInfo(alias="isFree", default=None)
    """Является ли бесплатным проектом"""

    last_notify_data: Optional[ProjectListResponseItemLastNotifyData] = FieldInfo(alias="lastNotifyData", default=None)

    periodicity_data: Optional[ProjectListResponseItemPeriodicityData] = FieldInfo(
        alias="periodicityData", default=None
    )

    position: Optional[int] = None
    """Позиция"""

    project_id: Optional[int] = FieldInfo(alias="projectId", default=None)
    """Идентификатор проекта"""

    settings: Optional[ProjectListResponseItemSettings] = None
    """Настройки по проекту"""

    title: Optional[str] = None
    """Заголовок проекта"""

    type: Optional[int] = None


ProjectListResponse: TypeAlias = List[ProjectListResponseItem]
