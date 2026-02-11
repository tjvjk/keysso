# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "MonitoringListResponse",
    "Data",
    "DataChildProjects",
    "DataChildProjectsCluster",
    "DataChildProjectsSerp",
    "DataChildProjectsWordstat",
    "DataSearchSetting",
]


class DataChildProjectsCluster(BaseModel):
    """Проект кластеризатора"""

    name: Optional[str] = None
    """Название кластеризатора"""

    uid: Optional[str] = None
    """Уникальный идентификатор кластеризатора"""


class DataChildProjectsSerp(BaseModel):
    id: Optional[int] = None
    """Идентификатор проекта выдачи"""

    name: Optional[str] = None
    """Название проекта выдачи"""


class DataChildProjectsWordstat(BaseModel):
    id: Optional[int] = None
    """Идентификатор проекта выдачи"""

    name: Optional[str] = None
    """Название проекта выдачи"""


class DataChildProjects(BaseModel):
    """Связанные дочерние проекты"""

    cluster: Optional[DataChildProjectsCluster] = None
    """Проект кластеризатора"""

    serp: Optional[List[DataChildProjectsSerp]] = None
    """Проекты выдачи"""

    wordstat: Optional[List[DataChildProjectsWordstat]] = None
    """Проекты Wordstat"""


class DataSearchSetting(BaseModel):
    engine_name: Optional[str] = None
    """Название поисковой системы"""

    language: Optional[Literal[0]] = None
    """ID языка (пока только `0`)"""

    region_id: Optional[int] = None
    """Идентификатор региона"""

    region_name: Optional[str] = None
    """Название региона"""

    search_engine: Optional[int] = None
    """Идентификатор поисковой системы"""


class Data(BaseModel):
    id: Optional[int] = None
    """Идентификатор проекта"""

    avg_pos: Optional[int] = None
    """Средняя позиция в поисковой выдаче"""

    child_projects: Optional[DataChildProjects] = None
    """Связанные дочерние проекты"""

    created_at: Optional[str] = None
    """Дата создания проекта"""

    delta_avg_pos: Optional[int] = None
    """Изменение средней позиции"""

    last_finished_at: Optional[str] = None
    """Дата последнего завершения обработки"""

    name: Optional[str] = None
    """Название проекта"""

    next_start_at: Optional[str] = None
    """Дата следующего запуска проекта"""

    numwords: Optional[int] = None
    """Количество фраз в проекте"""

    search_settings: Optional[List[DataSearchSetting]] = None
    """Поисковые системы и регионы"""


class MonitoringListResponse(BaseModel):
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
