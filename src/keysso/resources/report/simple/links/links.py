# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .backlinks_ip import (
    BacklinksIPResource,
    AsyncBacklinksIPResource,
    BacklinksIPResourceWithRawResponse,
    AsyncBacklinksIPResourceWithRawResponse,
    BacklinksIPResourceWithStreamingResponse,
    AsyncBacklinksIPResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.report import Base
from .....types.report.base import Base
from .....types.report.simple import (
    link_domains_batch_params,
    link_retrieve_pages_params,
    link_retrieve_outlinks_params,
    link_retrieve_backlinks_params,
    link_retrieve_backlinks_anchor_params,
    link_retrieve_outlinks_domains_params,
    link_retrieve_backlinks_domains_params,
    link_retrieve_outlinks_domains_view_domain_params,
    link_retrieve_backlinks_domains_view_domain_params,
)
from .....types.report.simple.link_domains_batch_response import LinkDomainsBatchResponse
from .....types.report.simple.link_retrieve_pages_response import LinkRetrievePagesResponse
from .....types.report.simple.link_retrieve_outlinks_response import LinkRetrieveOutlinksResponse
from .....types.report.simple.link_retrieve_backlinks_response import LinkRetrieveBacklinksResponse
from .....types.report.simple.link_retrieve_backlinks_anchor_response import LinkRetrieveBacklinksAnchorResponse
from .....types.report.simple.link_retrieve_outlinks_domains_response import LinkRetrieveOutlinksDomainsResponse
from .....types.report.simple.link_retrieve_backlinks_domains_response import LinkRetrieveBacklinksDomainsResponse
from .....types.report.simple.link_retrieve_outlinks_domains_view_domain_response import (
    LinkRetrieveOutlinksDomainsViewDomainResponse,
)
from .....types.report.simple.link_retrieve_backlinks_domains_view_domain_response import (
    LinkRetrieveBacklinksDomainsViewDomainResponse,
)

__all__ = ["LinksResource", "AsyncLinksResource"]


class LinksResource(SyncAPIResource):
    @cached_property
    def backlinks_ip(self) -> BacklinksIPResource:
        return BacklinksIPResource(self._client)

    @cached_property
    def with_raw_response(self) -> LinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return LinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return LinksResourceWithStreamingResponse(self)

    def domains_batch(
        self,
        *,
        data: link_domains_batch_params.Data,
        base: Base | Omit = omit,
        params: link_domains_batch_params.Params | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkDomainsBatchResponse:
        """
        Пример запроса `https://api.keys.so/report/simple/links/domains-batch?base=msk`

        Args:
          data: Данные для анализа

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          params: Параметры запроса в теле

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/report/simple/links/domains-batch",
            body=maybe_transform(
                {
                    "data": data,
                    "params": params,
                },
                link_domains_batch_params.LinkDomainsBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"base": base}, link_domains_batch_params.LinkDomainsBatchParams),
            ),
            cast_to=LinkDomainsBatchResponse,
        )

    def retrieve_backlinks(
        self,
        *,
        domain: str,
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
    ) -> LinkRetrieveBacklinksResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/backlinks?domain=wildberries.ru&sort=created_at%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/backlinks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_backlinks_params.LinkRetrieveBacklinksParams,
                ),
            ),
            cast_to=LinkRetrieveBacklinksResponse,
        )

    def retrieve_backlinks_anchor(
        self,
        *,
        domain: str,
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
    ) -> LinkRetrieveBacklinksAnchorResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/backlinks-anchor?domain=wildberries.ru&sort=backlinks_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/backlinks-anchor",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_backlinks_anchor_params.LinkRetrieveBacklinksAnchorParams,
                ),
            ),
            cast_to=LinkRetrieveBacklinksAnchorResponse,
        )

    def retrieve_backlinks_domains(
        self,
        *,
        domain: str,
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
    ) -> LinkRetrieveBacklinksDomainsResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/backlinks-domains?domain=wildberries.ru&sort=outlinks_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/backlinks-domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_backlinks_domains_params.LinkRetrieveBacklinksDomainsParams,
                ),
            ),
            cast_to=LinkRetrieveBacklinksDomainsResponse,
        )

    def retrieve_backlinks_domains_view_domain(
        self,
        *,
        domain: str,
        view: str,
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
    ) -> LinkRetrieveBacklinksDomainsViewDomainResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/backlinks-domains?domain=wildberries.ru&view=domain&sort=outlinks_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

          view: Фильтр данных по конкретному домену

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
            "/report/simple/links/backlinks-domains?view=domain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "view": view,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_backlinks_domains_view_domain_params.LinkRetrieveBacklinksDomainsViewDomainParams,
                ),
            ),
            cast_to=LinkRetrieveBacklinksDomainsViewDomainResponse,
        )

    def retrieve_outlinks(
        self,
        *,
        domain: str,
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
    ) -> LinkRetrieveOutlinksResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/outlinks?domain=wildberries.ru&sort=created_at%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/outlinks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_outlinks_params.LinkRetrieveOutlinksParams,
                ),
            ),
            cast_to=LinkRetrieveOutlinksResponse,
        )

    def retrieve_outlinks_domains(
        self,
        *,
        domain: str,
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
    ) -> LinkRetrieveOutlinksDomainsResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/outlinks-domains?domain=wildberries.ru&sort=backlinks_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/outlinks-domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_outlinks_domains_params.LinkRetrieveOutlinksDomainsParams,
                ),
            ),
            cast_to=LinkRetrieveOutlinksDomainsResponse,
        )

    def retrieve_outlinks_domains_view_domain(
        self,
        *,
        domain: str,
        view: str,
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
    ) -> LinkRetrieveOutlinksDomainsViewDomainResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/outlinks-domains?domain=wildberries.ru&view=domain&sort=backlinks_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

          view: Фильтр данных по конкретному домену

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
            "/report/simple/links/outlinks-domains?view=domain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "view": view,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_outlinks_domains_view_domain_params.LinkRetrieveOutlinksDomainsViewDomainParams,
                ),
            ),
            cast_to=LinkRetrieveOutlinksDomainsViewDomainResponse,
        )

    def retrieve_pages(
        self,
        *,
        domain: str,
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
    ) -> LinkRetrievePagesResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/pages?domain=dodopizza.ru&sort=numurl%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/pages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_pages_params.LinkRetrievePagesParams,
                ),
            ),
            cast_to=LinkRetrievePagesResponse,
        )


class AsyncLinksResource(AsyncAPIResource):
    @cached_property
    def backlinks_ip(self) -> AsyncBacklinksIPResource:
        return AsyncBacklinksIPResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncLinksResourceWithStreamingResponse(self)

    async def domains_batch(
        self,
        *,
        data: link_domains_batch_params.Data,
        base: Base | Omit = omit,
        params: link_domains_batch_params.Params | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkDomainsBatchResponse:
        """
        Пример запроса `https://api.keys.so/report/simple/links/domains-batch?base=msk`

        Args:
          data: Данные для анализа

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          params: Параметры запроса в теле

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/report/simple/links/domains-batch",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "params": params,
                },
                link_domains_batch_params.LinkDomainsBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"base": base}, link_domains_batch_params.LinkDomainsBatchParams),
            ),
            cast_to=LinkDomainsBatchResponse,
        )

    async def retrieve_backlinks(
        self,
        *,
        domain: str,
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
    ) -> LinkRetrieveBacklinksResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/backlinks?domain=wildberries.ru&sort=created_at%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/backlinks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_backlinks_params.LinkRetrieveBacklinksParams,
                ),
            ),
            cast_to=LinkRetrieveBacklinksResponse,
        )

    async def retrieve_backlinks_anchor(
        self,
        *,
        domain: str,
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
    ) -> LinkRetrieveBacklinksAnchorResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/backlinks-anchor?domain=wildberries.ru&sort=backlinks_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/backlinks-anchor",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_backlinks_anchor_params.LinkRetrieveBacklinksAnchorParams,
                ),
            ),
            cast_to=LinkRetrieveBacklinksAnchorResponse,
        )

    async def retrieve_backlinks_domains(
        self,
        *,
        domain: str,
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
    ) -> LinkRetrieveBacklinksDomainsResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/backlinks-domains?domain=wildberries.ru&sort=outlinks_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/backlinks-domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_backlinks_domains_params.LinkRetrieveBacklinksDomainsParams,
                ),
            ),
            cast_to=LinkRetrieveBacklinksDomainsResponse,
        )

    async def retrieve_backlinks_domains_view_domain(
        self,
        *,
        domain: str,
        view: str,
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
    ) -> LinkRetrieveBacklinksDomainsViewDomainResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/backlinks-domains?domain=wildberries.ru&view=domain&sort=outlinks_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

          view: Фильтр данных по конкретному домену

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
            "/report/simple/links/backlinks-domains?view=domain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "view": view,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_backlinks_domains_view_domain_params.LinkRetrieveBacklinksDomainsViewDomainParams,
                ),
            ),
            cast_to=LinkRetrieveBacklinksDomainsViewDomainResponse,
        )

    async def retrieve_outlinks(
        self,
        *,
        domain: str,
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
    ) -> LinkRetrieveOutlinksResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/outlinks?domain=wildberries.ru&sort=created_at%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/outlinks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_outlinks_params.LinkRetrieveOutlinksParams,
                ),
            ),
            cast_to=LinkRetrieveOutlinksResponse,
        )

    async def retrieve_outlinks_domains(
        self,
        *,
        domain: str,
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
    ) -> LinkRetrieveOutlinksDomainsResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/outlinks-domains?domain=wildberries.ru&sort=backlinks_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/outlinks-domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_outlinks_domains_params.LinkRetrieveOutlinksDomainsParams,
                ),
            ),
            cast_to=LinkRetrieveOutlinksDomainsResponse,
        )

    async def retrieve_outlinks_domains_view_domain(
        self,
        *,
        domain: str,
        view: str,
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
    ) -> LinkRetrieveOutlinksDomainsViewDomainResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/outlinks-domains?domain=wildberries.ru&view=domain&sort=backlinks_count%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

          view: Фильтр данных по конкретному домену

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
            "/report/simple/links/outlinks-domains?view=domain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "view": view,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_outlinks_domains_view_domain_params.LinkRetrieveOutlinksDomainsViewDomainParams,
                ),
            ),
            cast_to=LinkRetrieveOutlinksDomainsViewDomainResponse,
        )

    async def retrieve_pages(
        self,
        *,
        domain: str,
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
    ) -> LinkRetrievePagesResponse:
        """
        Пример запроса
        `https://api.keys.so/report/simple/links/pages?domain=dodopizza.ru&sort=numurl%7Cdesc&page=1&per_page=25`

        Args:
          domain: Имя домена

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
            "/report/simple/links/pages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    link_retrieve_pages_params.LinkRetrievePagesParams,
                ),
            ),
            cast_to=LinkRetrievePagesResponse,
        )


class LinksResourceWithRawResponse:
    def __init__(self, links: LinksResource) -> None:
        self._links = links

        self.domains_batch = to_raw_response_wrapper(
            links.domains_batch,
        )
        self.retrieve_backlinks = to_raw_response_wrapper(
            links.retrieve_backlinks,
        )
        self.retrieve_backlinks_anchor = to_raw_response_wrapper(
            links.retrieve_backlinks_anchor,
        )
        self.retrieve_backlinks_domains = to_raw_response_wrapper(
            links.retrieve_backlinks_domains,
        )
        self.retrieve_backlinks_domains_view_domain = to_raw_response_wrapper(
            links.retrieve_backlinks_domains_view_domain,
        )
        self.retrieve_outlinks = to_raw_response_wrapper(
            links.retrieve_outlinks,
        )
        self.retrieve_outlinks_domains = to_raw_response_wrapper(
            links.retrieve_outlinks_domains,
        )
        self.retrieve_outlinks_domains_view_domain = to_raw_response_wrapper(
            links.retrieve_outlinks_domains_view_domain,
        )
        self.retrieve_pages = to_raw_response_wrapper(
            links.retrieve_pages,
        )

    @cached_property
    def backlinks_ip(self) -> BacklinksIPResourceWithRawResponse:
        return BacklinksIPResourceWithRawResponse(self._links.backlinks_ip)


class AsyncLinksResourceWithRawResponse:
    def __init__(self, links: AsyncLinksResource) -> None:
        self._links = links

        self.domains_batch = async_to_raw_response_wrapper(
            links.domains_batch,
        )
        self.retrieve_backlinks = async_to_raw_response_wrapper(
            links.retrieve_backlinks,
        )
        self.retrieve_backlinks_anchor = async_to_raw_response_wrapper(
            links.retrieve_backlinks_anchor,
        )
        self.retrieve_backlinks_domains = async_to_raw_response_wrapper(
            links.retrieve_backlinks_domains,
        )
        self.retrieve_backlinks_domains_view_domain = async_to_raw_response_wrapper(
            links.retrieve_backlinks_domains_view_domain,
        )
        self.retrieve_outlinks = async_to_raw_response_wrapper(
            links.retrieve_outlinks,
        )
        self.retrieve_outlinks_domains = async_to_raw_response_wrapper(
            links.retrieve_outlinks_domains,
        )
        self.retrieve_outlinks_domains_view_domain = async_to_raw_response_wrapper(
            links.retrieve_outlinks_domains_view_domain,
        )
        self.retrieve_pages = async_to_raw_response_wrapper(
            links.retrieve_pages,
        )

    @cached_property
    def backlinks_ip(self) -> AsyncBacklinksIPResourceWithRawResponse:
        return AsyncBacklinksIPResourceWithRawResponse(self._links.backlinks_ip)


class LinksResourceWithStreamingResponse:
    def __init__(self, links: LinksResource) -> None:
        self._links = links

        self.domains_batch = to_streamed_response_wrapper(
            links.domains_batch,
        )
        self.retrieve_backlinks = to_streamed_response_wrapper(
            links.retrieve_backlinks,
        )
        self.retrieve_backlinks_anchor = to_streamed_response_wrapper(
            links.retrieve_backlinks_anchor,
        )
        self.retrieve_backlinks_domains = to_streamed_response_wrapper(
            links.retrieve_backlinks_domains,
        )
        self.retrieve_backlinks_domains_view_domain = to_streamed_response_wrapper(
            links.retrieve_backlinks_domains_view_domain,
        )
        self.retrieve_outlinks = to_streamed_response_wrapper(
            links.retrieve_outlinks,
        )
        self.retrieve_outlinks_domains = to_streamed_response_wrapper(
            links.retrieve_outlinks_domains,
        )
        self.retrieve_outlinks_domains_view_domain = to_streamed_response_wrapper(
            links.retrieve_outlinks_domains_view_domain,
        )
        self.retrieve_pages = to_streamed_response_wrapper(
            links.retrieve_pages,
        )

    @cached_property
    def backlinks_ip(self) -> BacklinksIPResourceWithStreamingResponse:
        return BacklinksIPResourceWithStreamingResponse(self._links.backlinks_ip)


class AsyncLinksResourceWithStreamingResponse:
    def __init__(self, links: AsyncLinksResource) -> None:
        self._links = links

        self.domains_batch = async_to_streamed_response_wrapper(
            links.domains_batch,
        )
        self.retrieve_backlinks = async_to_streamed_response_wrapper(
            links.retrieve_backlinks,
        )
        self.retrieve_backlinks_anchor = async_to_streamed_response_wrapper(
            links.retrieve_backlinks_anchor,
        )
        self.retrieve_backlinks_domains = async_to_streamed_response_wrapper(
            links.retrieve_backlinks_domains,
        )
        self.retrieve_backlinks_domains_view_domain = async_to_streamed_response_wrapper(
            links.retrieve_backlinks_domains_view_domain,
        )
        self.retrieve_outlinks = async_to_streamed_response_wrapper(
            links.retrieve_outlinks,
        )
        self.retrieve_outlinks_domains = async_to_streamed_response_wrapper(
            links.retrieve_outlinks_domains,
        )
        self.retrieve_outlinks_domains_view_domain = async_to_streamed_response_wrapper(
            links.retrieve_outlinks_domains_view_domain,
        )
        self.retrieve_pages = async_to_streamed_response_wrapper(
            links.retrieve_pages,
        )

    @cached_property
    def backlinks_ip(self) -> AsyncBacklinksIPResourceWithStreamingResponse:
        return AsyncBacklinksIPResourceWithStreamingResponse(self._links.backlinks_ip)
