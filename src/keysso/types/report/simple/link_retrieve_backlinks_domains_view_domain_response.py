# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["LinkRetrieveBacklinksDomainsViewDomainResponse", "Data"]


class Data(BaseModel):
    id: Optional[int] = None
    """Идентификатор домена Возможность фильтровать по полю: `нет`"""

    dr: Optional[int] = None
    """
    Рейтинг домена — метрика, которая показывает общую силу ссылочного профиля
    домена в сравнении со всеми остальными сайтами. Возможность фильтровать по полю:
    `да`
    """

    name: Optional[str] = None
    """
    Адрес домена, который ссылается на анализируемый сайт. Возможность фильтровать
    по полю: `да`
    """

    outlinks_active_count: Optional[int] = None
    """
    Количество активных исходящих ссылок с домена на анализируемый домен.
    Возможность фильтровать по полю: `да`
    """

    outlinks_archive_count: Optional[int] = None
    """
    Количество архивных исходящих ссылок с домена на анализируемый домен.
    Возможность фильтровать по полю: `да`
    """

    outlinks_count: Optional[int] = None
    """
    Количество исходящих ссылок с домена на анализируемый домен. Возможность
    фильтровать по полю: `да`
    """

    rel_type: Optional[List[int]] = None
    """
    Атрибут: `0` - `follow` – тег указывает поисковой системе следовать по ссылке и
    передавать свой вес странице, на которую ссылается `1` - `nofollow` – тег
    указывает поисковой системе не передавать свой вес странице, на которую
    ссылается `2` - `sponsored` – тег, используемый для указания рекламных и платных
    ссылок `3` - `ugc` – тег для пользовательского контента Возможность фильтровать
    по полю: `да`
    """

    vis: Optional[int] = None
    """Ориентировочное количество пользователей из органического поиска в сутки.

    Этот параметр рассчитывается по алгоритму, схожему с расчётом видимости сайта,
    но имеет свои понижающие коэффициенты. Возможность фильтровать по полю: `да`
    """


class LinkRetrieveBacklinksDomainsViewDomainResponse(BaseModel):
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

    view: Optional[str] = None
    """Фильтр данных по конкретному домену"""
