# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GroupListResponse", "Data"]


class Data(BaseModel):
    access_date: Optional[str] = None
    """Последнее обновление"""

    base: Optional[str] = None
    """База по которой построен отчет"""

    can_change_owner: Optional[bool] = FieldInfo(alias="canChangeOwner", default=None)
    """Возможность сменить владельца"""

    can_delete: Optional[bool] = FieldInfo(alias="canDelete", default=None)
    """Возможность удаления отчета"""

    create_date: Optional[str] = None
    """Дата создания отчета"""

    name: Optional[str] = None
    """Имя отчета"""

    owner: Optional[str] = None
    """Владелец отчета"""

    rid: Optional[str] = None
    """Идентификатор отчета"""

    state: Optional[int] = None
    """Статус отчета

    `1` - В обработке

    `2` - Ошибка обработки

    `10` - Обработка завершена
    """

    top: Optional[int] = None
    """Охват позиций"""


class GroupListResponse(BaseModel):
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
