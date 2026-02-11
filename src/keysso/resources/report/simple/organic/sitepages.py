# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.report import Base
from .....types.report.base import Base
from .....types.report.simple.organic import sitepage_list_params, sitepage_retrieve_withkeys_params
from .....types.report.simple.organic.sitepage_list_response import SitepageListResponse
from .....types.report.simple.organic.sitepage_retrieve_withkeys_response import SitepageRetrieveWithkeysResponse

__all__ = ["SitepagesResource", "AsyncSitepagesResource"]


class SitepagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SitepagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return SitepagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SitepagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return SitepagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SitepageListResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/organic/sitepages?base=msk&domain=wildberries.ru&sort=it50%7Casc&page=1&per_page=25`

        Args:
          domain: Имя домена

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/report/simple/organic/sitepages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    sitepage_list_params.SitepageListParams,
                ),
            ),
            cast_to=SitepageListResponse,
        )

    def retrieve_withkeys(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SitepageRetrieveWithkeysResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/organic/sitepages/withkeys?base=msk&domain=dodopizza.ru&sort=url%7Casc&page=1&per_page=25`

        Args:
          domain: Имя домена

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/report/simple/organic/sitepages/withkeys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    sitepage_retrieve_withkeys_params.SitepageRetrieveWithkeysParams,
                ),
            ),
            cast_to=SitepageRetrieveWithkeysResponse,
        )


class AsyncSitepagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSitepagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSitepagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSitepagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return AsyncSitepagesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SitepageListResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/organic/sitepages?base=msk&domain=wildberries.ru&sort=it50%7Casc&page=1&per_page=25`

        Args:
          domain: Имя домена

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/report/simple/organic/sitepages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    sitepage_list_params.SitepageListParams,
                ),
            ),
            cast_to=SitepageListResponse,
        )

    async def retrieve_withkeys(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SitepageRetrieveWithkeysResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/organic/sitepages/withkeys?base=msk&domain=dodopizza.ru&sort=url%7Casc&page=1&per_page=25`

        Args:
          domain: Имя домена

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/report/simple/organic/sitepages/withkeys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    sitepage_retrieve_withkeys_params.SitepageRetrieveWithkeysParams,
                ),
            ),
            cast_to=SitepageRetrieveWithkeysResponse,
        )


class SitepagesResourceWithRawResponse:
    def __init__(self, sitepages: SitepagesResource) -> None:
        self._sitepages = sitepages

        self.list = to_raw_response_wrapper(
            sitepages.list,
        )
        self.retrieve_withkeys = to_raw_response_wrapper(
            sitepages.retrieve_withkeys,
        )


class AsyncSitepagesResourceWithRawResponse:
    def __init__(self, sitepages: AsyncSitepagesResource) -> None:
        self._sitepages = sitepages

        self.list = async_to_raw_response_wrapper(
            sitepages.list,
        )
        self.retrieve_withkeys = async_to_raw_response_wrapper(
            sitepages.retrieve_withkeys,
        )


class SitepagesResourceWithStreamingResponse:
    def __init__(self, sitepages: SitepagesResource) -> None:
        self._sitepages = sitepages

        self.list = to_streamed_response_wrapper(
            sitepages.list,
        )
        self.retrieve_withkeys = to_streamed_response_wrapper(
            sitepages.retrieve_withkeys,
        )


class AsyncSitepagesResourceWithStreamingResponse:
    def __init__(self, sitepages: AsyncSitepagesResource) -> None:
        self._sitepages = sitepages

        self.list = async_to_streamed_response_wrapper(
            sitepages.list,
        )
        self.retrieve_withkeys = async_to_streamed_response_wrapper(
            sitepages.retrieve_withkeys,
        )
