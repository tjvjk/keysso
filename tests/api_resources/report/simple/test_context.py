# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.report.simple import ContextRetrieveConcurentsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContext:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_concurents(self, client: Keysso) -> None:
        context = client.report.simple.context.retrieve_concurents(
            domain="domain",
        )
        assert_matches_type(ContextRetrieveConcurentsResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_concurents_with_all_params(self, client: Keysso) -> None:
        context = client.report.simple.context.retrieve_concurents(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(ContextRetrieveConcurentsResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_concurents(self, client: Keysso) -> None:
        response = client.report.simple.context.with_raw_response.retrieve_concurents(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(ContextRetrieveConcurentsResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_concurents(self, client: Keysso) -> None:
        with client.report.simple.context.with_streaming_response.retrieve_concurents(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(ContextRetrieveConcurentsResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContext:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_concurents(self, async_client: AsyncKeysso) -> None:
        context = await async_client.report.simple.context.retrieve_concurents(
            domain="domain",
        )
        assert_matches_type(ContextRetrieveConcurentsResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_concurents_with_all_params(self, async_client: AsyncKeysso) -> None:
        context = await async_client.report.simple.context.retrieve_concurents(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(ContextRetrieveConcurentsResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_concurents(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.context.with_raw_response.retrieve_concurents(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(ContextRetrieveConcurentsResponse, context, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_concurents(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.context.with_streaming_response.retrieve_concurents(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(ContextRetrieveConcurentsResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True
