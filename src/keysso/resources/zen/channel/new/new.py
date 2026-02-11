# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .top import (
    TopResource,
    AsyncTopResource,
    TopResourceWithRawResponse,
    AsyncTopResourceWithRawResponse,
    TopResourceWithStreamingResponse,
    AsyncTopResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["NewResource", "AsyncNewResource"]


class NewResource(SyncAPIResource):
    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def with_raw_response(self) -> NewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return NewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return NewResourceWithStreamingResponse(self)


class AsyncNewResource(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncNewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncNewResourceWithStreamingResponse(self)


class NewResourceWithRawResponse:
    def __init__(self, new: NewResource) -> None:
        self._new = new

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._new.top)


class AsyncNewResourceWithRawResponse:
    def __init__(self, new: AsyncNewResource) -> None:
        self._new = new

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._new.top)


class NewResourceWithStreamingResponse:
    def __init__(self, new: NewResource) -> None:
        self._new = new

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._new.top)


class AsyncNewResourceWithStreamingResponse:
    def __init__(self, new: AsyncNewResource) -> None:
        self._new = new

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._new.top)
