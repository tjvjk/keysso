# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .top import (
    TopResource,
    AsyncTopResource,
    TopResourceWithRawResponse,
    AsyncTopResourceWithRawResponse,
    TopResourceWithStreamingResponse,
    AsyncTopResourceWithStreamingResponse,
)
from ...types import zen_retrieve_dashboard_params
from ..._types import Body, Query, Headers, NotGiven, not_given
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
from .channel.channel import (
    ChannelResource,
    AsyncChannelResource,
    ChannelResourceWithRawResponse,
    AsyncChannelResourceWithRawResponse,
    ChannelResourceWithStreamingResponse,
    AsyncChannelResourceWithStreamingResponse,
)
from ...types.zen_retrieve_dashboard_response import ZenRetrieveDashboardResponse

__all__ = ["ZenResource", "AsyncZenResource"]


class ZenResource(SyncAPIResource):
    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def channel(self) -> ChannelResource:
        return ChannelResource(self._client)

    @cached_property
    def with_raw_response(self) -> ZenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return ZenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return ZenResourceWithStreamingResponse(self)

    def retrieve_dashboard(
        self,
        *,
        channel: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZenRetrieveDashboardResponse:
        """
        Пример запроса
        `https://api.keys.so/zen/dashboard?channel=Text.ru+-+%D0%BF%D0%B8%D1%88%D0%B8+%D0%B8+%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8F%D0%B9`

        Args:
          channel: Имя или урл канала

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/zen/dashboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"channel": channel}, zen_retrieve_dashboard_params.ZenRetrieveDashboardParams),
            ),
            cast_to=ZenRetrieveDashboardResponse,
        )


class AsyncZenResource(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def channel(self) -> AsyncChannelResource:
        return AsyncChannelResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncZenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncZenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncZenResourceWithStreamingResponse(self)

    async def retrieve_dashboard(
        self,
        *,
        channel: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ZenRetrieveDashboardResponse:
        """
        Пример запроса
        `https://api.keys.so/zen/dashboard?channel=Text.ru+-+%D0%BF%D0%B8%D1%88%D0%B8+%D0%B8+%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D1%8F%D0%B9`

        Args:
          channel: Имя или урл канала

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/zen/dashboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"channel": channel}, zen_retrieve_dashboard_params.ZenRetrieveDashboardParams
                ),
            ),
            cast_to=ZenRetrieveDashboardResponse,
        )


class ZenResourceWithRawResponse:
    def __init__(self, zen: ZenResource) -> None:
        self._zen = zen

        self.retrieve_dashboard = to_raw_response_wrapper(
            zen.retrieve_dashboard,
        )

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._zen.top)

    @cached_property
    def channel(self) -> ChannelResourceWithRawResponse:
        return ChannelResourceWithRawResponse(self._zen.channel)


class AsyncZenResourceWithRawResponse:
    def __init__(self, zen: AsyncZenResource) -> None:
        self._zen = zen

        self.retrieve_dashboard = async_to_raw_response_wrapper(
            zen.retrieve_dashboard,
        )

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._zen.top)

    @cached_property
    def channel(self) -> AsyncChannelResourceWithRawResponse:
        return AsyncChannelResourceWithRawResponse(self._zen.channel)


class ZenResourceWithStreamingResponse:
    def __init__(self, zen: ZenResource) -> None:
        self._zen = zen

        self.retrieve_dashboard = to_streamed_response_wrapper(
            zen.retrieve_dashboard,
        )

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._zen.top)

    @cached_property
    def channel(self) -> ChannelResourceWithStreamingResponse:
        return ChannelResourceWithStreamingResponse(self._zen.channel)


class AsyncZenResourceWithStreamingResponse:
    def __init__(self, zen: AsyncZenResource) -> None:
        self._zen = zen

        self.retrieve_dashboard = async_to_streamed_response_wrapper(
            zen.retrieve_dashboard,
        )

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._zen.top)

    @cached_property
    def channel(self) -> AsyncChannelResourceWithStreamingResponse:
        return AsyncChannelResourceWithStreamingResponse(self._zen.channel)
