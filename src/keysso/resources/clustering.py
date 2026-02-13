# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import clustering_list_params, clustering_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.report import Base
from ..types.report.base import Base
from ..types.clustering_list_response import ClusteringListResponse
from ..types.clustering_create_response import ClusteringCreateResponse

__all__ = ["ClusteringResource", "AsyncClusteringResource"]


class ClusteringResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClusteringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return ClusteringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClusteringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return ClusteringResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        list: SequenceNotStr[str],
        base: Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClusteringCreateResponse:
        """
        Args:
          list: Массив фраз (максимальная длина фразы - 100 символов)

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
            "/clustering",
            body=maybe_transform(
                {
                    "list": list,
                    "base": base,
                },
                clustering_create_params.ClusteringCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClusteringCreateResponse,
        )

    def list(
        self,
        *,
        is_main: bool | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClusteringListResponse:
        """
        Пример запроса
        `https://api.keys.so/clustering/list?sort=access_date%7Casc&page=1&per_page=25`

        Args:
          is_main: **Список проектов:** `true` — только созданные вручную `false` — все проекты,
              включая созданные автоматически родительскими типами проектов

              **Иерархия проектов:** `Мониторинг » Кластеризатор » Выдача | Wordstat`

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
            "/clustering/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_main": is_main,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    clustering_list_params.ClusteringListParams,
                ),
            ),
            cast_to=ClusteringListResponse,
        )


class AsyncClusteringResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClusteringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncClusteringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClusteringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncClusteringResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        list: SequenceNotStr[str],
        base: Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClusteringCreateResponse:
        """
        Args:
          list: Массив фраз (максимальная длина фразы - 100 символов)

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
            "/clustering",
            body=await async_maybe_transform(
                {
                    "list": list,
                    "base": base,
                },
                clustering_create_params.ClusteringCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClusteringCreateResponse,
        )

    async def list(
        self,
        *,
        is_main: bool | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClusteringListResponse:
        """
        Пример запроса
        `https://api.keys.so/clustering/list?sort=access_date%7Casc&page=1&per_page=25`

        Args:
          is_main: **Список проектов:** `true` — только созданные вручную `false` — все проекты,
              включая созданные автоматически родительскими типами проектов

              **Иерархия проектов:** `Мониторинг » Кластеризатор » Выдача | Wordstat`

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
            "/clustering/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "is_main": is_main,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    clustering_list_params.ClusteringListParams,
                ),
            ),
            cast_to=ClusteringListResponse,
        )


class ClusteringResourceWithRawResponse:
    def __init__(self, clustering: ClusteringResource) -> None:
        self._clustering = clustering

        self.create = to_raw_response_wrapper(
            clustering.create,
        )
        self.list = to_raw_response_wrapper(
            clustering.list,
        )


class AsyncClusteringResourceWithRawResponse:
    def __init__(self, clustering: AsyncClusteringResource) -> None:
        self._clustering = clustering

        self.create = async_to_raw_response_wrapper(
            clustering.create,
        )
        self.list = async_to_raw_response_wrapper(
            clustering.list,
        )


class ClusteringResourceWithStreamingResponse:
    def __init__(self, clustering: ClusteringResource) -> None:
        self._clustering = clustering

        self.create = to_streamed_response_wrapper(
            clustering.create,
        )
        self.list = to_streamed_response_wrapper(
            clustering.list,
        )


class AsyncClusteringResourceWithStreamingResponse:
    def __init__(self, clustering: AsyncClusteringResource) -> None:
        self._clustering = clustering

        self.create = async_to_streamed_response_wrapper(
            clustering.create,
        )
        self.list = async_to_streamed_response_wrapper(
            clustering.list,
        )
