# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.projects import (
    CompetitorListResponse,
    CompetitorCompareResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompetitors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Keysso) -> None:
        competitor = client.projects.competitors.list()
        assert_matches_type(CompetitorListResponse, competitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Keysso) -> None:
        competitor = client.projects.competitors.list(
            project_id=12333,
        )
        assert_matches_type(CompetitorListResponse, competitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Keysso) -> None:
        response = client.projects.competitors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        competitor = response.parse()
        assert_matches_type(CompetitorListResponse, competitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Keysso) -> None:
        with client.projects.competitors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            competitor = response.parse()
            assert_matches_type(CompetitorListResponse, competitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare(self, client: Keysso) -> None:
        competitor = client.projects.competitors.compare(
            domains=["senler.ru", "sigmasms.ru", "smsdar.ru", "smspobeda.ru", "bandlink.media"],
            view="organic",
        )
        assert_matches_type(CompetitorCompareResponse, competitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare_with_all_params(self, client: Keysso) -> None:
        competitor = client.projects.competitors.compare(
            domains=["senler.ru", "sigmasms.ru", "smsdar.ru", "smspobeda.ru", "bandlink.media"],
            view="organic",
            type=1,
        )
        assert_matches_type(CompetitorCompareResponse, competitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_compare(self, client: Keysso) -> None:
        response = client.projects.competitors.with_raw_response.compare(
            domains=["senler.ru", "sigmasms.ru", "smsdar.ru", "smspobeda.ru", "bandlink.media"],
            view="organic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        competitor = response.parse()
        assert_matches_type(CompetitorCompareResponse, competitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_compare(self, client: Keysso) -> None:
        with client.projects.competitors.with_streaming_response.compare(
            domains=["senler.ru", "sigmasms.ru", "smsdar.ru", "smspobeda.ru", "bandlink.media"],
            view="organic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            competitor = response.parse()
            assert_matches_type(CompetitorCompareResponse, competitor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompetitors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeysso) -> None:
        competitor = await async_client.projects.competitors.list()
        assert_matches_type(CompetitorListResponse, competitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeysso) -> None:
        competitor = await async_client.projects.competitors.list(
            project_id=12333,
        )
        assert_matches_type(CompetitorListResponse, competitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeysso) -> None:
        response = await async_client.projects.competitors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        competitor = await response.parse()
        assert_matches_type(CompetitorListResponse, competitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeysso) -> None:
        async with async_client.projects.competitors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            competitor = await response.parse()
            assert_matches_type(CompetitorListResponse, competitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare(self, async_client: AsyncKeysso) -> None:
        competitor = await async_client.projects.competitors.compare(
            domains=["senler.ru", "sigmasms.ru", "smsdar.ru", "smspobeda.ru", "bandlink.media"],
            view="organic",
        )
        assert_matches_type(CompetitorCompareResponse, competitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare_with_all_params(self, async_client: AsyncKeysso) -> None:
        competitor = await async_client.projects.competitors.compare(
            domains=["senler.ru", "sigmasms.ru", "smsdar.ru", "smspobeda.ru", "bandlink.media"],
            view="organic",
            type=1,
        )
        assert_matches_type(CompetitorCompareResponse, competitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_compare(self, async_client: AsyncKeysso) -> None:
        response = await async_client.projects.competitors.with_raw_response.compare(
            domains=["senler.ru", "sigmasms.ru", "smsdar.ru", "smspobeda.ru", "bandlink.media"],
            view="organic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        competitor = await response.parse()
        assert_matches_type(CompetitorCompareResponse, competitor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_compare(self, async_client: AsyncKeysso) -> None:
        async with async_client.projects.competitors.with_streaming_response.compare(
            domains=["senler.ru", "sigmasms.ru", "smsdar.ru", "smspobeda.ru", "bandlink.media"],
            view="organic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            competitor = await response.parse()
            assert_matches_type(CompetitorCompareResponse, competitor, path=["response"])

        assert cast(Any, response.is_closed) is True
