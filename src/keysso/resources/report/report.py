# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .owner import (
    OwnerResource,
    AsyncOwnerResource,
    OwnerResourceWithRawResponse,
    AsyncOwnerResourceWithRawResponse,
    OwnerResourceWithStreamingResponse,
    AsyncOwnerResourceWithStreamingResponse,
)
from ...types import (
    report_compare_context_params,
    report_compare_organic_params,
    report_compare_backlinks_params,
    report_create_system_keywords_params,
)
from .ads.ads import (
    AdsResource,
    AsyncAdsResource,
    AdsResourceWithRawResponse,
    AsyncAdsResourceWithRawResponse,
    AdsResourceWithStreamingResponse,
    AsyncAdsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .group.group import (
    GroupResource,
    AsyncGroupResource,
    GroupResourceWithRawResponse,
    AsyncGroupResourceWithRawResponse,
    GroupResourceWithStreamingResponse,
    AsyncGroupResourceWithStreamingResponse,
)
from .simple.simple import (
    SimpleResource,
    AsyncSimpleResource,
    SimpleResourceWithRawResponse,
    AsyncSimpleResourceWithRawResponse,
    SimpleResourceWithStreamingResponse,
    AsyncSimpleResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.report import Base
from ...types.report.base import Base
from ...types.report_compare_context_response import ReportCompareContextResponse
from ...types.report_compare_organic_response import ReportCompareOrganicResponse
from ...types.report_compare_backlinks_response import ReportCompareBacklinksResponse
from ...types.report_create_system_keywords_response import ReportCreateSystemKeywordsResponse

__all__ = ["ReportResource", "AsyncReportResource"]


class ReportResource(SyncAPIResource):
    @cached_property
    def simple(self) -> SimpleResource:
        return SimpleResource(self._client)

    @cached_property
    def group(self) -> GroupResource:
        return GroupResource(self._client)

    @cached_property
    def ads(self) -> AdsResource:
        return AdsResource(self._client)

    @cached_property
    def owner(self) -> OwnerResource:
        return OwnerResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return ReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return ReportResourceWithStreamingResponse(self)

    def compare_backlinks(
        self,
        *,
        excl: str,
        incl: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        view: Literal["organic", "context", "backlinks"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCompareBacklinksResponse:
        """
        Пример запроса
        `https://api.keys.so/report/compare?base=msk&incl=keys.so,text.ru&excl=&view=backlinks&sort=numurl%7Cdesc&page=1&per_page=25`

        Args:
          excl: Список доменов через запятую

          incl: Список доменов через запятую

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          filter: Подробнее про фильтрацию смотрите в разделе
              [Фильтрация данных](#tag/Filtraciya-dannyh)

          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          view: Тип отчета `backlinks`, для данного инструмента необходимо явно указывать данный
              тип отчета

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/report/compare?view=backlinks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "excl": excl,
                        "incl": incl,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "view": view,
                    },
                    report_compare_backlinks_params.ReportCompareBacklinksParams,
                ),
            ),
            cast_to=ReportCompareBacklinksResponse,
        )

    def compare_context(
        self,
        *,
        excl: str,
        incl: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        view: Literal["organic", "context", "backlinks"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCompareContextResponse:
        """
        Пример запроса
        `https://api.keys.so/report/compare?base=msk&incl=keys.so,text.ru&excl=&view=organic&sort=numwords%7Cdesc&page=1&per_page=25`

        Args:
          excl: Список доменов через запятую

          incl: Список доменов через запятую

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          filter: Подробнее про фильтрацию смотрите в разделе
              [Фильтрация данных](#tag/Filtraciya-dannyh)

          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          view: Тип отчета `context`, для данного инструмента необходимо явно указывать данный
              тип отчета

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/report/compare?view=context",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "excl": excl,
                        "incl": incl,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "view": view,
                    },
                    report_compare_context_params.ReportCompareContextParams,
                ),
            ),
            cast_to=ReportCompareContextResponse,
        )

    def compare_organic(
        self,
        *,
        excl: str,
        incl: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        view: Literal["organic", "context", "backlinks"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCompareOrganicResponse:
        """
        Пример запроса
        `https://api.keys.so/report/compare?base=msk&incl=keys.so,text.ru&excl=&view=organic&sort=numwords%7Cdesc&page=1&per_page=25`

        Args:
          excl: Список доменов через запятую

          incl: Список доменов через запятую

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          filter: Подробнее про фильтрацию смотрите в разделе
              [Фильтрация данных](#tag/Filtraciya-dannyh)

          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          view: Тип отчета `organic`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/report/compare?view=organic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "excl": excl,
                        "incl": incl,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "view": view,
                    },
                    report_compare_organic_params.ReportCompareOrganicParams,
                ),
            ),
            cast_to=ReportCompareOrganicResponse,
        )

    def create_system_keywords(
        self,
        *,
        hideadult: bool,
        strict: bool,
        page: int | Omit = omit,
        sort: str | Omit = omit,
        params: report_create_system_keywords_params.Params | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCreateSystemKeywordsResponse:
        """
        Пример запроса
        `https://api.keys.so/report/system_keywords?strict=true&hideadult=true`

        Args:
          hideadult: Скрыть запросы тематики 18+

          strict: Нечеткий поиск(поддержка склонения слов, изменения их порядка, не более 1 000
              000 результатов)

          page: Порядковый номер страницы результатов

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          params: Параметры запроса в теле

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/report/system_keywords",
            body=maybe_transform(
                {"params": params}, report_create_system_keywords_params.ReportCreateSystemKeywordsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "hideadult": hideadult,
                        "strict": strict,
                        "page": page,
                        "sort": sort,
                    },
                    report_create_system_keywords_params.ReportCreateSystemKeywordsParams,
                ),
            ),
            cast_to=ReportCreateSystemKeywordsResponse,
        )


class AsyncReportResource(AsyncAPIResource):
    @cached_property
    def simple(self) -> AsyncSimpleResource:
        return AsyncSimpleResource(self._client)

    @cached_property
    def group(self) -> AsyncGroupResource:
        return AsyncGroupResource(self._client)

    @cached_property
    def ads(self) -> AsyncAdsResource:
        return AsyncAdsResource(self._client)

    @cached_property
    def owner(self) -> AsyncOwnerResource:
        return AsyncOwnerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncReportResourceWithStreamingResponse(self)

    async def compare_backlinks(
        self,
        *,
        excl: str,
        incl: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        view: Literal["organic", "context", "backlinks"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCompareBacklinksResponse:
        """
        Пример запроса
        `https://api.keys.so/report/compare?base=msk&incl=keys.so,text.ru&excl=&view=backlinks&sort=numurl%7Cdesc&page=1&per_page=25`

        Args:
          excl: Список доменов через запятую

          incl: Список доменов через запятую

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          filter: Подробнее про фильтрацию смотрите в разделе
              [Фильтрация данных](#tag/Filtraciya-dannyh)

          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          view: Тип отчета `backlinks`, для данного инструмента необходимо явно указывать данный
              тип отчета

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/report/compare?view=backlinks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "excl": excl,
                        "incl": incl,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "view": view,
                    },
                    report_compare_backlinks_params.ReportCompareBacklinksParams,
                ),
            ),
            cast_to=ReportCompareBacklinksResponse,
        )

    async def compare_context(
        self,
        *,
        excl: str,
        incl: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        view: Literal["organic", "context", "backlinks"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCompareContextResponse:
        """
        Пример запроса
        `https://api.keys.so/report/compare?base=msk&incl=keys.so,text.ru&excl=&view=organic&sort=numwords%7Cdesc&page=1&per_page=25`

        Args:
          excl: Список доменов через запятую

          incl: Список доменов через запятую

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          filter: Подробнее про фильтрацию смотрите в разделе
              [Фильтрация данных](#tag/Filtraciya-dannyh)

          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          view: Тип отчета `context`, для данного инструмента необходимо явно указывать данный
              тип отчета

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/report/compare?view=context",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "excl": excl,
                        "incl": incl,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "view": view,
                    },
                    report_compare_context_params.ReportCompareContextParams,
                ),
            ),
            cast_to=ReportCompareContextResponse,
        )

    async def compare_organic(
        self,
        *,
        excl: str,
        incl: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        view: Literal["organic", "context", "backlinks"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCompareOrganicResponse:
        """
        Пример запроса
        `https://api.keys.so/report/compare?base=msk&incl=keys.so,text.ru&excl=&view=organic&sort=numwords%7Cdesc&page=1&per_page=25`

        Args:
          excl: Список доменов через запятую

          incl: Список доменов через запятую

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          filter: Подробнее про фильтрацию смотрите в разделе
              [Фильтрация данных](#tag/Filtraciya-dannyh)

          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          view: Тип отчета `organic`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/report/compare?view=organic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "excl": excl,
                        "incl": incl,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "view": view,
                    },
                    report_compare_organic_params.ReportCompareOrganicParams,
                ),
            ),
            cast_to=ReportCompareOrganicResponse,
        )

    async def create_system_keywords(
        self,
        *,
        hideadult: bool,
        strict: bool,
        page: int | Omit = omit,
        sort: str | Omit = omit,
        params: report_create_system_keywords_params.Params | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCreateSystemKeywordsResponse:
        """
        Пример запроса
        `https://api.keys.so/report/system_keywords?strict=true&hideadult=true`

        Args:
          hideadult: Скрыть запросы тематики 18+

          strict: Нечеткий поиск(поддержка склонения слов, изменения их порядка, не более 1 000
              000 результатов)

          page: Порядковый номер страницы результатов

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          params: Параметры запроса в теле

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/report/system_keywords",
            body=await async_maybe_transform(
                {"params": params}, report_create_system_keywords_params.ReportCreateSystemKeywordsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "hideadult": hideadult,
                        "strict": strict,
                        "page": page,
                        "sort": sort,
                    },
                    report_create_system_keywords_params.ReportCreateSystemKeywordsParams,
                ),
            ),
            cast_to=ReportCreateSystemKeywordsResponse,
        )


class ReportResourceWithRawResponse:
    def __init__(self, report: ReportResource) -> None:
        self._report = report

        self.compare_backlinks = to_raw_response_wrapper(
            report.compare_backlinks,
        )
        self.compare_context = to_raw_response_wrapper(
            report.compare_context,
        )
        self.compare_organic = to_raw_response_wrapper(
            report.compare_organic,
        )
        self.create_system_keywords = to_raw_response_wrapper(
            report.create_system_keywords,
        )

    @cached_property
    def simple(self) -> SimpleResourceWithRawResponse:
        return SimpleResourceWithRawResponse(self._report.simple)

    @cached_property
    def group(self) -> GroupResourceWithRawResponse:
        return GroupResourceWithRawResponse(self._report.group)

    @cached_property
    def ads(self) -> AdsResourceWithRawResponse:
        return AdsResourceWithRawResponse(self._report.ads)

    @cached_property
    def owner(self) -> OwnerResourceWithRawResponse:
        return OwnerResourceWithRawResponse(self._report.owner)


class AsyncReportResourceWithRawResponse:
    def __init__(self, report: AsyncReportResource) -> None:
        self._report = report

        self.compare_backlinks = async_to_raw_response_wrapper(
            report.compare_backlinks,
        )
        self.compare_context = async_to_raw_response_wrapper(
            report.compare_context,
        )
        self.compare_organic = async_to_raw_response_wrapper(
            report.compare_organic,
        )
        self.create_system_keywords = async_to_raw_response_wrapper(
            report.create_system_keywords,
        )

    @cached_property
    def simple(self) -> AsyncSimpleResourceWithRawResponse:
        return AsyncSimpleResourceWithRawResponse(self._report.simple)

    @cached_property
    def group(self) -> AsyncGroupResourceWithRawResponse:
        return AsyncGroupResourceWithRawResponse(self._report.group)

    @cached_property
    def ads(self) -> AsyncAdsResourceWithRawResponse:
        return AsyncAdsResourceWithRawResponse(self._report.ads)

    @cached_property
    def owner(self) -> AsyncOwnerResourceWithRawResponse:
        return AsyncOwnerResourceWithRawResponse(self._report.owner)


class ReportResourceWithStreamingResponse:
    def __init__(self, report: ReportResource) -> None:
        self._report = report

        self.compare_backlinks = to_streamed_response_wrapper(
            report.compare_backlinks,
        )
        self.compare_context = to_streamed_response_wrapper(
            report.compare_context,
        )
        self.compare_organic = to_streamed_response_wrapper(
            report.compare_organic,
        )
        self.create_system_keywords = to_streamed_response_wrapper(
            report.create_system_keywords,
        )

    @cached_property
    def simple(self) -> SimpleResourceWithStreamingResponse:
        return SimpleResourceWithStreamingResponse(self._report.simple)

    @cached_property
    def group(self) -> GroupResourceWithStreamingResponse:
        return GroupResourceWithStreamingResponse(self._report.group)

    @cached_property
    def ads(self) -> AdsResourceWithStreamingResponse:
        return AdsResourceWithStreamingResponse(self._report.ads)

    @cached_property
    def owner(self) -> OwnerResourceWithStreamingResponse:
        return OwnerResourceWithStreamingResponse(self._report.owner)


class AsyncReportResourceWithStreamingResponse:
    def __init__(self, report: AsyncReportResource) -> None:
        self._report = report

        self.compare_backlinks = async_to_streamed_response_wrapper(
            report.compare_backlinks,
        )
        self.compare_context = async_to_streamed_response_wrapper(
            report.compare_context,
        )
        self.compare_organic = async_to_streamed_response_wrapper(
            report.compare_organic,
        )
        self.create_system_keywords = async_to_streamed_response_wrapper(
            report.create_system_keywords,
        )

    @cached_property
    def simple(self) -> AsyncSimpleResourceWithStreamingResponse:
        return AsyncSimpleResourceWithStreamingResponse(self._report.simple)

    @cached_property
    def group(self) -> AsyncGroupResourceWithStreamingResponse:
        return AsyncGroupResourceWithStreamingResponse(self._report.group)

    @cached_property
    def ads(self) -> AsyncAdsResourceWithStreamingResponse:
        return AsyncAdsResourceWithStreamingResponse(self._report.ads)

    @cached_property
    def owner(self) -> AsyncOwnerResourceWithStreamingResponse:
        return AsyncOwnerResourceWithStreamingResponse(self._report.owner)
