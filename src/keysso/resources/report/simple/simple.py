# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .direct import (
    DirectResource,
    AsyncDirectResource,
    DirectResourceWithRawResponse,
    AsyncDirectResourceWithRawResponse,
    DirectResourceWithStreamingResponse,
    AsyncDirectResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .ai_answers import (
    AIAnswersResource,
    AsyncAIAnswersResource,
    AIAnswersResourceWithRawResponse,
    AsyncAIAnswersResourceWithRawResponse,
    AIAnswersResourceWithStreamingResponse,
    AsyncAIAnswersResourceWithStreamingResponse,
)
from .links.links import (
    LinksResource,
    AsyncLinksResource,
    LinksResourceWithRawResponse,
    AsyncLinksResourceWithRawResponse,
    LinksResourceWithStreamingResponse,
    AsyncLinksResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.report import (
    Base,
    simple_retrieve_similarkeys_params,
    simple_retrieve_domain_dashboard_params,
    simple_retrieve_domain_ad_history_params,
    simple_retrieve_keyword_dashboard_params,
    simple_retrieve_top_domain_visibility_params,
)
from .context.context import (
    ContextResource,
    AsyncContextResource,
    ContextResourceWithRawResponse,
    AsyncContextResourceWithRawResponse,
    ContextResourceWithStreamingResponse,
    AsyncContextResourceWithStreamingResponse,
)
from .organic.organic import (
    OrganicResource,
    AsyncOrganicResource,
    OrganicResourceWithRawResponse,
    AsyncOrganicResourceWithRawResponse,
    OrganicResourceWithStreamingResponse,
    AsyncOrganicResourceWithStreamingResponse,
)
from ....types.report.base import Base
from ....types.report.simple_retrieve_similarkeys_response import SimpleRetrieveSimilarkeysResponse
from ....types.report.simple_retrieve_domain_dashboard_response import SimpleRetrieveDomainDashboardResponse
from ....types.report.simple_retrieve_domain_ad_history_response import SimpleRetrieveDomainAdHistoryResponse
from ....types.report.simple_retrieve_keyword_dashboard_response import SimpleRetrieveKeywordDashboardResponse
from ....types.report.simple_retrieve_top_domain_visibility_response import SimpleRetrieveTopDomainVisibilityResponse

__all__ = ["SimpleResource", "AsyncSimpleResource"]


class SimpleResource(SyncAPIResource):
    @cached_property
    def organic(self) -> OrganicResource:
        return OrganicResource(self._client)

    @cached_property
    def context(self) -> ContextResource:
        return ContextResource(self._client)

    @cached_property
    def ai_answers(self) -> AIAnswersResource:
        return AIAnswersResource(self._client)

    @cached_property
    def links(self) -> LinksResource:
        return LinksResource(self._client)

    @cached_property
    def direct(self) -> DirectResource:
        return DirectResource(self._client)

    @cached_property
    def with_raw_response(self) -> SimpleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return SimpleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimpleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return SimpleResourceWithStreamingResponse(self)

    def retrieve_domain_ad_history(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimpleRetrieveDomainAdHistoryResponse:
        """
        Пример запроса:
        `https://api.keys.so/report/simple/domain_ad_history?base=msk&domain=wildberries.ru`

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/report/simple/domain_ad_history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                    },
                    simple_retrieve_domain_ad_history_params.SimpleRetrieveDomainAdHistoryParams,
                ),
            ),
            cast_to=SimpleRetrieveDomainAdHistoryResponse,
        )

    def retrieve_domain_dashboard(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimpleRetrieveDomainDashboardResponse:
        """
        Пример запроса:
        `https://api.keys.so/report/simple/domain_dashboard?base=msk&domain=wildberries.ru`

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/report/simple/domain_dashboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                    },
                    simple_retrieve_domain_dashboard_params.SimpleRetrieveDomainDashboardParams,
                ),
            ),
            cast_to=SimpleRetrieveDomainDashboardResponse,
        )

    def retrieve_keyword_dashboard(
        self,
        *,
        keyword: str,
        base: Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimpleRetrieveKeywordDashboardResponse:
        """
        Пример запроса:
        `https://api.keys.so/report/simple/keyword_dashboard?keyword=%D0%9F%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BE%D0%BA%D0%BD%D0%B0&base=msk`

        Args:
          keyword: Поисковый запрос

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
        return self._get(
            "/report/simple/keyword_dashboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "keyword": keyword,
                        "base": base,
                    },
                    simple_retrieve_keyword_dashboard_params.SimpleRetrieveKeywordDashboardParams,
                ),
            ),
            cast_to=SimpleRetrieveKeywordDashboardResponse,
        )

    def retrieve_similarkeys(
        self,
        *,
        keyword: str,
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
    ) -> SimpleRetrieveSimilarkeysResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/similarkeys?base=msk&keyword=%D0%BF%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BE%D0%BA%D0%BD%D0%B0 &sort=wsk%7Casc&page=1&per_page=25`

        Args:
          keyword: Поисковый запрос

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
            "/report/simple/similarkeys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "keyword": keyword,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    simple_retrieve_similarkeys_params.SimpleRetrieveSimilarkeysParams,
                ),
            ),
            cast_to=SimpleRetrieveSimilarkeysResponse,
        )

    def retrieve_top_domain_visibility(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimpleRetrieveTopDomainVisibilityResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/top_domain_visibility?base=msk&domain=dodopizza.ru&sort=&page=54&per_page=25`

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
            "/report/simple/top_domain_visibility",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    simple_retrieve_top_domain_visibility_params.SimpleRetrieveTopDomainVisibilityParams,
                ),
            ),
            cast_to=SimpleRetrieveTopDomainVisibilityResponse,
        )


class AsyncSimpleResource(AsyncAPIResource):
    @cached_property
    def organic(self) -> AsyncOrganicResource:
        return AsyncOrganicResource(self._client)

    @cached_property
    def context(self) -> AsyncContextResource:
        return AsyncContextResource(self._client)

    @cached_property
    def ai_answers(self) -> AsyncAIAnswersResource:
        return AsyncAIAnswersResource(self._client)

    @cached_property
    def links(self) -> AsyncLinksResource:
        return AsyncLinksResource(self._client)

    @cached_property
    def direct(self) -> AsyncDirectResource:
        return AsyncDirectResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSimpleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimpleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimpleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return AsyncSimpleResourceWithStreamingResponse(self)

    async def retrieve_domain_ad_history(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimpleRetrieveDomainAdHistoryResponse:
        """
        Пример запроса:
        `https://api.keys.so/report/simple/domain_ad_history?base=msk&domain=wildberries.ru`

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/report/simple/domain_ad_history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                    },
                    simple_retrieve_domain_ad_history_params.SimpleRetrieveDomainAdHistoryParams,
                ),
            ),
            cast_to=SimpleRetrieveDomainAdHistoryResponse,
        )

    async def retrieve_domain_dashboard(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimpleRetrieveDomainDashboardResponse:
        """
        Пример запроса:
        `https://api.keys.so/report/simple/domain_dashboard?base=msk&domain=wildberries.ru`

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/report/simple/domain_dashboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                    },
                    simple_retrieve_domain_dashboard_params.SimpleRetrieveDomainDashboardParams,
                ),
            ),
            cast_to=SimpleRetrieveDomainDashboardResponse,
        )

    async def retrieve_keyword_dashboard(
        self,
        *,
        keyword: str,
        base: Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimpleRetrieveKeywordDashboardResponse:
        """
        Пример запроса:
        `https://api.keys.so/report/simple/keyword_dashboard?keyword=%D0%9F%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BE%D0%BA%D0%BD%D0%B0&base=msk`

        Args:
          keyword: Поисковый запрос

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
        return await self._get(
            "/report/simple/keyword_dashboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "keyword": keyword,
                        "base": base,
                    },
                    simple_retrieve_keyword_dashboard_params.SimpleRetrieveKeywordDashboardParams,
                ),
            ),
            cast_to=SimpleRetrieveKeywordDashboardResponse,
        )

    async def retrieve_similarkeys(
        self,
        *,
        keyword: str,
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
    ) -> SimpleRetrieveSimilarkeysResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/similarkeys?base=msk&keyword=%D0%BF%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BE%D0%BA%D0%BD%D0%B0 &sort=wsk%7Casc&page=1&per_page=25`

        Args:
          keyword: Поисковый запрос

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
            "/report/simple/similarkeys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "keyword": keyword,
                        "base": base,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    simple_retrieve_similarkeys_params.SimpleRetrieveSimilarkeysParams,
                ),
            ),
            cast_to=SimpleRetrieveSimilarkeysResponse,
        )

    async def retrieve_top_domain_visibility(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimpleRetrieveTopDomainVisibilityResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/top_domain_visibility?base=msk&domain=dodopizza.ru&sort=&page=54&per_page=25`

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
            "/report/simple/top_domain_visibility",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    simple_retrieve_top_domain_visibility_params.SimpleRetrieveTopDomainVisibilityParams,
                ),
            ),
            cast_to=SimpleRetrieveTopDomainVisibilityResponse,
        )


class SimpleResourceWithRawResponse:
    def __init__(self, simple: SimpleResource) -> None:
        self._simple = simple

        self.retrieve_domain_ad_history = to_raw_response_wrapper(
            simple.retrieve_domain_ad_history,
        )
        self.retrieve_domain_dashboard = to_raw_response_wrapper(
            simple.retrieve_domain_dashboard,
        )
        self.retrieve_keyword_dashboard = to_raw_response_wrapper(
            simple.retrieve_keyword_dashboard,
        )
        self.retrieve_similarkeys = to_raw_response_wrapper(
            simple.retrieve_similarkeys,
        )
        self.retrieve_top_domain_visibility = to_raw_response_wrapper(
            simple.retrieve_top_domain_visibility,
        )

    @cached_property
    def organic(self) -> OrganicResourceWithRawResponse:
        return OrganicResourceWithRawResponse(self._simple.organic)

    @cached_property
    def context(self) -> ContextResourceWithRawResponse:
        return ContextResourceWithRawResponse(self._simple.context)

    @cached_property
    def ai_answers(self) -> AIAnswersResourceWithRawResponse:
        return AIAnswersResourceWithRawResponse(self._simple.ai_answers)

    @cached_property
    def links(self) -> LinksResourceWithRawResponse:
        return LinksResourceWithRawResponse(self._simple.links)

    @cached_property
    def direct(self) -> DirectResourceWithRawResponse:
        return DirectResourceWithRawResponse(self._simple.direct)


class AsyncSimpleResourceWithRawResponse:
    def __init__(self, simple: AsyncSimpleResource) -> None:
        self._simple = simple

        self.retrieve_domain_ad_history = async_to_raw_response_wrapper(
            simple.retrieve_domain_ad_history,
        )
        self.retrieve_domain_dashboard = async_to_raw_response_wrapper(
            simple.retrieve_domain_dashboard,
        )
        self.retrieve_keyword_dashboard = async_to_raw_response_wrapper(
            simple.retrieve_keyword_dashboard,
        )
        self.retrieve_similarkeys = async_to_raw_response_wrapper(
            simple.retrieve_similarkeys,
        )
        self.retrieve_top_domain_visibility = async_to_raw_response_wrapper(
            simple.retrieve_top_domain_visibility,
        )

    @cached_property
    def organic(self) -> AsyncOrganicResourceWithRawResponse:
        return AsyncOrganicResourceWithRawResponse(self._simple.organic)

    @cached_property
    def context(self) -> AsyncContextResourceWithRawResponse:
        return AsyncContextResourceWithRawResponse(self._simple.context)

    @cached_property
    def ai_answers(self) -> AsyncAIAnswersResourceWithRawResponse:
        return AsyncAIAnswersResourceWithRawResponse(self._simple.ai_answers)

    @cached_property
    def links(self) -> AsyncLinksResourceWithRawResponse:
        return AsyncLinksResourceWithRawResponse(self._simple.links)

    @cached_property
    def direct(self) -> AsyncDirectResourceWithRawResponse:
        return AsyncDirectResourceWithRawResponse(self._simple.direct)


class SimpleResourceWithStreamingResponse:
    def __init__(self, simple: SimpleResource) -> None:
        self._simple = simple

        self.retrieve_domain_ad_history = to_streamed_response_wrapper(
            simple.retrieve_domain_ad_history,
        )
        self.retrieve_domain_dashboard = to_streamed_response_wrapper(
            simple.retrieve_domain_dashboard,
        )
        self.retrieve_keyword_dashboard = to_streamed_response_wrapper(
            simple.retrieve_keyword_dashboard,
        )
        self.retrieve_similarkeys = to_streamed_response_wrapper(
            simple.retrieve_similarkeys,
        )
        self.retrieve_top_domain_visibility = to_streamed_response_wrapper(
            simple.retrieve_top_domain_visibility,
        )

    @cached_property
    def organic(self) -> OrganicResourceWithStreamingResponse:
        return OrganicResourceWithStreamingResponse(self._simple.organic)

    @cached_property
    def context(self) -> ContextResourceWithStreamingResponse:
        return ContextResourceWithStreamingResponse(self._simple.context)

    @cached_property
    def ai_answers(self) -> AIAnswersResourceWithStreamingResponse:
        return AIAnswersResourceWithStreamingResponse(self._simple.ai_answers)

    @cached_property
    def links(self) -> LinksResourceWithStreamingResponse:
        return LinksResourceWithStreamingResponse(self._simple.links)

    @cached_property
    def direct(self) -> DirectResourceWithStreamingResponse:
        return DirectResourceWithStreamingResponse(self._simple.direct)


class AsyncSimpleResourceWithStreamingResponse:
    def __init__(self, simple: AsyncSimpleResource) -> None:
        self._simple = simple

        self.retrieve_domain_ad_history = async_to_streamed_response_wrapper(
            simple.retrieve_domain_ad_history,
        )
        self.retrieve_domain_dashboard = async_to_streamed_response_wrapper(
            simple.retrieve_domain_dashboard,
        )
        self.retrieve_keyword_dashboard = async_to_streamed_response_wrapper(
            simple.retrieve_keyword_dashboard,
        )
        self.retrieve_similarkeys = async_to_streamed_response_wrapper(
            simple.retrieve_similarkeys,
        )
        self.retrieve_top_domain_visibility = async_to_streamed_response_wrapper(
            simple.retrieve_top_domain_visibility,
        )

    @cached_property
    def organic(self) -> AsyncOrganicResourceWithStreamingResponse:
        return AsyncOrganicResourceWithStreamingResponse(self._simple.organic)

    @cached_property
    def context(self) -> AsyncContextResourceWithStreamingResponse:
        return AsyncContextResourceWithStreamingResponse(self._simple.context)

    @cached_property
    def ai_answers(self) -> AsyncAIAnswersResourceWithStreamingResponse:
        return AsyncAIAnswersResourceWithStreamingResponse(self._simple.ai_answers)

    @cached_property
    def links(self) -> AsyncLinksResourceWithStreamingResponse:
        return AsyncLinksResourceWithStreamingResponse(self._simple.links)

    @cached_property
    def direct(self) -> AsyncDirectResourceWithStreamingResponse:
        return AsyncDirectResourceWithStreamingResponse(self._simple.direct)
