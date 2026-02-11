# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types import SerpListResponse, SerpCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSerp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Keysso) -> None:
        serp = client.serp.create(
            data={},
        )
        assert_matches_type(SerpCreateResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Keysso) -> None:
        serp = client.serp.create(
            data={
                "name": "Имя проекта",
                "region_id": 38,
                "search_engine": 0,
                "top_number": 10,
                "words": ["фраза1", "фраза2", "фраза3"],
            },
        )
        assert_matches_type(SerpCreateResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Keysso) -> None:
        response = client.serp.with_raw_response.create(
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        serp = response.parse()
        assert_matches_type(SerpCreateResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Keysso) -> None:
        with client.serp.with_streaming_response.create(
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            serp = response.parse()
            assert_matches_type(SerpCreateResponse, serp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Keysso) -> None:
        serp = client.serp.list()
        assert_matches_type(SerpListResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Keysso) -> None:
        serp = client.serp.list(
            is_main=True,
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(SerpListResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Keysso) -> None:
        response = client.serp.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        serp = response.parse()
        assert_matches_type(SerpListResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Keysso) -> None:
        with client.serp.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            serp = response.parse()
            assert_matches_type(SerpListResponse, serp, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSerp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeysso) -> None:
        serp = await async_client.serp.create(
            data={},
        )
        assert_matches_type(SerpCreateResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeysso) -> None:
        serp = await async_client.serp.create(
            data={
                "name": "Имя проекта",
                "region_id": 38,
                "search_engine": 0,
                "top_number": 10,
                "words": ["фраза1", "фраза2", "фраза3"],
            },
        )
        assert_matches_type(SerpCreateResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeysso) -> None:
        response = await async_client.serp.with_raw_response.create(
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        serp = await response.parse()
        assert_matches_type(SerpCreateResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeysso) -> None:
        async with async_client.serp.with_streaming_response.create(
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            serp = await response.parse()
            assert_matches_type(SerpCreateResponse, serp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeysso) -> None:
        serp = await async_client.serp.list()
        assert_matches_type(SerpListResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeysso) -> None:
        serp = await async_client.serp.list(
            is_main=True,
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(SerpListResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeysso) -> None:
        response = await async_client.serp.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        serp = await response.parse()
        assert_matches_type(SerpListResponse, serp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeysso) -> None:
        async with async_client.serp.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            serp = await response.parse()
            assert_matches_type(SerpListResponse, serp, path=["response"])

        assert cast(Any, response.is_closed) is True
