# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.report.simple import (
    DirectRetrieveAdsResponse,
    DirectRetrieveDomainResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDirect:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_ads(self, client: Keysso) -> None:
        direct = client.report.simple.direct.retrieve_ads(
            kid=0,
        )
        assert_matches_type(DirectRetrieveAdsResponse, direct, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_ads_with_all_params(self, client: Keysso) -> None:
        direct = client.report.simple.direct.retrieve_ads(
            kid=0,
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(DirectRetrieveAdsResponse, direct, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_ads(self, client: Keysso) -> None:
        response = client.report.simple.direct.with_raw_response.retrieve_ads(
            kid=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        direct = response.parse()
        assert_matches_type(DirectRetrieveAdsResponse, direct, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_ads(self, client: Keysso) -> None:
        with client.report.simple.direct.with_streaming_response.retrieve_ads(
            kid=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            direct = response.parse()
            assert_matches_type(DirectRetrieveAdsResponse, direct, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_domain(self, client: Keysso) -> None:
        direct = client.report.simple.direct.retrieve_domain(
            domain="domain",
        )
        assert_matches_type(DirectRetrieveDomainResponse, direct, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_domain_with_all_params(self, client: Keysso) -> None:
        direct = client.report.simple.direct.retrieve_domain(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(DirectRetrieveDomainResponse, direct, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_domain(self, client: Keysso) -> None:
        response = client.report.simple.direct.with_raw_response.retrieve_domain(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        direct = response.parse()
        assert_matches_type(DirectRetrieveDomainResponse, direct, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_domain(self, client: Keysso) -> None:
        with client.report.simple.direct.with_streaming_response.retrieve_domain(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            direct = response.parse()
            assert_matches_type(DirectRetrieveDomainResponse, direct, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDirect:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_ads(self, async_client: AsyncKeysso) -> None:
        direct = await async_client.report.simple.direct.retrieve_ads(
            kid=0,
        )
        assert_matches_type(DirectRetrieveAdsResponse, direct, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_ads_with_all_params(self, async_client: AsyncKeysso) -> None:
        direct = await async_client.report.simple.direct.retrieve_ads(
            kid=0,
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(DirectRetrieveAdsResponse, direct, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_ads(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.direct.with_raw_response.retrieve_ads(
            kid=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        direct = await response.parse()
        assert_matches_type(DirectRetrieveAdsResponse, direct, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_ads(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.direct.with_streaming_response.retrieve_ads(
            kid=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            direct = await response.parse()
            assert_matches_type(DirectRetrieveAdsResponse, direct, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_domain(self, async_client: AsyncKeysso) -> None:
        direct = await async_client.report.simple.direct.retrieve_domain(
            domain="domain",
        )
        assert_matches_type(DirectRetrieveDomainResponse, direct, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_domain_with_all_params(self, async_client: AsyncKeysso) -> None:
        direct = await async_client.report.simple.direct.retrieve_domain(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(DirectRetrieveDomainResponse, direct, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_domain(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.direct.with_raw_response.retrieve_domain(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        direct = await response.parse()
        assert_matches_type(DirectRetrieveDomainResponse, direct, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_domain(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.direct.with_streaming_response.retrieve_domain(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            direct = await response.parse()
            assert_matches_type(DirectRetrieveDomainResponse, direct, path=["response"])

        assert cast(Any, response.is_closed) is True
