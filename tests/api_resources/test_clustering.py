# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types import (
    ClusteringListResponse,
    ClusteringCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClustering:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Keysso) -> None:
        clustering = client.clustering.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        )
        assert_matches_type(ClusteringCreateResponse, clustering, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Keysso) -> None:
        clustering = client.clustering.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
            base="msk",
        )
        assert_matches_type(ClusteringCreateResponse, clustering, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Keysso) -> None:
        response = client.clustering.with_raw_response.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clustering = response.parse()
        assert_matches_type(ClusteringCreateResponse, clustering, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Keysso) -> None:
        with client.clustering.with_streaming_response.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clustering = response.parse()
            assert_matches_type(ClusteringCreateResponse, clustering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Keysso) -> None:
        clustering = client.clustering.list()
        assert_matches_type(ClusteringListResponse, clustering, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Keysso) -> None:
        clustering = client.clustering.list(
            is_main=True,
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(ClusteringListResponse, clustering, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Keysso) -> None:
        response = client.clustering.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clustering = response.parse()
        assert_matches_type(ClusteringListResponse, clustering, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Keysso) -> None:
        with client.clustering.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clustering = response.parse()
            assert_matches_type(ClusteringListResponse, clustering, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClustering:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeysso) -> None:
        clustering = await async_client.clustering.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        )
        assert_matches_type(ClusteringCreateResponse, clustering, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeysso) -> None:
        clustering = await async_client.clustering.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
            base="msk",
        )
        assert_matches_type(ClusteringCreateResponse, clustering, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeysso) -> None:
        response = await async_client.clustering.with_raw_response.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clustering = await response.parse()
        assert_matches_type(ClusteringCreateResponse, clustering, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeysso) -> None:
        async with async_client.clustering.with_streaming_response.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clustering = await response.parse()
            assert_matches_type(ClusteringCreateResponse, clustering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeysso) -> None:
        clustering = await async_client.clustering.list()
        assert_matches_type(ClusteringListResponse, clustering, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeysso) -> None:
        clustering = await async_client.clustering.list(
            is_main=True,
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(ClusteringListResponse, clustering, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeysso) -> None:
        response = await async_client.clustering.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clustering = await response.parse()
        assert_matches_type(ClusteringListResponse, clustering, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeysso) -> None:
        async with async_client.clustering.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clustering = await response.parse()
            assert_matches_type(ClusteringListResponse, clustering, path=["response"])

        assert cast(Any, response.is_closed) is True
