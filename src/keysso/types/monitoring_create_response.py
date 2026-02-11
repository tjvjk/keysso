# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .alert_setting import AlertSetting
from .scheduler_setting import SchedulerSetting

__all__ = ["MonitoringCreateResponse", "SearchSetting"]


class SearchSetting(BaseModel):
    engine: Optional[int] = None
    """Идентификатор поисковой системы"""

    region_id: Optional[int] = FieldInfo(alias="regionId", default=None)
    """Идентификатор региона"""

    region_name: Optional[str] = FieldInfo(alias="regionName", default=None)
    """Название региона"""


class MonitoringCreateResponse(BaseModel):
    id: Optional[int] = None
    """Идентификатор созданного проекта"""

    alert_setting: Optional[AlertSetting] = FieldInfo(alias="alertSetting", default=None)
    """Настройки уведомлений"""

    child_projects: Optional[List[object]] = FieldInfo(alias="childProjects", default=None)
    """Дочерние проекты (фиксированное значение [])"""

    cluster_arts: Optional[List[object]] = FieldInfo(alias="clusterArts", default=None)
    """Папки проекта кластеризатора (фиксированное значение [])"""

    cluster_uuid: Optional[str] = FieldInfo(alias="clusterUuid", default=None)
    """Уникальный идентификатор кластера"""

    name: Optional[str] = None
    """Название проекта"""

    next_start_at: Optional[str] = FieldInfo(alias="nextStartAt", default=None)
    """Время следующего запуска (фиксированное значение null)"""

    scheduler_setting: Optional[SchedulerSetting] = FieldInfo(alias="schedulerSetting", default=None)
    """Настройки планировщика"""

    search_settings: Optional[List[SearchSetting]] = FieldInfo(alias="searchSettings", default=None)

    tracking_item: Optional[str] = FieldInfo(alias="trackingItem", default=None)
    """Элемент отслеживания"""

    tracking_item_icon: Optional[Literal[""]] = FieldInfo(alias="trackingItemIcon", default=None)
    """Иконка элемента отслеживания (фиксированное значение "")"""

    track_sub_domains: Optional[bool] = FieldInfo(alias="trackSubDomains", default=None)
    """Флаг отслеживания поддоменов"""
