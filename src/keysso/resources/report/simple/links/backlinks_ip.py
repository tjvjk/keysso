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
from .....types.report.simple.links import (
    backlinks_ip_retrieve_subnet_params,
    backlinks_ip_retrieve_backlinks_ip_params,
)
from .....types.report.simple.links.backlinks_ip_retrieve_subnet_response import BacklinksIPRetrieveSubnetResponse
from .....types.report.simple.links.backlinks_ip_retrieve_backlinks_ip_response import (
    BacklinksIPRetrieveBacklinksIPResponse,
)

__all__ = ["BacklinksIPResource", "AsyncBacklinksIPResource"]


class BacklinksIPResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BacklinksIPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return BacklinksIPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BacklinksIPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return BacklinksIPResourceWithStreamingResponse(self)

    def retrieve_backlinks_ip(
        self,
        *,
        domain: str,
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
    ) -> BacklinksIPRetrieveBacklinksIPResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/backlinks-ip?domain=wildberries.ru&sort=backlinks_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/backlinks-ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    backlinks_ip_retrieve_backlinks_ip_params.BacklinksIPRetrieveBacklinksIPParams,
                ),
            ),
            cast_to=BacklinksIPRetrieveBacklinksIPResponse,
        )

    def retrieve_subnet(
        self,
        *,
        domain: str,
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
    ) -> BacklinksIPRetrieveSubnetResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/backlinks-ip/subnet?domain=wildberries.ru&sort=domains_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/backlinks-ip/subnet",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    backlinks_ip_retrieve_subnet_params.BacklinksIPRetrieveSubnetParams,
                ),
            ),
            cast_to=BacklinksIPRetrieveSubnetResponse,
        )


class AsyncBacklinksIPResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBacklinksIPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBacklinksIPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBacklinksIPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return AsyncBacklinksIPResourceWithStreamingResponse(self)

    async def retrieve_backlinks_ip(
        self,
        *,
        domain: str,
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
    ) -> BacklinksIPRetrieveBacklinksIPResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/backlinks-ip?domain=wildberries.ru&sort=backlinks_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/backlinks-ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    backlinks_ip_retrieve_backlinks_ip_params.BacklinksIPRetrieveBacklinksIPParams,
                ),
            ),
            cast_to=BacklinksIPRetrieveBacklinksIPResponse,
        )

    async def retrieve_subnet(
        self,
        *,
        domain: str,
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
    ) -> BacklinksIPRetrieveSubnetResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/backlinks-ip/subnet?domain=wildberries.ru&sort=domains_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/backlinks-ip/subnet",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    backlinks_ip_retrieve_subnet_params.BacklinksIPRetrieveSubnetParams,
                ),
            ),
            cast_to=BacklinksIPRetrieveSubnetResponse,
        )


class BacklinksIPResourceWithRawResponse:
    def __init__(self, backlinks_ip: BacklinksIPResource) -> None:
        self._backlinks_ip = backlinks_ip

        self.retrieve_backlinks_ip = to_raw_response_wrapper(
            backlinks_ip.retrieve_backlinks_ip,
        )
        self.retrieve_subnet = to_raw_response_wrapper(
            backlinks_ip.retrieve_subnet,
        )


class AsyncBacklinksIPResourceWithRawResponse:
    def __init__(self, backlinks_ip: AsyncBacklinksIPResource) -> None:
        self._backlinks_ip = backlinks_ip

        self.retrieve_backlinks_ip = async_to_raw_response_wrapper(
            backlinks_ip.retrieve_backlinks_ip,
        )
        self.retrieve_subnet = async_to_raw_response_wrapper(
            backlinks_ip.retrieve_subnet,
        )


class BacklinksIPResourceWithStreamingResponse:
    def __init__(self, backlinks_ip: BacklinksIPResource) -> None:
        self._backlinks_ip = backlinks_ip

        self.retrieve_backlinks_ip = to_streamed_response_wrapper(
            backlinks_ip.retrieve_backlinks_ip,
        )
        self.retrieve_subnet = to_streamed_response_wrapper(
            backlinks_ip.retrieve_subnet,
        )


class AsyncBacklinksIPResourceWithStreamingResponse:
    def __init__(self, backlinks_ip: AsyncBacklinksIPResource) -> None:
        self._backlinks_ip = backlinks_ip

        self.retrieve_backlinks_ip = async_to_streamed_response_wrapper(
            backlinks_ip.retrieve_backlinks_ip,
        )
        self.retrieve_subnet = async_to_streamed_response_wrapper(
            backlinks_ip.retrieve_subnet,
        )
