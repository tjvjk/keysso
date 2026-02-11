# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.report.simple.links import (
    BacklinksIPRetrieveSubnetResponse,
    BacklinksIPRetrieveBacklinksIPResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBacklinksIP:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_backlinks_ip(self, client: Keysso) -> None:
        backlinks_ip = client.report.simple.links.backlinks_ip.retrieve_backlinks_ip(
            domain="domain",
        )
        assert_matches_type(BacklinksIPRetrieveBacklinksIPResponse, backlinks_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_backlinks_ip_with_all_params(self, client: Keysso) -> None:
        backlinks_ip = client.report.simple.links.backlinks_ip.retrieve_backlinks_ip(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(BacklinksIPRetrieveBacklinksIPResponse, backlinks_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_backlinks_ip(self, client: Keysso) -> None:
        response = client.report.simple.links.backlinks_ip.with_raw_response.retrieve_backlinks_ip(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backlinks_ip = response.parse()
        assert_matches_type(BacklinksIPRetrieveBacklinksIPResponse, backlinks_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_backlinks_ip(self, client: Keysso) -> None:
        with client.report.simple.links.backlinks_ip.with_streaming_response.retrieve_backlinks_ip(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backlinks_ip = response.parse()
            assert_matches_type(BacklinksIPRetrieveBacklinksIPResponse, backlinks_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_subnet(self, client: Keysso) -> None:
        backlinks_ip = client.report.simple.links.backlinks_ip.retrieve_subnet(
            domain="domain",
        )
        assert_matches_type(BacklinksIPRetrieveSubnetResponse, backlinks_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_subnet_with_all_params(self, client: Keysso) -> None:
        backlinks_ip = client.report.simple.links.backlinks_ip.retrieve_subnet(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(BacklinksIPRetrieveSubnetResponse, backlinks_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_subnet(self, client: Keysso) -> None:
        response = client.report.simple.links.backlinks_ip.with_raw_response.retrieve_subnet(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backlinks_ip = response.parse()
        assert_matches_type(BacklinksIPRetrieveSubnetResponse, backlinks_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_subnet(self, client: Keysso) -> None:
        with client.report.simple.links.backlinks_ip.with_streaming_response.retrieve_subnet(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backlinks_ip = response.parse()
            assert_matches_type(BacklinksIPRetrieveSubnetResponse, backlinks_ip, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBacklinksIP:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_backlinks_ip(self, async_client: AsyncKeysso) -> None:
        backlinks_ip = await async_client.report.simple.links.backlinks_ip.retrieve_backlinks_ip(
            domain="domain",
        )
        assert_matches_type(BacklinksIPRetrieveBacklinksIPResponse, backlinks_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_backlinks_ip_with_all_params(self, async_client: AsyncKeysso) -> None:
        backlinks_ip = await async_client.report.simple.links.backlinks_ip.retrieve_backlinks_ip(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(BacklinksIPRetrieveBacklinksIPResponse, backlinks_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_backlinks_ip(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.links.backlinks_ip.with_raw_response.retrieve_backlinks_ip(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backlinks_ip = await response.parse()
        assert_matches_type(BacklinksIPRetrieveBacklinksIPResponse, backlinks_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_backlinks_ip(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.links.backlinks_ip.with_streaming_response.retrieve_backlinks_ip(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backlinks_ip = await response.parse()
            assert_matches_type(BacklinksIPRetrieveBacklinksIPResponse, backlinks_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_subnet(self, async_client: AsyncKeysso) -> None:
        backlinks_ip = await async_client.report.simple.links.backlinks_ip.retrieve_subnet(
            domain="domain",
        )
        assert_matches_type(BacklinksIPRetrieveSubnetResponse, backlinks_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_subnet_with_all_params(self, async_client: AsyncKeysso) -> None:
        backlinks_ip = await async_client.report.simple.links.backlinks_ip.retrieve_subnet(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(BacklinksIPRetrieveSubnetResponse, backlinks_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_subnet(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.links.backlinks_ip.with_raw_response.retrieve_subnet(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backlinks_ip = await response.parse()
        assert_matches_type(BacklinksIPRetrieveSubnetResponse, backlinks_ip, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_subnet(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.links.backlinks_ip.with_streaming_response.retrieve_subnet(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backlinks_ip = await response.parse()
            assert_matches_type(BacklinksIPRetrieveSubnetResponse, backlinks_ip, path=["response"])

        assert cast(Any, response.is_closed) is True
