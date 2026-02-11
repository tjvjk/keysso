# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...types import monitoring_list_params, monitoring_create_params, monitoring_get_state_params
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
from ...types.report.base import Base
from ...types.clustering.items import Items
from ...types.search_setting_param import SearchSettingParam
from ...types.monitoring_list_response import MonitoringListResponse
from ...types.monitoring_create_response import MonitoringCreateResponse
from ...types.monitoring_get_state_response import MonitoringGetStateResponse

__all__ = ["MonitoringResource", "AsyncMonitoringResource"]


class MonitoringResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MonitoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return MonitoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonitoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return MonitoringResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        search_settings: Iterable[SearchSettingParam],
        tracking_item: str,
        track_sub_domains: bool,
        base: Base | Omit = omit,
        cluster_uuid: str | Omit = omit,
        keywords: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        serp: bool | Omit = omit,
        wordstat: bool | Omit = omit,
        ws_types: Iterable[Items] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitoringCreateResponse:
        """
        Пример запроса `https://api.keys.so/monitoring`

        Args:
          search_settings: Список настроек поисковых систем и регионов

          tracking_item: Элемент отслеживания (домен/url)

          track_sub_domains: Флаг отслеживания поддоменов

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          cluster_uuid: Уникальный идентификатор кластеризатора

          keywords: Список фраз

          name: Название проекта

          serp: Флаг для включения SERP

          wordstat: Флаг для включения статистики слов

          ws_types: Типы частотности: `0` - Wordstat `1` - "!Wordstat" `2` - "[!Wordstat]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/monitoring",
            body=maybe_transform(
                {
                    "search_settings": search_settings,
                    "tracking_item": tracking_item,
                    "track_sub_domains": track_sub_domains,
                    "base": base,
                    "cluster_uuid": cluster_uuid,
                    "keywords": keywords,
                    "name": name,
                    "serp": serp,
                    "wordstat": wordstat,
                    "ws_types": ws_types,
                },
                monitoring_create_params.MonitoringCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitoringCreateResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitoringListResponse:
        """
        Пример запроса `https://api.keys.so/monitoring`

        Args:
          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          search: Поиск по названию проекта и ключевым словам

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
            "/monitoring",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "sort": sort,
                    },
                    monitoring_list_params.MonitoringListParams,
                ),
            ),
            cast_to=MonitoringListResponse,
        )

    def get_state(
        self,
        *,
        ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitoringGetStateResponse:
        """
        Пример запроса
        `https://api.keys.so/monitoring/state?ids[]=123&ids[]=456&ids[]=789`

        Args:
          ids: Список идентификаторов проектов для получения статусов

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/monitoring/state",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, monitoring_get_state_params.MonitoringGetStateParams),
            ),
            cast_to=MonitoringGetStateResponse,
        )


class AsyncMonitoringResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMonitoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMonitoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonitoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return AsyncMonitoringResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        search_settings: Iterable[SearchSettingParam],
        tracking_item: str,
        track_sub_domains: bool,
        base: Base | Omit = omit,
        cluster_uuid: str | Omit = omit,
        keywords: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        serp: bool | Omit = omit,
        wordstat: bool | Omit = omit,
        ws_types: Iterable[Items] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitoringCreateResponse:
        """
        Пример запроса `https://api.keys.so/monitoring`

        Args:
          search_settings: Список настроек поисковых систем и регионов

          tracking_item: Элемент отслеживания (домен/url)

          track_sub_domains: Флаг отслеживания поддоменов

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          cluster_uuid: Уникальный идентификатор кластеризатора

          keywords: Список фраз

          name: Название проекта

          serp: Флаг для включения SERP

          wordstat: Флаг для включения статистики слов

          ws_types: Типы частотности: `0` - Wordstat `1` - "!Wordstat" `2` - "[!Wordstat]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/monitoring",
            body=await async_maybe_transform(
                {
                    "search_settings": search_settings,
                    "tracking_item": tracking_item,
                    "track_sub_domains": track_sub_domains,
                    "base": base,
                    "cluster_uuid": cluster_uuid,
                    "keywords": keywords,
                    "name": name,
                    "serp": serp,
                    "wordstat": wordstat,
                    "ws_types": ws_types,
                },
                monitoring_create_params.MonitoringCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitoringCreateResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitoringListResponse:
        """
        Пример запроса `https://api.keys.so/monitoring`

        Args:
          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          search: Поиск по названию проекта и ключевым словам

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
            "/monitoring",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "sort": sort,
                    },
                    monitoring_list_params.MonitoringListParams,
                ),
            ),
            cast_to=MonitoringListResponse,
        )

    async def get_state(
        self,
        *,
        ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitoringGetStateResponse:
        """
        Пример запроса
        `https://api.keys.so/monitoring/state?ids[]=123&ids[]=456&ids[]=789`

        Args:
          ids: Список идентификаторов проектов для получения статусов

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/monitoring/state",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ids": ids}, monitoring_get_state_params.MonitoringGetStateParams),
            ),
            cast_to=MonitoringGetStateResponse,
        )


class MonitoringResourceWithRawResponse:
    def __init__(self, monitoring: MonitoringResource) -> None:
        self._monitoring = monitoring

        self.create = to_raw_response_wrapper(
            monitoring.create,
        )
        self.list = to_raw_response_wrapper(
            monitoring.list,
        )
        self.get_state = to_raw_response_wrapper(
            monitoring.get_state,
        )


class AsyncMonitoringResourceWithRawResponse:
    def __init__(self, monitoring: AsyncMonitoringResource) -> None:
        self._monitoring = monitoring

        self.create = async_to_raw_response_wrapper(
            monitoring.create,
        )
        self.list = async_to_raw_response_wrapper(
            monitoring.list,
        )
        self.get_state = async_to_raw_response_wrapper(
            monitoring.get_state,
        )


class MonitoringResourceWithStreamingResponse:
    def __init__(self, monitoring: MonitoringResource) -> None:
        self._monitoring = monitoring

        self.create = to_streamed_response_wrapper(
            monitoring.create,
        )
        self.list = to_streamed_response_wrapper(
            monitoring.list,
        )
        self.get_state = to_streamed_response_wrapper(
            monitoring.get_state,
        )


class AsyncMonitoringResourceWithStreamingResponse:
    def __init__(self, monitoring: AsyncMonitoringResource) -> None:
        self._monitoring = monitoring

        self.create = async_to_streamed_response_wrapper(
            monitoring.create,
        )
        self.list = async_to_streamed_response_wrapper(
            monitoring.list,
        )
        self.get_state = async_to_streamed_response_wrapper(
            monitoring.get_state,
        )
