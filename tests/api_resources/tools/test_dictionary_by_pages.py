# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.tools import DictionaryByPageCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDictionaryByPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Keysso) -> None:
        dictionary_by_page = client.tools.dictionary_by_pages.create(
            pages=["dodopizza.ru/VerkhnyayaPyshma/bonusactions", "dodopizza.ru/bonusactionsz"],
        )
        assert_matches_type(DictionaryByPageCreateResponse, dictionary_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Keysso) -> None:
        dictionary_by_page = client.tools.dictionary_by_pages.create(
            pages=["dodopizza.ru/VerkhnyayaPyshma/bonusactions", "dodopizza.ru/bonusactionsz"],
            base="msk",
            config={"more": True},
        )
        assert_matches_type(DictionaryByPageCreateResponse, dictionary_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Keysso) -> None:
        response = client.tools.dictionary_by_pages.with_raw_response.create(
            pages=["dodopizza.ru/VerkhnyayaPyshma/bonusactions", "dodopizza.ru/bonusactionsz"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dictionary_by_page = response.parse()
        assert_matches_type(DictionaryByPageCreateResponse, dictionary_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Keysso) -> None:
        with client.tools.dictionary_by_pages.with_streaming_response.create(
            pages=["dodopizza.ru/VerkhnyayaPyshma/bonusactions", "dodopizza.ru/bonusactionsz"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dictionary_by_page = response.parse()
            assert_matches_type(DictionaryByPageCreateResponse, dictionary_by_page, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDictionaryByPages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeysso) -> None:
        dictionary_by_page = await async_client.tools.dictionary_by_pages.create(
            pages=["dodopizza.ru/VerkhnyayaPyshma/bonusactions", "dodopizza.ru/bonusactionsz"],
        )
        assert_matches_type(DictionaryByPageCreateResponse, dictionary_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeysso) -> None:
        dictionary_by_page = await async_client.tools.dictionary_by_pages.create(
            pages=["dodopizza.ru/VerkhnyayaPyshma/bonusactions", "dodopizza.ru/bonusactionsz"],
            base="msk",
            config={"more": True},
        )
        assert_matches_type(DictionaryByPageCreateResponse, dictionary_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.dictionary_by_pages.with_raw_response.create(
            pages=["dodopizza.ru/VerkhnyayaPyshma/bonusactions", "dodopizza.ru/bonusactionsz"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dictionary_by_page = await response.parse()
        assert_matches_type(DictionaryByPageCreateResponse, dictionary_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.dictionary_by_pages.with_streaming_response.create(
            pages=["dodopizza.ru/VerkhnyayaPyshma/bonusactions", "dodopizza.ru/bonusactionsz"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dictionary_by_page = await response.parse()
            assert_matches_type(DictionaryByPageCreateResponse, dictionary_by_page, path=["response"])

        assert cast(Any, response.is_closed) is True
