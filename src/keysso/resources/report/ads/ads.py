# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rsya import (
    RsyaResource,
    AsyncRsyaResource,
    RsyaResourceWithRawResponse,
    AsyncRsyaResourceWithRawResponse,
    RsyaResourceWithStreamingResponse,
    AsyncRsyaResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AdsResource", "AsyncAdsResource"]


class AdsResource(SyncAPIResource):
    @cached_property
    def rsya(self) -> RsyaResource:
        return RsyaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AdsResourceWithStreamingResponse(self)


class AsyncAdsResource(AsyncAPIResource):
    @cached_property
    def rsya(self) -> AsyncRsyaResource:
        return AsyncRsyaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncAdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncAdsResourceWithStreamingResponse(self)


class AdsResourceWithRawResponse:
    def __init__(self, ads: AdsResource) -> None:
        self._ads = ads

    @cached_property
    def rsya(self) -> RsyaResourceWithRawResponse:
        return RsyaResourceWithRawResponse(self._ads.rsya)


class AsyncAdsResourceWithRawResponse:
    def __init__(self, ads: AsyncAdsResource) -> None:
        self._ads = ads

    @cached_property
    def rsya(self) -> AsyncRsyaResourceWithRawResponse:
        return AsyncRsyaResourceWithRawResponse(self._ads.rsya)


class AdsResourceWithStreamingResponse:
    def __init__(self, ads: AdsResource) -> None:
        self._ads = ads

    @cached_property
    def rsya(self) -> RsyaResourceWithStreamingResponse:
        return RsyaResourceWithStreamingResponse(self._ads.rsya)


class AsyncAdsResourceWithStreamingResponse:
    def __init__(self, ads: AsyncAdsResource) -> None:
        self._ads = ads

    @cached_property
    def rsya(self) -> AsyncRsyaResourceWithStreamingResponse:
        return AsyncRsyaResourceWithStreamingResponse(self._ads.rsya)
