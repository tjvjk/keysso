# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.report.ads import rsya_retrieve_params
from .....types.report.ads.rsya_retrieve_response import RsyaRetrieveResponse

__all__ = ["RsyaResource", "AsyncRsyaResource"]


class RsyaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RsyaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return RsyaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RsyaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return RsyaResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        filter: str | Omit = omit,
        grouping_by: Literal["img_path", "inn", "domain", "erir"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RsyaRetrieveResponse:
        """
        Пример запроса
        `https://api.keys.so/report/ads/rsya?sort=&page=1&per_page=25&groupingBy=erir&filter=titleLIKE%25D0%259A%25D1%2580%25D0%25BE%25D1%2581%25D0%25BE%25D0%25B2%25D0%25BA%25D0%25B8%255EORlegalLIKE%25D0%259A%25D1%2580%25D0%25BE%25D1%2581%25D0%25BE%25D0%25B2%25D0%25BA%25D0%25B8%255EORtarget_urlLIKE%25D0%259A%25D1%2580%25D0%25BE%25D1%2581%25D0%25BE%25D0%25B2%25D0%25BA%25D0%25B8`

        Args:
          filter: Подробнее про фильтрацию смотрите в разделе
              [Фильтрация данных](#tag/Filtraciya-dannyh)

          grouping_by: Группировка. Данный параметр работает только при наличии фильтра.

              `img_path` - по изображению

              `inn` - по рекламодателю(ИНН)

              `domain` - по домену

              `erir` - по ЕРИР

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
            "/report/ads/rsya",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "grouping_by": grouping_by,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    rsya_retrieve_params.RsyaRetrieveParams,
                ),
            ),
            cast_to=RsyaRetrieveResponse,
        )


class AsyncRsyaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRsyaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncRsyaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRsyaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncRsyaResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        filter: str | Omit = omit,
        grouping_by: Literal["img_path", "inn", "domain", "erir"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RsyaRetrieveResponse:
        """
        Пример запроса
        `https://api.keys.so/report/ads/rsya?sort=&page=1&per_page=25&groupingBy=erir&filter=titleLIKE%25D0%259A%25D1%2580%25D0%25BE%25D1%2581%25D0%25BE%25D0%25B2%25D0%25BA%25D0%25B8%255EORlegalLIKE%25D0%259A%25D1%2580%25D0%25BE%25D1%2581%25D0%25BE%25D0%25B2%25D0%25BA%25D0%25B8%255EORtarget_urlLIKE%25D0%259A%25D1%2580%25D0%25BE%25D1%2581%25D0%25BE%25D0%25B2%25D0%25BA%25D0%25B8`

        Args:
          filter: Подробнее про фильтрацию смотрите в разделе
              [Фильтрация данных](#tag/Filtraciya-dannyh)

          grouping_by: Группировка. Данный параметр работает только при наличии фильтра.

              `img_path` - по изображению

              `inn` - по рекламодателю(ИНН)

              `domain` - по домену

              `erir` - по ЕРИР

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
            "/report/ads/rsya",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "grouping_by": grouping_by,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    rsya_retrieve_params.RsyaRetrieveParams,
                ),
            ),
            cast_to=RsyaRetrieveResponse,
        )


class RsyaResourceWithRawResponse:
    def __init__(self, rsya: RsyaResource) -> None:
        self._rsya = rsya

        self.retrieve = to_raw_response_wrapper(
            rsya.retrieve,
        )


class AsyncRsyaResourceWithRawResponse:
    def __init__(self, rsya: AsyncRsyaResource) -> None:
        self._rsya = rsya

        self.retrieve = async_to_raw_response_wrapper(
            rsya.retrieve,
        )


class RsyaResourceWithStreamingResponse:
    def __init__(self, rsya: RsyaResource) -> None:
        self._rsya = rsya

        self.retrieve = to_streamed_response_wrapper(
            rsya.retrieve,
        )


class AsyncRsyaResourceWithStreamingResponse:
    def __init__(self, rsya: AsyncRsyaResource) -> None:
        self._rsya = rsya

        self.retrieve = async_to_streamed_response_wrapper(
            rsya.retrieve,
        )
