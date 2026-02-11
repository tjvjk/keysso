# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .report.base import Base

__all__ = ["ClusteringListResponse", "Data", "DataChildProjects", "DataChildProjectsSerp", "DataChildProjectsWordstat"]


class DataChildProjectsSerp(BaseModel):
    id: Optional[int] = None
    """ID проекта"""

    name: Optional[str] = None
    """Название проекта"""


class DataChildProjectsWordstat(BaseModel):
    id: Optional[int] = None
    """ID проекта"""

    name: Optional[str] = None
    """Название проекта"""


class DataChildProjects(BaseModel):
    """Дочерние проекты по типу данных"""

    serp: Optional[List[DataChildProjectsSerp]] = None
    """Проекты выдачи"""

    wordstat: Optional[List[DataChildProjectsWordstat]] = None
    """Проекты Wordstat"""


class Data(BaseModel):
    access_date: Optional[str] = None
    """Последнее обновление"""

    base: Optional[Base] = None
    """
    Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
    `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
    Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
    Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
    `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
    Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
    `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
    Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
    Минск `tom` - Яндекс: Томск `gny` - Google: New York
    """

    can_change_owner: Optional[bool] = FieldInfo(alias="canChangeOwner", default=None)
    """Возможность сменить владельца"""

    can_delete: Optional[bool] = FieldInfo(alias="canDelete", default=None)
    """Возможность удаления отчета"""

    child_projects: Optional[DataChildProjects] = None
    """Дочерние проекты по типу данных"""

    create_date: Optional[str] = None
    """Дата создания отчета"""

    monitoring_id: Optional[int] = None
    """ID родительского проекта мониторинга"""

    monitoring_name: Optional[str] = None
    """Название родительского проекта мониторинга"""

    name: Optional[str] = None
    """Имя отчета"""

    owner: Optional[str] = None
    """Владелец отчета"""

    state: Optional[int] = None
    """Статус отчета

    `1` - В обработке

    `2` - Ошибка обработки

    `10` - Обработка завершена
    """

    uid: Optional[str] = None
    """Идентификатор отчета"""


class ClusteringListResponse(BaseModel):
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
