# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ....types.tools import keywords_by_page_create_params
from ...._base_client import make_request_options
from ....types.report import Base
from ....types.report.base import Base
from ....types.tools.keywords_by_page_create_response import KeywordsByPageCreateResponse

__all__ = ["KeywordsByPagesResource", "AsyncKeywordsByPagesResource"]


class KeywordsByPagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeywordsByPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return KeywordsByPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeywordsByPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return KeywordsByPagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        list: SequenceNotStr[str],
        base: Base | Omit = omit,
        top: Literal[10, 50] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeywordsByPageCreateResponse:
        """
        Создание отчета и получение идентификатора, который понадобится в дальнейшем для
        взаимодействия с отчетом.

        Args:
          list: Список запросов страниц

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          top: Охват позиций

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tools/keywords_by_pages",
            body=maybe_transform(
                {
                    "list": list,
                    "base": base,
                    "top": top,
                },
                keywords_by_page_create_params.KeywordsByPageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordsByPageCreateResponse,
        )


class AsyncKeywordsByPagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeywordsByPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeywordsByPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeywordsByPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return AsyncKeywordsByPagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        list: SequenceNotStr[str],
        base: Base | Omit = omit,
        top: Literal[10, 50] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeywordsByPageCreateResponse:
        """
        Создание отчета и получение идентификатора, который понадобится в дальнейшем для
        взаимодействия с отчетом.

        Args:
          list: Список запросов страниц

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          top: Охват позиций

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tools/keywords_by_pages",
            body=await async_maybe_transform(
                {
                    "list": list,
                    "base": base,
                    "top": top,
                },
                keywords_by_page_create_params.KeywordsByPageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordsByPageCreateResponse,
        )


class KeywordsByPagesResourceWithRawResponse:
    def __init__(self, keywords_by_pages: KeywordsByPagesResource) -> None:
        self._keywords_by_pages = keywords_by_pages

        self.create = to_raw_response_wrapper(
            keywords_by_pages.create,
        )


class AsyncKeywordsByPagesResourceWithRawResponse:
    def __init__(self, keywords_by_pages: AsyncKeywordsByPagesResource) -> None:
        self._keywords_by_pages = keywords_by_pages

        self.create = async_to_raw_response_wrapper(
            keywords_by_pages.create,
        )


class KeywordsByPagesResourceWithStreamingResponse:
    def __init__(self, keywords_by_pages: KeywordsByPagesResource) -> None:
        self._keywords_by_pages = keywords_by_pages

        self.create = to_streamed_response_wrapper(
            keywords_by_pages.create,
        )


class AsyncKeywordsByPagesResourceWithStreamingResponse:
    def __init__(self, keywords_by_pages: AsyncKeywordsByPagesResource) -> None:
        self._keywords_by_pages = keywords_by_pages

        self.create = async_to_streamed_response_wrapper(
            keywords_by_pages.create,
        )
