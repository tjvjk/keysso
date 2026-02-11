# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types import (
    MonitoringListResponse,
    MonitoringCreateResponse,
    MonitoringGetStateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonitoring:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Keysso) -> None:
        monitoring = client.monitoring.create(
            search_settings=[
                {
                    "engine": 0,
                    "region_id": 38,
                }
            ],
            tracking_item="keys.so",
            track_sub_domains=True,
        )
        assert_matches_type(MonitoringCreateResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Keysso) -> None:
        monitoring = client.monitoring.create(
            search_settings=[
                {
                    "engine": 0,
                    "region_id": 38,
                }
            ],
            tracking_item="keys.so",
            track_sub_domains=True,
            base="msk",
            cluster_uuid="f6ce68ad381acbb36e68b59971c70f12",
            keywords=["кластеризатор"],
            name="keys.so - мониторинг",
            serp=True,
            wordstat=True,
            ws_types=[0],
        )
        assert_matches_type(MonitoringCreateResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Keysso) -> None:
        response = client.monitoring.with_raw_response.create(
            search_settings=[
                {
                    "engine": 0,
                    "region_id": 38,
                }
            ],
            tracking_item="keys.so",
            track_sub_domains=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitoring = response.parse()
        assert_matches_type(MonitoringCreateResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Keysso) -> None:
        with client.monitoring.with_streaming_response.create(
            search_settings=[
                {
                    "engine": 0,
                    "region_id": 38,
                }
            ],
            tracking_item="keys.so",
            track_sub_domains=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitoring = response.parse()
            assert_matches_type(MonitoringCreateResponse, monitoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Keysso) -> None:
        monitoring = client.monitoring.list()
        assert_matches_type(MonitoringListResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Keysso) -> None:
        monitoring = client.monitoring.list(
            page=0,
            per_page=0,
            search="search",
            sort="sort",
        )
        assert_matches_type(MonitoringListResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Keysso) -> None:
        response = client.monitoring.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitoring = response.parse()
        assert_matches_type(MonitoringListResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Keysso) -> None:
        with client.monitoring.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitoring = response.parse()
            assert_matches_type(MonitoringListResponse, monitoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_state(self, client: Keysso) -> None:
        monitoring = client.monitoring.get_state(
            ids=[0],
        )
        assert_matches_type(MonitoringGetStateResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_state(self, client: Keysso) -> None:
        response = client.monitoring.with_raw_response.get_state(
            ids=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitoring = response.parse()
        assert_matches_type(MonitoringGetStateResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_state(self, client: Keysso) -> None:
        with client.monitoring.with_streaming_response.get_state(
            ids=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitoring = response.parse()
            assert_matches_type(MonitoringGetStateResponse, monitoring, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMonitoring:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeysso) -> None:
        monitoring = await async_client.monitoring.create(
            search_settings=[
                {
                    "engine": 0,
                    "region_id": 38,
                }
            ],
            tracking_item="keys.so",
            track_sub_domains=True,
        )
        assert_matches_type(MonitoringCreateResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeysso) -> None:
        monitoring = await async_client.monitoring.create(
            search_settings=[
                {
                    "engine": 0,
                    "region_id": 38,
                }
            ],
            tracking_item="keys.so",
            track_sub_domains=True,
            base="msk",
            cluster_uuid="f6ce68ad381acbb36e68b59971c70f12",
            keywords=["кластеризатор"],
            name="keys.so - мониторинг",
            serp=True,
            wordstat=True,
            ws_types=[0],
        )
        assert_matches_type(MonitoringCreateResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeysso) -> None:
        response = await async_client.monitoring.with_raw_response.create(
            search_settings=[
                {
                    "engine": 0,
                    "region_id": 38,
                }
            ],
            tracking_item="keys.so",
            track_sub_domains=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitoring = await response.parse()
        assert_matches_type(MonitoringCreateResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeysso) -> None:
        async with async_client.monitoring.with_streaming_response.create(
            search_settings=[
                {
                    "engine": 0,
                    "region_id": 38,
                }
            ],
            tracking_item="keys.so",
            track_sub_domains=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitoring = await response.parse()
            assert_matches_type(MonitoringCreateResponse, monitoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeysso) -> None:
        monitoring = await async_client.monitoring.list()
        assert_matches_type(MonitoringListResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeysso) -> None:
        monitoring = await async_client.monitoring.list(
            page=0,
            per_page=0,
            search="search",
            sort="sort",
        )
        assert_matches_type(MonitoringListResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeysso) -> None:
        response = await async_client.monitoring.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitoring = await response.parse()
        assert_matches_type(MonitoringListResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeysso) -> None:
        async with async_client.monitoring.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitoring = await response.parse()
            assert_matches_type(MonitoringListResponse, monitoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_state(self, async_client: AsyncKeysso) -> None:
        monitoring = await async_client.monitoring.get_state(
            ids=[0],
        )
        assert_matches_type(MonitoringGetStateResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_state(self, async_client: AsyncKeysso) -> None:
        response = await async_client.monitoring.with_raw_response.get_state(
            ids=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitoring = await response.parse()
        assert_matches_type(MonitoringGetStateResponse, monitoring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_state(self, async_client: AsyncKeysso) -> None:
        async with async_client.monitoring.with_streaming_response.get_state(
            ids=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitoring = await response.parse()
            assert_matches_type(MonitoringGetStateResponse, monitoring, path=["response"])

        assert cast(Any, response.is_closed) is True
