# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.tools import KeywordsByListCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeywordsByList:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Keysso) -> None:
        keywords_by_list = client.tools.keywords_by_list.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        )
        assert_matches_type(KeywordsByListCreateResponse, keywords_by_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Keysso) -> None:
        keywords_by_list = client.tools.keywords_by_list.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
            base="msk",
        )
        assert_matches_type(KeywordsByListCreateResponse, keywords_by_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Keysso) -> None:
        response = client.tools.keywords_by_list.with_raw_response.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keywords_by_list = response.parse()
        assert_matches_type(KeywordsByListCreateResponse, keywords_by_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Keysso) -> None:
        with client.tools.keywords_by_list.with_streaming_response.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keywords_by_list = response.parse()
            assert_matches_type(KeywordsByListCreateResponse, keywords_by_list, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKeywordsByList:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeysso) -> None:
        keywords_by_list = await async_client.tools.keywords_by_list.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        )
        assert_matches_type(KeywordsByListCreateResponse, keywords_by_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeysso) -> None:
        keywords_by_list = await async_client.tools.keywords_by_list.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
            base="msk",
        )
        assert_matches_type(KeywordsByListCreateResponse, keywords_by_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.keywords_by_list.with_raw_response.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keywords_by_list = await response.parse()
        assert_matches_type(KeywordsByListCreateResponse, keywords_by_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.keywords_by_list.with_streaming_response.create(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keywords_by_list = await response.parse()
            assert_matches_type(KeywordsByListCreateResponse, keywords_by_list, path=["response"])

        assert cast(Any, response.is_closed) is True
