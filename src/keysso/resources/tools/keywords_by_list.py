# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...types.tools import keywords_by_list_create_params
from ..._base_client import make_request_options
from ...types.report import Base
from ...types.report.base import Base
from ...types.tools.keywords_by_list_create_response import KeywordsByListCreateResponse

__all__ = ["KeywordsByListResource", "AsyncKeywordsByListResource"]


class KeywordsByListResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeywordsByListResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return KeywordsByListResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeywordsByListResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return KeywordsByListResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        list: Iterable[object],
        base: Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeywordsByListCreateResponse:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tools/keywords_by_list",
            body=maybe_transform(
                {
                    "list": list,
                    "base": base,
                },
                keywords_by_list_create_params.KeywordsByListCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordsByListCreateResponse,
        )


class AsyncKeywordsByListResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeywordsByListResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncKeywordsByListResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeywordsByListResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncKeywordsByListResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        list: Iterable[object],
        base: Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeywordsByListCreateResponse:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tools/keywords_by_list",
            body=await async_maybe_transform(
                {
                    "list": list,
                    "base": base,
                },
                keywords_by_list_create_params.KeywordsByListCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordsByListCreateResponse,
        )


class KeywordsByListResourceWithRawResponse:
    def __init__(self, keywords_by_list: KeywordsByListResource) -> None:
        self._keywords_by_list = keywords_by_list

        self.create = to_raw_response_wrapper(
            keywords_by_list.create,
        )


class AsyncKeywordsByListResourceWithRawResponse:
    def __init__(self, keywords_by_list: AsyncKeywordsByListResource) -> None:
        self._keywords_by_list = keywords_by_list

        self.create = async_to_raw_response_wrapper(
            keywords_by_list.create,
        )


class KeywordsByListResourceWithStreamingResponse:
    def __init__(self, keywords_by_list: KeywordsByListResource) -> None:
        self._keywords_by_list = keywords_by_list

        self.create = to_streamed_response_wrapper(
            keywords_by_list.create,
        )


class AsyncKeywordsByListResourceWithStreamingResponse:
    def __init__(self, keywords_by_list: AsyncKeywordsByListResource) -> None:
        self._keywords_by_list = keywords_by_list

        self.create = async_to_streamed_response_wrapper(
            keywords_by_list.create,
        )
