# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..base import Base

__all__ = ["LinkDomainsBatchParams", "Data", "Params"]


class LinkDomainsBatchParams(TypedDict, total=False):
    data: Required[Data]
    """Данные для анализа"""

    base: Base
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

    params: Params
    """Параметры запроса в теле"""


class Data(TypedDict, total=False):
    """Данные для анализа"""

    domains: Required[str]


class Params(TypedDict, total=False):
    """Параметры запроса в теле"""

    filter: str
    """
    Подробнее про фильтрацию смотрите в разделе
    [Фильтрация данных](#tag/Filtraciya-dannyh)

    Примеры запросов: купить слона в розницу купить слона -оптом

    Также можно использовать общий перечень минус-слов в конце списка. Пример:

    купить слона недорого -оптом -игрушечный
    [Список незначимых слов при фильтрации и минусации](https://snowballstem.org/algorithms/russian/stop.txt)
    (слова можно использовать в комбинации с другими словами).

    Пример:
    `wordLIKE%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C%20%D1%81%D0%BB%D0%BE%D0%BD%D0%B0%20%D0%B2%20%D1%80%D0%BE%D0%B7%D0%BD%D0%B8%D1%86%D1%83%0A%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C%20%D1%81%D0%BB%D0%BE%D0%BD%D0%B0%20-%D0%BE%D0%BF%D1%82%D0%BE%D0%BC%0A%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C%20%D1%81%D0%BB%D0%BE%D0%BD%D0%B0%20%D0%BD%D0%B5%D0%B4%D0%BE%D1%80%D0%BE%D0%B3%D0%BE%0A-%D0%BE%D0%BF%D1%82%D0%BE%D0%BC%0A-%D0%B8%D0%B3%D1%80%D1%83%D1%88%D0%B5%D1%87%D0%BD%D1%8B%D0%B9`
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
