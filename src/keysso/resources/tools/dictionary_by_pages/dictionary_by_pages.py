# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

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
from ....types.tools import dictionary_by_page_create_params
from ...._base_client import make_request_options
from ....types.report import Base
from ....types.report.base import Base
from ....types.tools.dictionary_by_page_create_response import DictionaryByPageCreateResponse

__all__ = ["DictionaryByPagesResource", "AsyncDictionaryByPagesResource"]


class DictionaryByPagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DictionaryByPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return DictionaryByPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DictionaryByPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return DictionaryByPagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        pages: Iterable[object],
        base: Base | Omit = omit,
        config: dictionary_by_page_create_params.Config | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DictionaryByPageCreateResponse:
        """
        Создание отчета и получение идентификатора, который понадобится в дальнейшем для
        взаимодействия с отчетом.

        Args:
          pages: Список страниц

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          config: Настройки

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tools/dictionary-by-pages",
            body=maybe_transform(
                {
                    "pages": pages,
                    "base": base,
                    "config": config,
                },
                dictionary_by_page_create_params.DictionaryByPageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DictionaryByPageCreateResponse,
        )


class AsyncDictionaryByPagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDictionaryByPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncDictionaryByPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDictionaryByPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncDictionaryByPagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        pages: Iterable[object],
        base: Base | Omit = omit,
        config: dictionary_by_page_create_params.Config | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DictionaryByPageCreateResponse:
        """
        Создание отчета и получение идентификатора, который понадобится в дальнейшем для
        взаимодействия с отчетом.

        Args:
          pages: Список страниц

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          config: Настройки

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tools/dictionary-by-pages",
            body=await async_maybe_transform(
                {
                    "pages": pages,
                    "base": base,
                    "config": config,
                },
                dictionary_by_page_create_params.DictionaryByPageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DictionaryByPageCreateResponse,
        )


class DictionaryByPagesResourceWithRawResponse:
    def __init__(self, dictionary_by_pages: DictionaryByPagesResource) -> None:
        self._dictionary_by_pages = dictionary_by_pages

        self.create = to_raw_response_wrapper(
            dictionary_by_pages.create,
        )


class AsyncDictionaryByPagesResourceWithRawResponse:
    def __init__(self, dictionary_by_pages: AsyncDictionaryByPagesResource) -> None:
        self._dictionary_by_pages = dictionary_by_pages

        self.create = async_to_raw_response_wrapper(
            dictionary_by_pages.create,
        )


class DictionaryByPagesResourceWithStreamingResponse:
    def __init__(self, dictionary_by_pages: DictionaryByPagesResource) -> None:
        self._dictionary_by_pages = dictionary_by_pages

        self.create = to_streamed_response_wrapper(
            dictionary_by_pages.create,
        )


class AsyncDictionaryByPagesResourceWithStreamingResponse:
    def __init__(self, dictionary_by_pages: AsyncDictionaryByPagesResource) -> None:
        self._dictionary_by_pages = dictionary_by_pages

        self.create = async_to_streamed_response_wrapper(
            dictionary_by_pages.create,
        )
