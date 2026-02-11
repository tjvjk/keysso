# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...types import (
    tool_combine_params,
    tool_compare_params,
    tool_suggest_params,
    tool_check_top_params,
    tool_create_unique_params,
    tool_delete_double_params,
    tool_list_site_themes_params,
    tool_create_history_serp_params,
    tool_create_domains_batch_params,
    tool_check_top_concurents_urls_params,
    tool_check_top_concurents_domains_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.report import Base
from .keywords_by_list import (
    KeywordsByListResource,
    AsyncKeywordsByListResource,
    KeywordsByListResourceWithRawResponse,
    AsyncKeywordsByListResourceWithRawResponse,
    KeywordsByListResourceWithStreamingResponse,
    AsyncKeywordsByListResourceWithStreamingResponse,
)
from ...types.report.base import Base
from ...types.tool_compare_response import ToolCompareResponse
from ...types.tool_suggest_response import ToolSuggestResponse
from ...types.tool_check_top_response import ToolCheckTopResponse
from ...types.tool_create_unique_response import ToolCreateUniqueResponse
from ...types.tool_delete_double_response import ToolDeleteDoubleResponse
from .extended_keywords.extended_keywords import (
    ExtendedKeywordsResource,
    AsyncExtendedKeywordsResource,
    ExtendedKeywordsResourceWithRawResponse,
    AsyncExtendedKeywordsResourceWithRawResponse,
    ExtendedKeywordsResourceWithStreamingResponse,
    AsyncExtendedKeywordsResourceWithStreamingResponse,
)
from .keywords_by_pages.keywords_by_pages import (
    KeywordsByPagesResource,
    AsyncKeywordsByPagesResource,
    KeywordsByPagesResourceWithRawResponse,
    AsyncKeywordsByPagesResourceWithRawResponse,
    KeywordsByPagesResourceWithStreamingResponse,
    AsyncKeywordsByPagesResourceWithStreamingResponse,
)
from ...types.tool_list_site_themes_response import ToolListSiteThemesResponse
from .dictionary_by_pages.dictionary_by_pages import (
    DictionaryByPagesResource,
    AsyncDictionaryByPagesResource,
    DictionaryByPagesResourceWithRawResponse,
    AsyncDictionaryByPagesResourceWithRawResponse,
    DictionaryByPagesResourceWithStreamingResponse,
    AsyncDictionaryByPagesResourceWithStreamingResponse,
)
from ...types.tool_create_history_serp_response import ToolCreateHistorySerpResponse
from ...types.tool_create_domains_batch_response import ToolCreateDomainsBatchResponse
from .concurents_by_keywords.concurents_by_keywords import (
    ConcurentsByKeywordsResource,
    AsyncConcurentsByKeywordsResource,
    ConcurentsByKeywordsResourceWithRawResponse,
    AsyncConcurentsByKeywordsResourceWithRawResponse,
    ConcurentsByKeywordsResourceWithStreamingResponse,
    AsyncConcurentsByKeywordsResourceWithStreamingResponse,
)
from .dictionary_ext_by_page.dictionary_ext_by_page import (
    DictionaryExtByPageResource,
    AsyncDictionaryExtByPageResource,
    DictionaryExtByPageResourceWithRawResponse,
    AsyncDictionaryExtByPageResourceWithRawResponse,
    DictionaryExtByPageResourceWithStreamingResponse,
    AsyncDictionaryExtByPageResourceWithStreamingResponse,
)
from ...types.tool_check_top_concurents_urls_response import ToolCheckTopConcurentsURLsResponse
from ...types.tool_check_top_concurents_domains_response import ToolCheckTopConcurentsDomainsResponse

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def extended_keywords(self) -> ExtendedKeywordsResource:
        return ExtendedKeywordsResource(self._client)

    @cached_property
    def keywords_by_list(self) -> KeywordsByListResource:
        return KeywordsByListResource(self._client)

    @cached_property
    def concurents_by_keywords(self) -> ConcurentsByKeywordsResource:
        return ConcurentsByKeywordsResource(self._client)

    @cached_property
    def keywords_by_pages(self) -> KeywordsByPagesResource:
        return KeywordsByPagesResource(self._client)

    @cached_property
    def dictionary_ext_by_page(self) -> DictionaryExtByPageResource:
        return DictionaryExtByPageResource(self._client)

    @cached_property
    def dictionary_by_pages(self) -> DictionaryByPagesResource:
        return DictionaryByPagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def check_top(
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
    ) -> ToolCheckTopResponse:
        """
        Пример запроса `https://api.keys.so/tools/check-top?base=msk`

        Args:
          list: Список поисковых фраз

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
            "/tools/check-top",
            body=maybe_transform({"list": list}, tool_check_top_params.ToolCheckTopParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"base": base}, tool_check_top_params.ToolCheckTopParams),
            ),
            cast_to=ToolCheckTopResponse,
        )

    def check_top_concurents_domains(
        self,
        *,
        list: SequenceNotStr[str],
        base: Base | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCheckTopConcurentsDomainsResponse:
        """
        Пример запроса `https://api.keys.so/tools/check-top-concurents-domains?base=msk`

        Args:
          list: Список поисковых фраз

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          page: Текущая страница

          per_page: Записей на странице

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tools/check-top-concurents-domains",
            body=maybe_transform(
                {
                    "list": list,
                    "page": page,
                    "per_page": per_page,
                },
                tool_check_top_concurents_domains_params.ToolCheckTopConcurentsDomainsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"base": base}, tool_check_top_concurents_domains_params.ToolCheckTopConcurentsDomainsParams
                ),
            ),
            cast_to=ToolCheckTopConcurentsDomainsResponse,
        )

    def check_top_concurents_urls(
        self,
        *,
        list: SequenceNotStr[str],
        base: Base | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCheckTopConcurentsURLsResponse:
        """
        Пример запроса `https://api.keys.so/tools/check-top-concurents-urls?base=msk`

        Args:
          list: Список поисковых фраз

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          page: Текущая страница

          per_page: Записей на странице

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tools/check-top-concurents-urls",
            body=maybe_transform(
                {
                    "list": list,
                    "page": page,
                    "per_page": per_page,
                },
                tool_check_top_concurents_urls_params.ToolCheckTopConcurentsURLsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"base": base}, tool_check_top_concurents_urls_params.ToolCheckTopConcurentsURLsParams
                ),
            ),
            cast_to=ToolCheckTopConcurentsURLsResponse,
        )

    def combine(
        self,
        *,
        lists: Iterable[Iterable[object]],
        options: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Пример запроса `https://api.keys.so/tools/combine`

        Args:
          lists: Список поисковых фраз

          options: Дополнительные настройки: `Заключить в " "` - quotes `Заключить в «[ ]»` -
              brackets `Добавить комбинации без операторов` - simple
              `Добавить «+» к стоп-словам` - simple

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tools/combine",
            body=maybe_transform(
                {
                    "lists": lists,
                    "options": options,
                },
                tool_combine_params.ToolCombineParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def compare(
        self,
        *,
        left: SequenceNotStr[str],
        options: Literal["present_right", "uniq", "union", "present_left"],
        right: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCompareResponse:
        """
        Пример запроса `https://api.keys.so/tools/compare`

        Args:
          left: Список поисковых фраз

          options: Тип сравнения

          right: Список поисковых фраз

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tools/compare",
            body=maybe_transform(
                {
                    "left": left,
                    "options": options,
                    "right": right,
                },
                tool_compare_params.ToolCompareParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolCompareResponse,
        )

    def create_domains_batch(
        self,
        *,
        data: tool_create_domains_batch_params.Data,
        base: Base | Omit = omit,
        params: tool_create_domains_batch_params.Params | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCreateDomainsBatchResponse:
        """
        Пример запроса `https://api.keys.so/tools/domains-batch?base=msk`

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
            "/tools/domains-batch",
            body=maybe_transform(
                {
                    "data": data,
                    "params": params,
                },
                tool_create_domains_batch_params.ToolCreateDomainsBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"base": base}, tool_create_domains_batch_params.ToolCreateDomainsBatchParams),
            ),
            cast_to=ToolCreateDomainsBatchResponse,
        )

    def create_history_serp(
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
    ) -> ToolCreateHistorySerpResponse:
        """
        Пример запроса `https://api.keys.so/tools/history-serp?base=gru`

        Args:
          keyword: Поисковая фраза

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
            "/tools/history-serp",
            body=maybe_transform({"keyword": keyword}, tool_create_history_serp_params.ToolCreateHistorySerpParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"base": base}, tool_create_history_serp_params.ToolCreateHistorySerpParams),
            ),
            cast_to=ToolCreateHistorySerpResponse,
        )

    def create_unique(
        self,
        *,
        list: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCreateUniqueResponse:
        """
        Пример запроса `https://api.keys.so/tools/unique`

        Args:
          list: Список поисковых фраз

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tools/unique",
            body=maybe_transform({"list": list}, tool_create_unique_params.ToolCreateUniqueParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolCreateUniqueResponse,
        )

    def delete_double(
        self,
        *,
        list: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolDeleteDoubleResponse:
        """
        Args:
          list: Массив фраз для чистки дублей

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tools/delete_double",
            body=maybe_transform({"list": list}, tool_delete_double_params.ToolDeleteDoubleParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolDeleteDoubleResponse,
        )

    def list_site_themes(
        self,
        *,
        site: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        like: str | Omit = omit,
        max_pos: int | Omit = omit,
        max_ws: int | Omit = omit,
        max_wsk: int | Omit = omit,
        min_pos: int | Omit = omit,
        min_ws: int | Omit = omit,
        min_wsk: int | Omit = omit,
        not_like: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        qby_url: int | Omit = omit,
        sort: str | Omit = omit,
        words: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListSiteThemesResponse:
        """
        Пример запроса
        `https://api.keys.so/tools/site-themes?base=msk&site=keys.so&minWs=0&maxWs=999999999&minPos=1&maxPos=50&qbyUrl=1&words=1&like=%D0%BA%D0%BE%D0%BD%D0%BA%D1%83%D1%80%D0%B5%D0%BD%D1%82%D1%8B&notLike=%D1%82%D0%B5%D0%BC%D0%B0&sort=wsk%7Cdesc&page=1&per_page=25`

        Args:
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

          like: Похож

          max_pos: Позиция до

          max_ws: Частотность не более

          max_wsk: [!Частотность] не более

          min_pos: Позиция от

          min_ws: Частотность не менее

          min_wsk: [!Частотность] не менее

          not_like: Не похож

          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          qby_url: Запросов с одной страницы

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          words: Частотность не более

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/tools/site-themes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "site": site,
                        "base": base,
                        "filter": filter,
                        "like": like,
                        "max_pos": max_pos,
                        "max_ws": max_ws,
                        "max_wsk": max_wsk,
                        "min_pos": min_pos,
                        "min_ws": min_ws,
                        "min_wsk": min_wsk,
                        "not_like": not_like,
                        "page": page,
                        "per_page": per_page,
                        "qby_url": qby_url,
                        "sort": sort,
                        "words": words,
                    },
                    tool_list_site_themes_params.ToolListSiteThemesParams,
                ),
            ),
            cast_to=ToolListSiteThemesResponse,
        )

    def suggest(
        self,
        *,
        list: SequenceNotStr[str],
        region: Literal[
            1,
            2,
            4,
            5,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            20,
            21,
            22,
            23,
            24,
            25,
            28,
            30,
            33,
            35,
            36,
            37,
            38,
            39,
            41,
            42,
            43,
            45,
            47,
            48,
            49,
            50,
            51,
            53,
            54,
            56,
            62,
            63,
            64,
            65,
            66,
            67,
            75,
            76,
            77,
            149,
            159,
            172,
            187,
            191,
            192,
            193,
            195,
            197,
            213,
            225,
            239,
            973,
            1092,
            1104,
            1106,
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSuggestResponse:
        """
        Пример запроса `https://api.keys.so/tools/suggest`

        Args:
          list: Список исходных ключевых слов

          region: Код региона: `1` - Москва и Московская область `2` - Санкт-Петербург `4` -
              Белгород `5` - Иваново `7` - Кострома `8` - Курск `9` - Липецк `10` - Орел
              `11` - Рязань `12` - Смоленск `13` - Тамбов `14` - Тверь `15` - Тула `16` -
              Ярославль `20` - Архангельск `21` - Вологда `22` - Калининград `23` - Мурманск
              `24` - Великий Новгород `25` - Псков `28` - Махачкала `30` - Нальчик `33` -
              Владикавказ `35` - Краснодар `36` - Ставрополь `37` - Астрахань `38` - Волгоград
              `39` - Ростов-на-Дону `41` - Йошкар-Ола `42` - Саранск `43` - Казань `45` -
              Чебоксары `47` - Нижний Новгород `48` - Оренбург `49` - Пенза `50` - Пермь
              `51` - Самара `53` - Курган `54` - Екатеринбург `56` - Челябинск `62` -
              Красноярск `63` - Иркутск `64` - Кемерово `65` - Новосибирск `66` - Омск `67` -
              Томск `75` - Владивосток `76` - Хабаровск `77` - Благовещенск `149` - Беларусь
              `159` - Казахстан `172` - Уфа `187` - Украина `191` - Брянск `192` - Владимир
              `193` - Воронеж `195` - Ульяновск `197` - Барнаул `213` - Москва `225` - Россия
              `239` - Сочи `973` - Сургут `1092` - Назрань `1104` - Черкесск `1106` - Грозный

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tools/suggest",
            body=maybe_transform(
                {
                    "list": list,
                    "region": region,
                },
                tool_suggest_params.ToolSuggestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSuggestResponse,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def extended_keywords(self) -> AsyncExtendedKeywordsResource:
        return AsyncExtendedKeywordsResource(self._client)

    @cached_property
    def keywords_by_list(self) -> AsyncKeywordsByListResource:
        return AsyncKeywordsByListResource(self._client)

    @cached_property
    def concurents_by_keywords(self) -> AsyncConcurentsByKeywordsResource:
        return AsyncConcurentsByKeywordsResource(self._client)

    @cached_property
    def keywords_by_pages(self) -> AsyncKeywordsByPagesResource:
        return AsyncKeywordsByPagesResource(self._client)

    @cached_property
    def dictionary_ext_by_page(self) -> AsyncDictionaryExtByPageResource:
        return AsyncDictionaryExtByPageResource(self._client)

    @cached_property
    def dictionary_by_pages(self) -> AsyncDictionaryByPagesResource:
        return AsyncDictionaryByPagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    async def check_top(
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
    ) -> ToolCheckTopResponse:
        """
        Пример запроса `https://api.keys.so/tools/check-top?base=msk`

        Args:
          list: Список поисковых фраз

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
            "/tools/check-top",
            body=await async_maybe_transform({"list": list}, tool_check_top_params.ToolCheckTopParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"base": base}, tool_check_top_params.ToolCheckTopParams),
            ),
            cast_to=ToolCheckTopResponse,
        )

    async def check_top_concurents_domains(
        self,
        *,
        list: SequenceNotStr[str],
        base: Base | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCheckTopConcurentsDomainsResponse:
        """
        Пример запроса `https://api.keys.so/tools/check-top-concurents-domains?base=msk`

        Args:
          list: Список поисковых фраз

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          page: Текущая страница

          per_page: Записей на странице

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tools/check-top-concurents-domains",
            body=await async_maybe_transform(
                {
                    "list": list,
                    "page": page,
                    "per_page": per_page,
                },
                tool_check_top_concurents_domains_params.ToolCheckTopConcurentsDomainsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"base": base}, tool_check_top_concurents_domains_params.ToolCheckTopConcurentsDomainsParams
                ),
            ),
            cast_to=ToolCheckTopConcurentsDomainsResponse,
        )

    async def check_top_concurents_urls(
        self,
        *,
        list: SequenceNotStr[str],
        base: Base | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCheckTopConcurentsURLsResponse:
        """
        Пример запроса `https://api.keys.so/tools/check-top-concurents-urls?base=msk`

        Args:
          list: Список поисковых фраз

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          page: Текущая страница

          per_page: Записей на странице

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tools/check-top-concurents-urls",
            body=await async_maybe_transform(
                {
                    "list": list,
                    "page": page,
                    "per_page": per_page,
                },
                tool_check_top_concurents_urls_params.ToolCheckTopConcurentsURLsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"base": base}, tool_check_top_concurents_urls_params.ToolCheckTopConcurentsURLsParams
                ),
            ),
            cast_to=ToolCheckTopConcurentsURLsResponse,
        )

    async def combine(
        self,
        *,
        lists: Iterable[Iterable[object]],
        options: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Пример запроса `https://api.keys.so/tools/combine`

        Args:
          lists: Список поисковых фраз

          options: Дополнительные настройки: `Заключить в " "` - quotes `Заключить в «[ ]»` -
              brackets `Добавить комбинации без операторов` - simple
              `Добавить «+» к стоп-словам` - simple

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tools/combine",
            body=await async_maybe_transform(
                {
                    "lists": lists,
                    "options": options,
                },
                tool_combine_params.ToolCombineParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def compare(
        self,
        *,
        left: SequenceNotStr[str],
        options: Literal["present_right", "uniq", "union", "present_left"],
        right: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCompareResponse:
        """
        Пример запроса `https://api.keys.so/tools/compare`

        Args:
          left: Список поисковых фраз

          options: Тип сравнения

          right: Список поисковых фраз

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tools/compare",
            body=await async_maybe_transform(
                {
                    "left": left,
                    "options": options,
                    "right": right,
                },
                tool_compare_params.ToolCompareParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolCompareResponse,
        )

    async def create_domains_batch(
        self,
        *,
        data: tool_create_domains_batch_params.Data,
        base: Base | Omit = omit,
        params: tool_create_domains_batch_params.Params | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCreateDomainsBatchResponse:
        """
        Пример запроса `https://api.keys.so/tools/domains-batch?base=msk`

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
            "/tools/domains-batch",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "params": params,
                },
                tool_create_domains_batch_params.ToolCreateDomainsBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"base": base}, tool_create_domains_batch_params.ToolCreateDomainsBatchParams
                ),
            ),
            cast_to=ToolCreateDomainsBatchResponse,
        )

    async def create_history_serp(
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
    ) -> ToolCreateHistorySerpResponse:
        """
        Пример запроса `https://api.keys.so/tools/history-serp?base=gru`

        Args:
          keyword: Поисковая фраза

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
            "/tools/history-serp",
            body=await async_maybe_transform(
                {"keyword": keyword}, tool_create_history_serp_params.ToolCreateHistorySerpParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"base": base}, tool_create_history_serp_params.ToolCreateHistorySerpParams
                ),
            ),
            cast_to=ToolCreateHistorySerpResponse,
        )

    async def create_unique(
        self,
        *,
        list: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCreateUniqueResponse:
        """
        Пример запроса `https://api.keys.so/tools/unique`

        Args:
          list: Список поисковых фраз

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tools/unique",
            body=await async_maybe_transform({"list": list}, tool_create_unique_params.ToolCreateUniqueParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolCreateUniqueResponse,
        )

    async def delete_double(
        self,
        *,
        list: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolDeleteDoubleResponse:
        """
        Args:
          list: Массив фраз для чистки дублей

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tools/delete_double",
            body=await async_maybe_transform({"list": list}, tool_delete_double_params.ToolDeleteDoubleParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolDeleteDoubleResponse,
        )

    async def list_site_themes(
        self,
        *,
        site: str,
        base: Base | Omit = omit,
        filter: str | Omit = omit,
        like: str | Omit = omit,
        max_pos: int | Omit = omit,
        max_ws: int | Omit = omit,
        max_wsk: int | Omit = omit,
        min_pos: int | Omit = omit,
        min_ws: int | Omit = omit,
        min_wsk: int | Omit = omit,
        not_like: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        qby_url: int | Omit = omit,
        sort: str | Omit = omit,
        words: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListSiteThemesResponse:
        """
        Пример запроса
        `https://api.keys.so/tools/site-themes?base=msk&site=keys.so&minWs=0&maxWs=999999999&minPos=1&maxPos=50&qbyUrl=1&words=1&like=%D0%BA%D0%BE%D0%BD%D0%BA%D1%83%D1%80%D0%B5%D0%BD%D1%82%D1%8B&notLike=%D1%82%D0%B5%D0%BC%D0%B0&sort=wsk%7Cdesc&page=1&per_page=25`

        Args:
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

          like: Похож

          max_pos: Позиция до

          max_ws: Частотность не более

          max_wsk: [!Частотность] не более

          min_pos: Позиция от

          min_ws: Частотность не менее

          min_wsk: [!Частотность] не менее

          not_like: Не похож

          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          qby_url: Запросов с одной страницы

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          words: Частотность не более

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/tools/site-themes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "site": site,
                        "base": base,
                        "filter": filter,
                        "like": like,
                        "max_pos": max_pos,
                        "max_ws": max_ws,
                        "max_wsk": max_wsk,
                        "min_pos": min_pos,
                        "min_ws": min_ws,
                        "min_wsk": min_wsk,
                        "not_like": not_like,
                        "page": page,
                        "per_page": per_page,
                        "qby_url": qby_url,
                        "sort": sort,
                        "words": words,
                    },
                    tool_list_site_themes_params.ToolListSiteThemesParams,
                ),
            ),
            cast_to=ToolListSiteThemesResponse,
        )

    async def suggest(
        self,
        *,
        list: SequenceNotStr[str],
        region: Literal[
            1,
            2,
            4,
            5,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            20,
            21,
            22,
            23,
            24,
            25,
            28,
            30,
            33,
            35,
            36,
            37,
            38,
            39,
            41,
            42,
            43,
            45,
            47,
            48,
            49,
            50,
            51,
            53,
            54,
            56,
            62,
            63,
            64,
            65,
            66,
            67,
            75,
            76,
            77,
            149,
            159,
            172,
            187,
            191,
            192,
            193,
            195,
            197,
            213,
            225,
            239,
            973,
            1092,
            1104,
            1106,
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSuggestResponse:
        """
        Пример запроса `https://api.keys.so/tools/suggest`

        Args:
          list: Список исходных ключевых слов

          region: Код региона: `1` - Москва и Московская область `2` - Санкт-Петербург `4` -
              Белгород `5` - Иваново `7` - Кострома `8` - Курск `9` - Липецк `10` - Орел
              `11` - Рязань `12` - Смоленск `13` - Тамбов `14` - Тверь `15` - Тула `16` -
              Ярославль `20` - Архангельск `21` - Вологда `22` - Калининград `23` - Мурманск
              `24` - Великий Новгород `25` - Псков `28` - Махачкала `30` - Нальчик `33` -
              Владикавказ `35` - Краснодар `36` - Ставрополь `37` - Астрахань `38` - Волгоград
              `39` - Ростов-на-Дону `41` - Йошкар-Ола `42` - Саранск `43` - Казань `45` -
              Чебоксары `47` - Нижний Новгород `48` - Оренбург `49` - Пенза `50` - Пермь
              `51` - Самара `53` - Курган `54` - Екатеринбург `56` - Челябинск `62` -
              Красноярск `63` - Иркутск `64` - Кемерово `65` - Новосибирск `66` - Омск `67` -
              Томск `75` - Владивосток `76` - Хабаровск `77` - Благовещенск `149` - Беларусь
              `159` - Казахстан `172` - Уфа `187` - Украина `191` - Брянск `192` - Владимир
              `193` - Воронеж `195` - Ульяновск `197` - Барнаул `213` - Москва `225` - Россия
              `239` - Сочи `973` - Сургут `1092` - Назрань `1104` - Черкесск `1106` - Грозный

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tools/suggest",
            body=await async_maybe_transform(
                {
                    "list": list,
                    "region": region,
                },
                tool_suggest_params.ToolSuggestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSuggestResponse,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.check_top = to_raw_response_wrapper(
            tools.check_top,
        )
        self.check_top_concurents_domains = to_raw_response_wrapper(
            tools.check_top_concurents_domains,
        )
        self.check_top_concurents_urls = to_raw_response_wrapper(
            tools.check_top_concurents_urls,
        )
        self.combine = to_raw_response_wrapper(
            tools.combine,
        )
        self.compare = to_raw_response_wrapper(
            tools.compare,
        )
        self.create_domains_batch = to_raw_response_wrapper(
            tools.create_domains_batch,
        )
        self.create_history_serp = to_raw_response_wrapper(
            tools.create_history_serp,
        )
        self.create_unique = to_raw_response_wrapper(
            tools.create_unique,
        )
        self.delete_double = to_raw_response_wrapper(
            tools.delete_double,
        )
        self.list_site_themes = to_raw_response_wrapper(
            tools.list_site_themes,
        )
        self.suggest = to_raw_response_wrapper(
            tools.suggest,
        )

    @cached_property
    def extended_keywords(self) -> ExtendedKeywordsResourceWithRawResponse:
        return ExtendedKeywordsResourceWithRawResponse(self._tools.extended_keywords)

    @cached_property
    def keywords_by_list(self) -> KeywordsByListResourceWithRawResponse:
        return KeywordsByListResourceWithRawResponse(self._tools.keywords_by_list)

    @cached_property
    def concurents_by_keywords(self) -> ConcurentsByKeywordsResourceWithRawResponse:
        return ConcurentsByKeywordsResourceWithRawResponse(self._tools.concurents_by_keywords)

    @cached_property
    def keywords_by_pages(self) -> KeywordsByPagesResourceWithRawResponse:
        return KeywordsByPagesResourceWithRawResponse(self._tools.keywords_by_pages)

    @cached_property
    def dictionary_ext_by_page(self) -> DictionaryExtByPageResourceWithRawResponse:
        return DictionaryExtByPageResourceWithRawResponse(self._tools.dictionary_ext_by_page)

    @cached_property
    def dictionary_by_pages(self) -> DictionaryByPagesResourceWithRawResponse:
        return DictionaryByPagesResourceWithRawResponse(self._tools.dictionary_by_pages)


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.check_top = async_to_raw_response_wrapper(
            tools.check_top,
        )
        self.check_top_concurents_domains = async_to_raw_response_wrapper(
            tools.check_top_concurents_domains,
        )
        self.check_top_concurents_urls = async_to_raw_response_wrapper(
            tools.check_top_concurents_urls,
        )
        self.combine = async_to_raw_response_wrapper(
            tools.combine,
        )
        self.compare = async_to_raw_response_wrapper(
            tools.compare,
        )
        self.create_domains_batch = async_to_raw_response_wrapper(
            tools.create_domains_batch,
        )
        self.create_history_serp = async_to_raw_response_wrapper(
            tools.create_history_serp,
        )
        self.create_unique = async_to_raw_response_wrapper(
            tools.create_unique,
        )
        self.delete_double = async_to_raw_response_wrapper(
            tools.delete_double,
        )
        self.list_site_themes = async_to_raw_response_wrapper(
            tools.list_site_themes,
        )
        self.suggest = async_to_raw_response_wrapper(
            tools.suggest,
        )

    @cached_property
    def extended_keywords(self) -> AsyncExtendedKeywordsResourceWithRawResponse:
        return AsyncExtendedKeywordsResourceWithRawResponse(self._tools.extended_keywords)

    @cached_property
    def keywords_by_list(self) -> AsyncKeywordsByListResourceWithRawResponse:
        return AsyncKeywordsByListResourceWithRawResponse(self._tools.keywords_by_list)

    @cached_property
    def concurents_by_keywords(self) -> AsyncConcurentsByKeywordsResourceWithRawResponse:
        return AsyncConcurentsByKeywordsResourceWithRawResponse(self._tools.concurents_by_keywords)

    @cached_property
    def keywords_by_pages(self) -> AsyncKeywordsByPagesResourceWithRawResponse:
        return AsyncKeywordsByPagesResourceWithRawResponse(self._tools.keywords_by_pages)

    @cached_property
    def dictionary_ext_by_page(self) -> AsyncDictionaryExtByPageResourceWithRawResponse:
        return AsyncDictionaryExtByPageResourceWithRawResponse(self._tools.dictionary_ext_by_page)

    @cached_property
    def dictionary_by_pages(self) -> AsyncDictionaryByPagesResourceWithRawResponse:
        return AsyncDictionaryByPagesResourceWithRawResponse(self._tools.dictionary_by_pages)


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.check_top = to_streamed_response_wrapper(
            tools.check_top,
        )
        self.check_top_concurents_domains = to_streamed_response_wrapper(
            tools.check_top_concurents_domains,
        )
        self.check_top_concurents_urls = to_streamed_response_wrapper(
            tools.check_top_concurents_urls,
        )
        self.combine = to_streamed_response_wrapper(
            tools.combine,
        )
        self.compare = to_streamed_response_wrapper(
            tools.compare,
        )
        self.create_domains_batch = to_streamed_response_wrapper(
            tools.create_domains_batch,
        )
        self.create_history_serp = to_streamed_response_wrapper(
            tools.create_history_serp,
        )
        self.create_unique = to_streamed_response_wrapper(
            tools.create_unique,
        )
        self.delete_double = to_streamed_response_wrapper(
            tools.delete_double,
        )
        self.list_site_themes = to_streamed_response_wrapper(
            tools.list_site_themes,
        )
        self.suggest = to_streamed_response_wrapper(
            tools.suggest,
        )

    @cached_property
    def extended_keywords(self) -> ExtendedKeywordsResourceWithStreamingResponse:
        return ExtendedKeywordsResourceWithStreamingResponse(self._tools.extended_keywords)

    @cached_property
    def keywords_by_list(self) -> KeywordsByListResourceWithStreamingResponse:
        return KeywordsByListResourceWithStreamingResponse(self._tools.keywords_by_list)

    @cached_property
    def concurents_by_keywords(self) -> ConcurentsByKeywordsResourceWithStreamingResponse:
        return ConcurentsByKeywordsResourceWithStreamingResponse(self._tools.concurents_by_keywords)

    @cached_property
    def keywords_by_pages(self) -> KeywordsByPagesResourceWithStreamingResponse:
        return KeywordsByPagesResourceWithStreamingResponse(self._tools.keywords_by_pages)

    @cached_property
    def dictionary_ext_by_page(self) -> DictionaryExtByPageResourceWithStreamingResponse:
        return DictionaryExtByPageResourceWithStreamingResponse(self._tools.dictionary_ext_by_page)

    @cached_property
    def dictionary_by_pages(self) -> DictionaryByPagesResourceWithStreamingResponse:
        return DictionaryByPagesResourceWithStreamingResponse(self._tools.dictionary_by_pages)


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.check_top = async_to_streamed_response_wrapper(
            tools.check_top,
        )
        self.check_top_concurents_domains = async_to_streamed_response_wrapper(
            tools.check_top_concurents_domains,
        )
        self.check_top_concurents_urls = async_to_streamed_response_wrapper(
            tools.check_top_concurents_urls,
        )
        self.combine = async_to_streamed_response_wrapper(
            tools.combine,
        )
        self.compare = async_to_streamed_response_wrapper(
            tools.compare,
        )
        self.create_domains_batch = async_to_streamed_response_wrapper(
            tools.create_domains_batch,
        )
        self.create_history_serp = async_to_streamed_response_wrapper(
            tools.create_history_serp,
        )
        self.create_unique = async_to_streamed_response_wrapper(
            tools.create_unique,
        )
        self.delete_double = async_to_streamed_response_wrapper(
            tools.delete_double,
        )
        self.list_site_themes = async_to_streamed_response_wrapper(
            tools.list_site_themes,
        )
        self.suggest = async_to_streamed_response_wrapper(
            tools.suggest,
        )

    @cached_property
    def extended_keywords(self) -> AsyncExtendedKeywordsResourceWithStreamingResponse:
        return AsyncExtendedKeywordsResourceWithStreamingResponse(self._tools.extended_keywords)

    @cached_property
    def keywords_by_list(self) -> AsyncKeywordsByListResourceWithStreamingResponse:
        return AsyncKeywordsByListResourceWithStreamingResponse(self._tools.keywords_by_list)

    @cached_property
    def concurents_by_keywords(self) -> AsyncConcurentsByKeywordsResourceWithStreamingResponse:
        return AsyncConcurentsByKeywordsResourceWithStreamingResponse(self._tools.concurents_by_keywords)

    @cached_property
    def keywords_by_pages(self) -> AsyncKeywordsByPagesResourceWithStreamingResponse:
        return AsyncKeywordsByPagesResourceWithStreamingResponse(self._tools.keywords_by_pages)

    @cached_property
    def dictionary_ext_by_page(self) -> AsyncDictionaryExtByPageResourceWithStreamingResponse:
        return AsyncDictionaryExtByPageResourceWithStreamingResponse(self._tools.dictionary_ext_by_page)

    @cached_property
    def dictionary_by_pages(self) -> AsyncDictionaryByPagesResourceWithStreamingResponse:
        return AsyncDictionaryByPagesResourceWithStreamingResponse(self._tools.dictionary_by_pages)
