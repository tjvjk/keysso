# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WordstatListParams"]


class WordstatListParams(TypedDict, total=False):
    is_main: Annotated[bool, PropertyInfo(alias="isMain")]
    """
    **Список проектов:** `true` — только созданные вручную `false` — все проекты,
    включая созданные автоматически родительскими типами проектов

    **Иерархия проектов:** `Мониторинг » Кластеризатор » Выдача | Wordstat`
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
