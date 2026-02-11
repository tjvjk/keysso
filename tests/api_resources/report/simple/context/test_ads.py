# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.report.simple.context import (
    AdRetrieveResponse,
    AdRetrieveFactsResponse,
    AdRetrieveLinksResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Keysso) -> None:
        ad = client.report.simple.context.ads.retrieve(
            domain="domain",
        )
        assert_matches_type(AdRetrieveResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Keysso) -> None:
        ad = client.report.simple.context.ads.retrieve(
            domain="domain",
            base="msk",
            filter="filter",
            full=True,
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(AdRetrieveResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Keysso) -> None:
        response = client.report.simple.context.ads.with_raw_response.retrieve(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdRetrieveResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Keysso) -> None:
        with client.report.simple.context.ads.with_streaming_response.retrieve(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdRetrieveResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_facts(self, client: Keysso) -> None:
        ad = client.report.simple.context.ads.retrieve_facts(
            domain="domain",
        )
        assert_matches_type(AdRetrieveFactsResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_facts_with_all_params(self, client: Keysso) -> None:
        ad = client.report.simple.context.ads.retrieve_facts(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(AdRetrieveFactsResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_facts(self, client: Keysso) -> None:
        response = client.report.simple.context.ads.with_raw_response.retrieve_facts(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdRetrieveFactsResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_facts(self, client: Keysso) -> None:
        with client.report.simple.context.ads.with_streaming_response.retrieve_facts(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdRetrieveFactsResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_links(self, client: Keysso) -> None:
        ad = client.report.simple.context.ads.retrieve_links(
            domain="domain",
        )
        assert_matches_type(AdRetrieveLinksResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_links_with_all_params(self, client: Keysso) -> None:
        ad = client.report.simple.context.ads.retrieve_links(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(AdRetrieveLinksResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_links(self, client: Keysso) -> None:
        response = client.report.simple.context.ads.with_raw_response.retrieve_links(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdRetrieveLinksResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_links(self, client: Keysso) -> None:
        with client.report.simple.context.ads.with_streaming_response.retrieve_links(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdRetrieveLinksResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKeysso) -> None:
        ad = await async_client.report.simple.context.ads.retrieve(
            domain="domain",
        )
        assert_matches_type(AdRetrieveResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncKeysso) -> None:
        ad = await async_client.report.simple.context.ads.retrieve(
            domain="domain",
            base="msk",
            filter="filter",
            full=True,
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(AdRetrieveResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.context.ads.with_raw_response.retrieve(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdRetrieveResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.context.ads.with_streaming_response.retrieve(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdRetrieveResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_facts(self, async_client: AsyncKeysso) -> None:
        ad = await async_client.report.simple.context.ads.retrieve_facts(
            domain="domain",
        )
        assert_matches_type(AdRetrieveFactsResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_facts_with_all_params(self, async_client: AsyncKeysso) -> None:
        ad = await async_client.report.simple.context.ads.retrieve_facts(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(AdRetrieveFactsResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_facts(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.context.ads.with_raw_response.retrieve_facts(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdRetrieveFactsResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_facts(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.context.ads.with_streaming_response.retrieve_facts(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdRetrieveFactsResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_links(self, async_client: AsyncKeysso) -> None:
        ad = await async_client.report.simple.context.ads.retrieve_links(
            domain="domain",
        )
        assert_matches_type(AdRetrieveLinksResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_links_with_all_params(self, async_client: AsyncKeysso) -> None:
        ad = await async_client.report.simple.context.ads.retrieve_links(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(AdRetrieveLinksResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_links(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.context.ads.with_raw_response.retrieve_links(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdRetrieveLinksResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_links(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.context.ads.with_streaming_response.retrieve_links(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdRetrieveLinksResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True
