# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WordstatReportParams"]


class WordstatReportParams(TypedDict, total=False):
    project_id: Required[Annotated[int, PropertyInfo(alias="projectId")]]
    """Идентификатор проекта"""

    full: str
    """
    При наличии данного параметра будет отдан полный отчет, при отсутствии ответ
    будет сгруппирован по запросу
    """

    page: int
    """Порядковый номер страницы результатов"""

    per_page: int
    """Количество результатов на одной странице"""

    sort: str
    """Сортировка данных по полям.

    Формат: `field|direction`, где

    `field` - имя колонки `direction` - направление сортировки, asc - по
    возрастанию, desc - по убыванию

    Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`
    """
