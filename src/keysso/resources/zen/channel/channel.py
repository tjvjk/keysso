# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .new.new import (
    NewResource,
    AsyncNewResource,
    NewResourceWithRawResponse,
    AsyncNewResourceWithRawResponse,
    NewResourceWithStreamingResponse,
    AsyncNewResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.zen import channel_list_publications_params
from ...._base_client import make_request_options
from ....types.zen.channel_list_publications_response import ChannelListPublicationsResponse

__all__ = ["ChannelResource", "AsyncChannelResource"]


class ChannelResource(SyncAPIResource):
    @cached_property
    def new(self) -> NewResource:
        return NewResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChannelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return ChannelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return ChannelResourceWithStreamingResponse(self)

    def list_publications(
        self,
        *,
        channel: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelListPublicationsResponse:
        """
        Пример запроса
        `https://api.keys.so/zen/channel/publications?channel=5e428f13bf8d3263221b5924&sort=datePublishAt%7Cdesc&page=1&per_page=25`

        Args:
          channel: Хеш, имя или урл канала для поиска

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
            "/zen/channel/publications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    channel_list_publications_params.ChannelListPublicationsParams,
                ),
            ),
            cast_to=ChannelListPublicationsResponse,
        )


class AsyncChannelResource(AsyncAPIResource):
    @cached_property
    def new(self) -> AsyncNewResource:
        return AsyncNewResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChannelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncChannelResourceWithStreamingResponse(self)

    async def list_publications(
        self,
        *,
        channel: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelListPublicationsResponse:
        """
        Пример запроса
        `https://api.keys.so/zen/channel/publications?channel=5e428f13bf8d3263221b5924&sort=datePublishAt%7Cdesc&page=1&per_page=25`

        Args:
          channel: Хеш, имя или урл канала для поиска

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
            "/zen/channel/publications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    channel_list_publications_params.ChannelListPublicationsParams,
                ),
            ),
            cast_to=ChannelListPublicationsResponse,
        )


class ChannelResourceWithRawResponse:
    def __init__(self, channel: ChannelResource) -> None:
        self._channel = channel

        self.list_publications = to_raw_response_wrapper(
            channel.list_publications,
        )

    @cached_property
    def new(self) -> NewResourceWithRawResponse:
        return NewResourceWithRawResponse(self._channel.new)


class AsyncChannelResourceWithRawResponse:
    def __init__(self, channel: AsyncChannelResource) -> None:
        self._channel = channel

        self.list_publications = async_to_raw_response_wrapper(
            channel.list_publications,
        )

    @cached_property
    def new(self) -> AsyncNewResourceWithRawResponse:
        return AsyncNewResourceWithRawResponse(self._channel.new)


class ChannelResourceWithStreamingResponse:
    def __init__(self, channel: ChannelResource) -> None:
        self._channel = channel

        self.list_publications = to_streamed_response_wrapper(
            channel.list_publications,
        )

    @cached_property
    def new(self) -> NewResourceWithStreamingResponse:
        return NewResourceWithStreamingResponse(self._channel.new)


class AsyncChannelResourceWithStreamingResponse:
    def __init__(self, channel: AsyncChannelResource) -> None:
        self._channel = channel

        self.list_publications = async_to_streamed_response_wrapper(
            channel.list_publications,
        )

    @cached_property
    def new(self) -> AsyncNewResourceWithStreamingResponse:
        return AsyncNewResourceWithStreamingResponse(self._channel.new)
