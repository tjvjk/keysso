# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...types import ai_tracker_list_params, ai_tracker_create_params, ai_tracker_get_state_params
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
from ...types.system_item import SystemItem
from ...types.ai_tracker_list_response import AITrackerListResponse
from ...types.ai_tracker_create_response import AITrackerCreateResponse
from ...types.ai_tracker_get_state_response import AITrackerGetStateResponse

__all__ = ["AITrackerResource", "AsyncAITrackerResource"]


class AITrackerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AITrackerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return AITrackerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AITrackerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return AITrackerResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        brand: str,
        description: SequenceNotStr[str],
        systems: Iterable[SystemItem],
        competitors: SequenceNotStr[str] | Omit = omit,
        prompts: Iterable[ai_tracker_create_params.Prompt] | Omit = omit,
        start: bool | Omit = omit,
        synonyms: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITrackerCreateResponse:
        """
        Пример запроса `https://api.keys.so/ai_tracker`

        Args:
          brand: Название бренда

          description: Вид деятельности, чем занимается

          systems: Массив идентификаторов систем ИИ: `1` - GigaChat `3` - DeepSeek `6` - OpenAI
              `7` - Grok

          competitors: Список конкурентов (названия брендов)

          prompts: Список промтов для генерации запросов Каждый элемент может содержать фразу и
              необязательные группы.

          start: Флаг автозапуска проекта после создания

          synonyms: Синонимы бренда, варианты написания

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai_tracker",
            body=maybe_transform(
                {
                    "brand": brand,
                    "description": description,
                    "systems": systems,
                    "competitors": competitors,
                    "prompts": prompts,
                    "start": start,
                    "synonyms": synonyms,
                },
                ai_tracker_create_params.AITrackerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITrackerCreateResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITrackerListResponse:
        """
        Пример запроса `https://api.keys.so/ai_tracker`

        Args:
          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          search: Поиск по названию проекта или бренду

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai_tracker",
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
                    },
                    ai_tracker_list_params.AITrackerListParams,
                ),
            ),
            cast_to=AITrackerListResponse,
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
    ) -> AITrackerGetStateResponse:
        """
        Пример запроса
        `https://api.keys.so/ai_tracker/state?ids[]=123&ids[]=456&ids[]=789`

        Args:
          ids: Список идентификаторов проектов для получения прогресса

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai_tracker/state",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, ai_tracker_get_state_params.AITrackerGetStateParams),
            ),
            cast_to=AITrackerGetStateResponse,
        )


class AsyncAITrackerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAITrackerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAITrackerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAITrackerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return AsyncAITrackerResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        brand: str,
        description: SequenceNotStr[str],
        systems: Iterable[SystemItem],
        competitors: SequenceNotStr[str] | Omit = omit,
        prompts: Iterable[ai_tracker_create_params.Prompt] | Omit = omit,
        start: bool | Omit = omit,
        synonyms: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITrackerCreateResponse:
        """
        Пример запроса `https://api.keys.so/ai_tracker`

        Args:
          brand: Название бренда

          description: Вид деятельности, чем занимается

          systems: Массив идентификаторов систем ИИ: `1` - GigaChat `3` - DeepSeek `6` - OpenAI
              `7` - Grok

          competitors: Список конкурентов (названия брендов)

          prompts: Список промтов для генерации запросов Каждый элемент может содержать фразу и
              необязательные группы.

          start: Флаг автозапуска проекта после создания

          synonyms: Синонимы бренда, варианты написания

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai_tracker",
            body=await async_maybe_transform(
                {
                    "brand": brand,
                    "description": description,
                    "systems": systems,
                    "competitors": competitors,
                    "prompts": prompts,
                    "start": start,
                    "synonyms": synonyms,
                },
                ai_tracker_create_params.AITrackerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITrackerCreateResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITrackerListResponse:
        """
        Пример запроса `https://api.keys.so/ai_tracker`

        Args:
          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          search: Поиск по названию проекта или бренду

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai_tracker",
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
                    },
                    ai_tracker_list_params.AITrackerListParams,
                ),
            ),
            cast_to=AITrackerListResponse,
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
    ) -> AITrackerGetStateResponse:
        """
        Пример запроса
        `https://api.keys.so/ai_tracker/state?ids[]=123&ids[]=456&ids[]=789`

        Args:
          ids: Список идентификаторов проектов для получения прогресса

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai_tracker/state",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ids": ids}, ai_tracker_get_state_params.AITrackerGetStateParams),
            ),
            cast_to=AITrackerGetStateResponse,
        )


class AITrackerResourceWithRawResponse:
    def __init__(self, ai_tracker: AITrackerResource) -> None:
        self._ai_tracker = ai_tracker

        self.create = to_raw_response_wrapper(
            ai_tracker.create,
        )
        self.list = to_raw_response_wrapper(
            ai_tracker.list,
        )
        self.get_state = to_raw_response_wrapper(
            ai_tracker.get_state,
        )


class AsyncAITrackerResourceWithRawResponse:
    def __init__(self, ai_tracker: AsyncAITrackerResource) -> None:
        self._ai_tracker = ai_tracker

        self.create = async_to_raw_response_wrapper(
            ai_tracker.create,
        )
        self.list = async_to_raw_response_wrapper(
            ai_tracker.list,
        )
        self.get_state = async_to_raw_response_wrapper(
            ai_tracker.get_state,
        )


class AITrackerResourceWithStreamingResponse:
    def __init__(self, ai_tracker: AITrackerResource) -> None:
        self._ai_tracker = ai_tracker

        self.create = to_streamed_response_wrapper(
            ai_tracker.create,
        )
        self.list = to_streamed_response_wrapper(
            ai_tracker.list,
        )
        self.get_state = to_streamed_response_wrapper(
            ai_tracker.get_state,
        )


class AsyncAITrackerResourceWithStreamingResponse:
    def __init__(self, ai_tracker: AsyncAITrackerResource) -> None:
        self._ai_tracker = ai_tracker

        self.create = async_to_streamed_response_wrapper(
            ai_tracker.create,
        )
        self.list = async_to_streamed_response_wrapper(
            ai_tracker.list,
        )
        self.get_state = async_to_streamed_response_wrapper(
            ai_tracker.get_state,
        )
