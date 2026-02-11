# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.report.simple.organic import (
    SitepageListResponse,
    SitepageRetrieveWithkeysResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSitepages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Keysso) -> None:
        sitepage = client.report.simple.organic.sitepages.list(
            domain="domain",
        )
        assert_matches_type(SitepageListResponse, sitepage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Keysso) -> None:
        sitepage = client.report.simple.organic.sitepages.list(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(SitepageListResponse, sitepage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Keysso) -> None:
        response = client.report.simple.organic.sitepages.with_raw_response.list(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitepage = response.parse()
        assert_matches_type(SitepageListResponse, sitepage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Keysso) -> None:
        with client.report.simple.organic.sitepages.with_streaming_response.list(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitepage = response.parse()
            assert_matches_type(SitepageListResponse, sitepage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_withkeys(self, client: Keysso) -> None:
        sitepage = client.report.simple.organic.sitepages.retrieve_withkeys(
            domain="domain",
        )
        assert_matches_type(SitepageRetrieveWithkeysResponse, sitepage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_withkeys_with_all_params(self, client: Keysso) -> None:
        sitepage = client.report.simple.organic.sitepages.retrieve_withkeys(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(SitepageRetrieveWithkeysResponse, sitepage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_withkeys(self, client: Keysso) -> None:
        response = client.report.simple.organic.sitepages.with_raw_response.retrieve_withkeys(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitepage = response.parse()
        assert_matches_type(SitepageRetrieveWithkeysResponse, sitepage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_withkeys(self, client: Keysso) -> None:
        with client.report.simple.organic.sitepages.with_streaming_response.retrieve_withkeys(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitepage = response.parse()
            assert_matches_type(SitepageRetrieveWithkeysResponse, sitepage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSitepages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeysso) -> None:
        sitepage = await async_client.report.simple.organic.sitepages.list(
            domain="domain",
        )
        assert_matches_type(SitepageListResponse, sitepage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeysso) -> None:
        sitepage = await async_client.report.simple.organic.sitepages.list(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(SitepageListResponse, sitepage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.organic.sitepages.with_raw_response.list(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitepage = await response.parse()
        assert_matches_type(SitepageListResponse, sitepage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.organic.sitepages.with_streaming_response.list(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitepage = await response.parse()
            assert_matches_type(SitepageListResponse, sitepage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_withkeys(self, async_client: AsyncKeysso) -> None:
        sitepage = await async_client.report.simple.organic.sitepages.retrieve_withkeys(
            domain="domain",
        )
        assert_matches_type(SitepageRetrieveWithkeysResponse, sitepage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_withkeys_with_all_params(self, async_client: AsyncKeysso) -> None:
        sitepage = await async_client.report.simple.organic.sitepages.retrieve_withkeys(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(SitepageRetrieveWithkeysResponse, sitepage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_withkeys(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.organic.sitepages.with_raw_response.retrieve_withkeys(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitepage = await response.parse()
        assert_matches_type(SitepageRetrieveWithkeysResponse, sitepage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_withkeys(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.organic.sitepages.with_streaming_response.retrieve_withkeys(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitepage = await response.parse()
            assert_matches_type(SitepageRetrieveWithkeysResponse, sitepage, path=["response"])

        assert cast(Any, response.is_closed) is True
