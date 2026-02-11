# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types.zen import top_list_channels_params
from ..._base_client import make_request_options
from ...types.zen.top_list_channels_response import TopListChannelsResponse

__all__ = ["TopResource", "AsyncTopResource"]


class TopResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return TopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return TopResourceWithStreamingResponse(self)

    def list_channels(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopListChannelsResponse:
        """
        Пример запроса
        `https://api.keys.so/zen/top/channels?sort=viewsRank%7Casc&page=1&per_page=25`

        Args:
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
            "/zen/top/channels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    top_list_channels_params.TopListChannelsParams,
                ),
            ),
            cast_to=TopListChannelsResponse,
        )


class AsyncTopResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncTopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncTopResourceWithStreamingResponse(self)

    async def list_channels(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopListChannelsResponse:
        """
        Пример запроса
        `https://api.keys.so/zen/top/channels?sort=viewsRank%7Casc&page=1&per_page=25`

        Args:
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
            "/zen/top/channels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    top_list_channels_params.TopListChannelsParams,
                ),
            ),
            cast_to=TopListChannelsResponse,
        )


class TopResourceWithRawResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

        self.list_channels = to_raw_response_wrapper(
            top.list_channels,
        )


class AsyncTopResourceWithRawResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

        self.list_channels = async_to_raw_response_wrapper(
            top.list_channels,
        )


class TopResourceWithStreamingResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

        self.list_channels = to_streamed_response_wrapper(
            top.list_channels,
        )


class AsyncTopResourceWithStreamingResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

        self.list_channels = async_to_streamed_response_wrapper(
            top.list_channels,
        )
