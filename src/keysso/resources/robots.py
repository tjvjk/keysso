# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import robot_list_dates_params, robot_retrieve_data_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.robot_list_dates_response import RobotListDatesResponse
from ..types.robot_retrieve_data_response import RobotRetrieveDataResponse

__all__ = ["RobotsResource", "AsyncRobotsResource"]


class RobotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RobotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return RobotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RobotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return RobotsResourceWithStreamingResponse(self)

    def list_dates(
        self,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RobotListDatesResponse:
        """
        Пример запроса `https://api.keys.so/robots/dates?domain=keys.so`

        Args:
          domain: Имя домена

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/robots/dates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"domain": domain}, robot_list_dates_params.RobotListDatesParams),
            ),
            cast_to=RobotListDatesResponse,
        )

    def retrieve_data(
        self,
        *,
        domain: str,
        date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RobotRetrieveDataResponse:
        """
        Пример запроса `https://api.keys.so/robots/data?domain=keys.so`

        Args:
          domain: Имя домена

          date: Дата изменения, если не указана - последнее изменение

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/robots/data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "date": date,
                    },
                    robot_retrieve_data_params.RobotRetrieveDataParams,
                ),
            ),
            cast_to=RobotRetrieveDataResponse,
        )


class AsyncRobotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRobotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRobotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRobotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/keysso-python#with_streaming_response
        """
        return AsyncRobotsResourceWithStreamingResponse(self)

    async def list_dates(
        self,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RobotListDatesResponse:
        """
        Пример запроса `https://api.keys.so/robots/dates?domain=keys.so`

        Args:
          domain: Имя домена

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/robots/dates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"domain": domain}, robot_list_dates_params.RobotListDatesParams),
            ),
            cast_to=RobotListDatesResponse,
        )

    async def retrieve_data(
        self,
        *,
        domain: str,
        date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RobotRetrieveDataResponse:
        """
        Пример запроса `https://api.keys.so/robots/data?domain=keys.so`

        Args:
          domain: Имя домена

          date: Дата изменения, если не указана - последнее изменение

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/robots/data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "date": date,
                    },
                    robot_retrieve_data_params.RobotRetrieveDataParams,
                ),
            ),
            cast_to=RobotRetrieveDataResponse,
        )


class RobotsResourceWithRawResponse:
    def __init__(self, robots: RobotsResource) -> None:
        self._robots = robots

        self.list_dates = to_raw_response_wrapper(
            robots.list_dates,
        )
        self.retrieve_data = to_raw_response_wrapper(
            robots.retrieve_data,
        )


class AsyncRobotsResourceWithRawResponse:
    def __init__(self, robots: AsyncRobotsResource) -> None:
        self._robots = robots

        self.list_dates = async_to_raw_response_wrapper(
            robots.list_dates,
        )
        self.retrieve_data = async_to_raw_response_wrapper(
            robots.retrieve_data,
        )


class RobotsResourceWithStreamingResponse:
    def __init__(self, robots: RobotsResource) -> None:
        self._robots = robots

        self.list_dates = to_streamed_response_wrapper(
            robots.list_dates,
        )
        self.retrieve_data = to_streamed_response_wrapper(
            robots.retrieve_data,
        )


class AsyncRobotsResourceWithStreamingResponse:
    def __init__(self, robots: AsyncRobotsResource) -> None:
        self._robots = robots

        self.list_dates = async_to_streamed_response_wrapper(
            robots.list_dates,
        )
        self.retrieve_data = async_to_streamed_response_wrapper(
            robots.retrieve_data,
        )
