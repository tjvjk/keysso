# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ReportCompareBacklinksResponse", "Data"]


class Data(BaseModel):
    dr: Optional[int] = None
    """
    Рейтинг домена — метрика, которая показывает общую силу ссылочного профиля
    домена в сравнении со всеми остальными сайтами
    """

    ip: Optional[str] = None
    """IP-адрес сайта, который ссылается на анализируемый домен"""

    it10: Optional[int] = None
    """Запросов сайта в топ 10"""

    it50: Optional[int] = None
    """Запросов сайта в топ 50"""

    name: Optional[str] = None
    """Имя домена"""

    numlink: Optional[int] = None
    """Ссылок"""

    numurl: Optional[int] = None
    """Страниц"""

    vis: Optional[int] = None
    """Оценка трафика с поиска"""


class ReportCompareBacklinksResponse(BaseModel):
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
