# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

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
from ...types.projects import competitor_list_params, competitor_compare_params
from ...types.projects.competitor_list_response import CompetitorListResponse
from ...types.projects.competitor_compare_response import CompetitorCompareResponse

__all__ = ["CompetitorsResource", "AsyncCompetitorsResource"]


class CompetitorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompetitorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return CompetitorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompetitorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return CompetitorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        project_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompetitorListResponse:
        """
        Пример запроса `https://api.keys.so/projects/competitors?projectId=12333`

        Args:
          project_id: Идентификатор проекта

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/projects/competitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, competitor_list_params.CompetitorListParams),
            ),
            cast_to=CompetitorListResponse,
        )

    def compare(
        self,
        *,
        domains: SequenceNotStr[str],
        view: Literal["organic", "context"],
        type: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompetitorCompareResponse:
        """
        Пример запроса `https://api.keys.so/projects/competitors/compare`

        Args:
          domains: Конкуренты

          view: Отчет вернет результаты для органики(`organic`) или контекста(`context`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/projects/competitors/compare",
            body=maybe_transform(
                {
                    "domains": domains,
                    "view": view,
                    "type": type,
                },
                competitor_compare_params.CompetitorCompareParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompetitorCompareResponse,
        )


class AsyncCompetitorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompetitorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncCompetitorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompetitorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncCompetitorsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        project_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompetitorListResponse:
        """
        Пример запроса `https://api.keys.so/projects/competitors?projectId=12333`

        Args:
          project_id: Идентификатор проекта

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/projects/competitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, competitor_list_params.CompetitorListParams
                ),
            ),
            cast_to=CompetitorListResponse,
        )

    async def compare(
        self,
        *,
        domains: SequenceNotStr[str],
        view: Literal["organic", "context"],
        type: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompetitorCompareResponse:
        """
        Пример запроса `https://api.keys.so/projects/competitors/compare`

        Args:
          domains: Конкуренты

          view: Отчет вернет результаты для органики(`organic`) или контекста(`context`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/projects/competitors/compare",
            body=await async_maybe_transform(
                {
                    "domains": domains,
                    "view": view,
                    "type": type,
                },
                competitor_compare_params.CompetitorCompareParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompetitorCompareResponse,
        )


class CompetitorsResourceWithRawResponse:
    def __init__(self, competitors: CompetitorsResource) -> None:
        self._competitors = competitors

        self.list = to_raw_response_wrapper(
            competitors.list,
        )
        self.compare = to_raw_response_wrapper(
            competitors.compare,
        )


class AsyncCompetitorsResourceWithRawResponse:
    def __init__(self, competitors: AsyncCompetitorsResource) -> None:
        self._competitors = competitors

        self.list = async_to_raw_response_wrapper(
            competitors.list,
        )
        self.compare = async_to_raw_response_wrapper(
            competitors.compare,
        )


class CompetitorsResourceWithStreamingResponse:
    def __init__(self, competitors: CompetitorsResource) -> None:
        self._competitors = competitors

        self.list = to_streamed_response_wrapper(
            competitors.list,
        )
        self.compare = to_streamed_response_wrapper(
            competitors.compare,
        )


class AsyncCompetitorsResourceWithStreamingResponse:
    def __init__(self, competitors: AsyncCompetitorsResource) -> None:
        self._competitors = competitors

        self.list = async_to_streamed_response_wrapper(
            competitors.list,
        )
        self.compare = async_to_streamed_response_wrapper(
            competitors.compare,
        )
