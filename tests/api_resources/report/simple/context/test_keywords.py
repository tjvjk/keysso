# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.report.simple.context import (
    KeywordListResponse,
    KeywordRetrieveByadsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeywords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Keysso) -> None:
        keyword = client.report.simple.context.keywords.list(
            domain="domain",
        )
        assert_matches_type(KeywordListResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Keysso) -> None:
        keyword = client.report.simple.context.keywords.list(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(KeywordListResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Keysso) -> None:
        response = client.report.simple.context.keywords.with_raw_response.list(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = response.parse()
        assert_matches_type(KeywordListResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Keysso) -> None:
        with client.report.simple.context.keywords.with_streaming_response.list(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = response.parse()
            assert_matches_type(KeywordListResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_byads(self, client: Keysso) -> None:
        keyword = client.report.simple.context.keywords.retrieve_byads(
            ads_id="ads_id",
            domain="domain",
        )
        assert_matches_type(KeywordRetrieveByadsResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_byads_with_all_params(self, client: Keysso) -> None:
        keyword = client.report.simple.context.keywords.retrieve_byads(
            ads_id="ads_id",
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(KeywordRetrieveByadsResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_byads(self, client: Keysso) -> None:
        response = client.report.simple.context.keywords.with_raw_response.retrieve_byads(
            ads_id="ads_id",
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = response.parse()
        assert_matches_type(KeywordRetrieveByadsResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_byads(self, client: Keysso) -> None:
        with client.report.simple.context.keywords.with_streaming_response.retrieve_byads(
            ads_id="ads_id",
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = response.parse()
            assert_matches_type(KeywordRetrieveByadsResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKeywords:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeysso) -> None:
        keyword = await async_client.report.simple.context.keywords.list(
            domain="domain",
        )
        assert_matches_type(KeywordListResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeysso) -> None:
        keyword = await async_client.report.simple.context.keywords.list(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(KeywordListResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.context.keywords.with_raw_response.list(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = await response.parse()
        assert_matches_type(KeywordListResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.context.keywords.with_streaming_response.list(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = await response.parse()
            assert_matches_type(KeywordListResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_byads(self, async_client: AsyncKeysso) -> None:
        keyword = await async_client.report.simple.context.keywords.retrieve_byads(
            ads_id="ads_id",
            domain="domain",
        )
        assert_matches_type(KeywordRetrieveByadsResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_byads_with_all_params(self, async_client: AsyncKeysso) -> None:
        keyword = await async_client.report.simple.context.keywords.retrieve_byads(
            ads_id="ads_id",
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(KeywordRetrieveByadsResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_byads(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.context.keywords.with_raw_response.retrieve_byads(
            ads_id="ads_id",
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = await response.parse()
        assert_matches_type(KeywordRetrieveByadsResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_byads(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.context.keywords.with_streaming_response.retrieve_byads(
            ads_id="ads_id",
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = await response.parse()
            assert_matches_type(KeywordRetrieveByadsResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True
