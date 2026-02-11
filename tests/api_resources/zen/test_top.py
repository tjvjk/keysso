# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.zen import TopListChannelsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_channels(self, client: Keysso) -> None:
        top = client.zen.top.list_channels()
        assert_matches_type(TopListChannelsResponse, top, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_channels_with_all_params(self, client: Keysso) -> None:
        top = client.zen.top.list_channels(
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(TopListChannelsResponse, top, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_channels(self, client: Keysso) -> None:
        response = client.zen.top.with_raw_response.list_channels()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopListChannelsResponse, top, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_channels(self, client: Keysso) -> None:
        with client.zen.top.with_streaming_response.list_channels() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopListChannelsResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTop:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_channels(self, async_client: AsyncKeysso) -> None:
        top = await async_client.zen.top.list_channels()
        assert_matches_type(TopListChannelsResponse, top, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_channels_with_all_params(self, async_client: AsyncKeysso) -> None:
        top = await async_client.zen.top.list_channels(
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(TopListChannelsResponse, top, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_channels(self, async_client: AsyncKeysso) -> None:
        response = await async_client.zen.top.with_raw_response.list_channels()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopListChannelsResponse, top, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_channels(self, async_client: AsyncKeysso) -> None:
        async with async_client.zen.top.with_streaming_response.list_channels() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopListChannelsResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True
