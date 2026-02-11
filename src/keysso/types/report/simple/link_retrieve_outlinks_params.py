# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LinkRetrieveOutlinksParams"]


class LinkRetrieveOutlinksParams(TypedDict, total=False):
    domain: Required[str]
    """Имя домена"""

    filter: str
    """
    Подробнее про фильтрацию смотрите в разделе
    [Фильтрация данных](#tag/Filtraciya-dannyh)
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
