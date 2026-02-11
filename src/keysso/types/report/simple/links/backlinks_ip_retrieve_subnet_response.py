# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["BacklinksIPRetrieveSubnetResponse", "Data"]


class Data(BaseModel):
    backlinks_count: Optional[int] = None
    """Входящих ссылок. Возможность фильтровать по полю: `нет`"""

    domains_count: Optional[int] = None
    """Входящих доменов Возможность фильтровать по полю: `нет`"""

    ips_count: Optional[int] = None
    """IP-адресов. Возможность фильтровать по полю: `нет`"""

    subnet: Optional[str] = None
    """Подсеть. Возможность фильтровать по полю: `да`"""


class BacklinksIPRetrieveSubnetResponse(BaseModel):
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
