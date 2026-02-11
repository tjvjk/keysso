# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["LinkRetrieveBacklinksAnchorResponse", "Data"]


class Data(BaseModel):
    anchor: Optional[str] = None
    """Анкор.

    Кликабельная текстовая часть ссылки, которую пользователи нажимают для перехода
    на анализируемый сайт. Возможность фильтровать по полю: `нет`
    """

    backlinks_count: Optional[int] = None
    """Кол-во ссылок Возможность фильтровать по полю: `нет`"""

    link_type: Optional[int] = None
    """
    Тип: `0` - `картинка` – ссылка представляет собой графическое изображение `1` -
    `текст` – ссылка представляет собой текст `2` - `форма` – на странице источнике
    в атрибуте «action» тега «form» указан целевой URL `3` - `фрейм` – на странице
    источнике в атрибуте «src» тега «iframe» указан целевой URL Возможность
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

    statuses: Optional[List[int]] = None
    """
    Статус: `1` - `активная` – ссылка присутствует на странице и ведёт на целевой
    URL `10` - архивная – при повторном обходе источника ссылка не была обнаружена,
    либо ссылается на уже несуществующую страницу. Возможность фильтровать по полю:
    `да`
    """

    words_count: Optional[int] = None
    """Количество слов в анкоре ссылки. Возможность фильтровать по полю: `да`"""


class LinkRetrieveBacklinksAnchorResponse(BaseModel):
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
