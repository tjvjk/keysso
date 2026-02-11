# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types import (
    RobotListDatesResponse,
    RobotRetrieveDataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRobots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_dates(self, client: Keysso) -> None:
        robot = client.robots.list_dates(
            domain="domain",
        )
        assert_matches_type(RobotListDatesResponse, robot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_dates(self, client: Keysso) -> None:
        response = client.robots.with_raw_response.list_dates(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        robot = response.parse()
        assert_matches_type(RobotListDatesResponse, robot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_dates(self, client: Keysso) -> None:
        with client.robots.with_streaming_response.list_dates(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            robot = response.parse()
            assert_matches_type(RobotListDatesResponse, robot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_data(self, client: Keysso) -> None:
        robot = client.robots.retrieve_data(
            domain="domain",
        )
        assert_matches_type(RobotRetrieveDataResponse, robot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_data_with_all_params(self, client: Keysso) -> None:
        robot = client.robots.retrieve_data(
            domain="domain",
            date="date",
        )
        assert_matches_type(RobotRetrieveDataResponse, robot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_data(self, client: Keysso) -> None:
        response = client.robots.with_raw_response.retrieve_data(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        robot = response.parse()
        assert_matches_type(RobotRetrieveDataResponse, robot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_data(self, client: Keysso) -> None:
        with client.robots.with_streaming_response.retrieve_data(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            robot = response.parse()
            assert_matches_type(RobotRetrieveDataResponse, robot, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRobots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_dates(self, async_client: AsyncKeysso) -> None:
        robot = await async_client.robots.list_dates(
            domain="domain",
        )
        assert_matches_type(RobotListDatesResponse, robot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_dates(self, async_client: AsyncKeysso) -> None:
        response = await async_client.robots.with_raw_response.list_dates(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        robot = await response.parse()
        assert_matches_type(RobotListDatesResponse, robot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_dates(self, async_client: AsyncKeysso) -> None:
        async with async_client.robots.with_streaming_response.list_dates(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            robot = await response.parse()
            assert_matches_type(RobotListDatesResponse, robot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_data(self, async_client: AsyncKeysso) -> None:
        robot = await async_client.robots.retrieve_data(
            domain="domain",
        )
        assert_matches_type(RobotRetrieveDataResponse, robot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_data_with_all_params(self, async_client: AsyncKeysso) -> None:
        robot = await async_client.robots.retrieve_data(
            domain="domain",
            date="date",
        )
        assert_matches_type(RobotRetrieveDataResponse, robot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_data(self, async_client: AsyncKeysso) -> None:
        response = await async_client.robots.with_raw_response.retrieve_data(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        robot = await response.parse()
        assert_matches_type(RobotRetrieveDataResponse, robot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_data(self, async_client: AsyncKeysso) -> None:
        async with async_client.robots.with_streaming_response.retrieve_data(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            robot = await response.parse()
            assert_matches_type(RobotRetrieveDataResponse, robot, path=["response"])

        assert cast(Any, response.is_closed) is True
