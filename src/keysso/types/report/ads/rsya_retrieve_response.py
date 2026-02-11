# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["RsyaRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Идентификатор объявления. Возможность фильтровать по полю: `нет`"""

    body: Optional[str] = None
    """Описание. Возможность фильтровать по полю: `да`"""

    company_name: Optional[str] = None
    """Название компании. Возможность фильтровать по полю: `да`"""

    diff_days: Optional[int] = None
    """Дней в открутке. Возможность фильтровать по полю: `да`"""

    domain: Optional[str] = None
    """Домен. Возможность фильтровать по полю: `да`"""

    files: Optional[List[str]] = None
    """Файл объявления. Возможность фильтровать по полю: `нет`"""

    found_at: Optional[object] = None
    """Дата обнаружения. Возможность фильтровать по полю: `да`"""

    group: Optional[List[object]] = None
    """
    Массив сгруппированных объявлений возвращается только в случае, если передан
    фильтр и `groupingBy` параметр. Структура вложенных объектов аналогична
    структуре в поле `data`
    """

    hash: Optional[str] = None
    """Идентификатор группы если передан фильтр и `groupingBy` параметр."""

    legal: Optional[str] = None
    """Данные рекламодателя. Возможность фильтровать по полю: `да`"""

    region_name: Optional[str] = None
    """Регион показа. Возможность фильтровать по полю: `да`"""

    second_title: Optional[str] = None
    """Альтернативный заголовок объявления. Возможность фильтровать по полю: `да`"""

    size: Optional[str] = None
    """Размер. Возможность фильтровать по полю: `нет`"""

    target_url: Optional[str] = None
    """Целевой URL. Возможность фильтровать по полю: `да`"""

    title: Optional[str] = None
    """Заголовок объявления. Возможность фильтровать по полю: `да`"""

    type: Optional[Literal["Google Play", "App Store", "Медиа", "Директ", "Видео"]] = None
    """Тип объявления. Возможность фильтровать по полю: `да`"""

    updated_at: Optional[str] = None
    """Дата обновления. Возможность фильтровать по полю: `да`"""

    view_cnt: Optional[int] = None
    """Показов. Возможность фильтровать по полю: `да`"""


class RsyaRetrieveResponse(BaseModel):
    current_page: Optional[int] = None
    """Текущая страница"""

    data: Optional[List[Data]] = None
    """Данные ответа"""

    last_page: Optional[int] = None
    """Последняя страница"""

    message: Optional[str] = None
    """Всего записей"""

    per_page: Optional[int] = None
    """Записей на странице"""

    total: Optional[int] = None
    """Всего записей"""
