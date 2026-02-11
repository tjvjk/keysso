# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.tools import extended_keyword_create_params
from ...._base_client import make_request_options
from ....types.report import Base
from ....types.report.base import Base
from ....types.tools.extended_keyword_create_response import ExtendedKeywordCreateResponse

__all__ = ["ExtendedKeywordsResource", "AsyncExtendedKeywordsResource"]


class ExtendedKeywordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtendedKeywordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return ExtendedKeywordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtendedKeywordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return ExtendedKeywordsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        list: SequenceNotStr[str],
        base: Base | Omit = omit,
        config: extended_keyword_create_params.Config | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtendedKeywordCreateResponse:
        """
        Args:
          list: Массив фраз

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          config: Массив фраз

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tools/extended_keywords",
            body=maybe_transform(
                {
                    "list": list,
                    "base": base,
                    "config": config,
                },
                extended_keyword_create_params.ExtendedKeywordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtendedKeywordCreateResponse,
        )


class AsyncExtendedKeywordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtendedKeywordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtendedKeywordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtendedKeywordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return AsyncExtendedKeywordsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        list: SequenceNotStr[str],
        base: Base | Omit = omit,
        config: extended_keyword_create_params.Config | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtendedKeywordCreateResponse:
        """
        Args:
          list: Массив фраз

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          config: Массив фраз

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tools/extended_keywords",
            body=await async_maybe_transform(
                {
                    "list": list,
                    "base": base,
                    "config": config,
                },
                extended_keyword_create_params.ExtendedKeywordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtendedKeywordCreateResponse,
        )


class ExtendedKeywordsResourceWithRawResponse:
    def __init__(self, extended_keywords: ExtendedKeywordsResource) -> None:
        self._extended_keywords = extended_keywords

        self.create = to_raw_response_wrapper(
            extended_keywords.create,
        )


class AsyncExtendedKeywordsResourceWithRawResponse:
    def __init__(self, extended_keywords: AsyncExtendedKeywordsResource) -> None:
        self._extended_keywords = extended_keywords

        self.create = async_to_raw_response_wrapper(
            extended_keywords.create,
        )


class ExtendedKeywordsResourceWithStreamingResponse:
    def __init__(self, extended_keywords: ExtendedKeywordsResource) -> None:
        self._extended_keywords = extended_keywords

        self.create = to_streamed_response_wrapper(
            extended_keywords.create,
        )


class AsyncExtendedKeywordsResourceWithStreamingResponse:
    def __init__(self, extended_keywords: AsyncExtendedKeywordsResource) -> None:
        self._extended_keywords = extended_keywords

        self.create = async_to_streamed_response_wrapper(
            extended_keywords.create,
        )
