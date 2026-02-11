# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RsyaRetrieveParams"]


class RsyaRetrieveParams(TypedDict, total=False):
    filter: str
    """
    Подробнее про фильтрацию смотрите в разделе
    [Фильтрация данных](#tag/Filtraciya-dannyh)
    """

    grouping_by: Annotated[Literal["img_path", "inn", "domain", "erir"], PropertyInfo(alias="groupingBy")]
    """Группировка. Данный параметр работает только при наличии фильтра.

    `img_path` - по изображению

    `inn` - по рекламодателю(ИНН)

    `domain` - по домену

    `erir` - по ЕРИР
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
