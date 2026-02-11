# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...._base_client import make_request_options
from ....types.report import Base
from ....types.report.base import Base
from ....types.report.simple import direct_retrieve_ads_params, direct_retrieve_domain_params
from ....types.report.simple.direct_retrieve_ads_response import DirectRetrieveAdsResponse
from ....types.report.simple.direct_retrieve_domain_response import DirectRetrieveDomainResponse

__all__ = ["DirectResource", "AsyncDirectResource"]


class DirectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DirectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return DirectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return DirectResourceWithStreamingResponse(self)

    def retrieve_ads(
        self,
        *,
        kid: int,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectRetrieveAdsResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/direct/ads?base=msk&kid=17222067&sort=keys_count%7Cdesc&page=1&per_page=25`

        Args:
          kid: Идентификатор фразы

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          filter: Подробнее про фильтрацию смотрите в разделе
              [Фильтрация данных](#tag/Filtraciya-dannyh)

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
            "/report/simple/direct/ads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "kid": kid,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    direct_retrieve_ads_params.DirectRetrieveAdsParams,
                ),
            ),
            cast_to=DirectRetrieveAdsResponse,
        )

    def retrieve_domain(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectRetrieveDomainResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/direct/domain?base=msk&domain=wildberries.ru&sort=keys_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          filter: Подробнее про фильтрацию смотрите в разделе
              [Фильтрация данных](#tag/Filtraciya-dannyh)

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
            "/report/simple/direct/domain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    direct_retrieve_domain_params.DirectRetrieveDomainParams,
                ),
            ),
            cast_to=DirectRetrieveDomainResponse,
        )


class AsyncDirectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDirectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDirectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return AsyncDirectResourceWithStreamingResponse(self)

    async def retrieve_ads(
        self,
        *,
        kid: int,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectRetrieveAdsResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/direct/ads?base=msk&kid=17222067&sort=keys_count%7Cdesc&page=1&per_page=25`

        Args:
          kid: Идентификатор фразы

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          filter: Подробнее про фильтрацию смотрите в разделе
              [Фильтрация данных](#tag/Filtraciya-dannyh)

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
            "/report/simple/direct/ads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "kid": kid,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    direct_retrieve_ads_params.DirectRetrieveAdsParams,
                ),
            ),
            cast_to=DirectRetrieveAdsResponse,
        )

    async def retrieve_domain(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectRetrieveDomainResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/direct/domain?base=msk&domain=wildberries.ru&sort=keys_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          filter: Подробнее про фильтрацию смотрите в разделе
              [Фильтрация данных](#tag/Filtraciya-dannyh)

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
            "/report/simple/direct/domain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    direct_retrieve_domain_params.DirectRetrieveDomainParams,
                ),
            ),
            cast_to=DirectRetrieveDomainResponse,
        )


class DirectResourceWithRawResponse:
    def __init__(self, direct: DirectResource) -> None:
        self._direct = direct

        self.retrieve_ads = to_raw_response_wrapper(
            direct.retrieve_ads,
        )
        self.retrieve_domain = to_raw_response_wrapper(
            direct.retrieve_domain,
        )


class AsyncDirectResourceWithRawResponse:
    def __init__(self, direct: AsyncDirectResource) -> None:
        self._direct = direct

        self.retrieve_ads = async_to_raw_response_wrapper(
            direct.retrieve_ads,
        )
        self.retrieve_domain = async_to_raw_response_wrapper(
            direct.retrieve_domain,
        )


class DirectResourceWithStreamingResponse:
    def __init__(self, direct: DirectResource) -> None:
        self._direct = direct

        self.retrieve_ads = to_streamed_response_wrapper(
            direct.retrieve_ads,
        )
        self.retrieve_domain = to_streamed_response_wrapper(
            direct.retrieve_domain,
        )


class AsyncDirectResourceWithStreamingResponse:
    def __init__(self, direct: AsyncDirectResource) -> None:
        self._direct = direct

        self.retrieve_ads = async_to_streamed_response_wrapper(
            direct.retrieve_ads,
        )
        self.retrieve_domain = async_to_streamed_response_wrapper(
            direct.retrieve_domain,
        )
