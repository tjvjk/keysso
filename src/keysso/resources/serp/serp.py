# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import serp_list_params, serp_create_params
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
from ..._base_client import make_request_options
from ...types.serp_list_response import SerpListResponse
from ...types.serp_create_response import SerpCreateResponse

__all__ = ["SerpResource", "AsyncSerpResource"]


class SerpResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SerpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return SerpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SerpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return SerpResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        data: serp_create_params.Data,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SerpCreateResponse:
        """
        Пример запроса `https://api.keys.so/serp`

        Args:
          data: Данные для парсинга

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/serp",
            body=maybe_transform({"data": data}, serp_create_params.SerpCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SerpCreateResponse,
        )

    def list(
        self,
        *,
        is_main: bool | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SerpListResponse:
        """
        Пример запроса
        `https://api.keys.so/serp?sort=created_at%7Cdesc&page=1&per_page=25`

        Args:
          is_main: **Список проектов:** `true` — только созданные вручную `false` — все проекты,
              включая созданные автоматически родительскими типами проектов

              **Иерархия проектов:** `Мониторинг » Кластеризатор » Выдача | Wordstat`

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
            "/serp",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_main": is_main,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    serp_list_params.SerpListParams,
                ),
            ),
            cast_to=SerpListResponse,
        )


class AsyncSerpResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSerpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncSerpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSerpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncSerpResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        data: serp_create_params.Data,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SerpCreateResponse:
        """
        Пример запроса `https://api.keys.so/serp`

        Args:
          data: Данные для парсинга

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/serp",
            body=await async_maybe_transform({"data": data}, serp_create_params.SerpCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SerpCreateResponse,
        )

    async def list(
        self,
        *,
        is_main: bool | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SerpListResponse:
        """
        Пример запроса
        `https://api.keys.so/serp?sort=created_at%7Cdesc&page=1&per_page=25`

        Args:
          is_main: **Список проектов:** `true` — только созданные вручную `false` — все проекты,
              включая созданные автоматически родительскими типами проектов

              **Иерархия проектов:** `Мониторинг » Кластеризатор » Выдача | Wordstat`

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
            "/serp",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "is_main": is_main,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    serp_list_params.SerpListParams,
                ),
            ),
            cast_to=SerpListResponse,
        )


class SerpResourceWithRawResponse:
    def __init__(self, serp: SerpResource) -> None:
        self._serp = serp

        self.create = to_raw_response_wrapper(
            serp.create,
        )
        self.list = to_raw_response_wrapper(
            serp.list,
        )


class AsyncSerpResourceWithRawResponse:
    def __init__(self, serp: AsyncSerpResource) -> None:
        self._serp = serp

        self.create = async_to_raw_response_wrapper(
            serp.create,
        )
        self.list = async_to_raw_response_wrapper(
            serp.list,
        )


class SerpResourceWithStreamingResponse:
    def __init__(self, serp: SerpResource) -> None:
        self._serp = serp

        self.create = to_streamed_response_wrapper(
            serp.create,
        )
        self.list = to_streamed_response_wrapper(
            serp.list,
        )


class AsyncSerpResourceWithStreamingResponse:
    def __init__(self, serp: AsyncSerpResource) -> None:
        self._serp = serp

        self.create = async_to_streamed_response_wrapper(
            serp.create,
        )
        self.list = async_to_streamed_response_wrapper(
            serp.list,
        )
