# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.tools import DictionaryExtByPageCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDictionaryExtByPage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Keysso) -> None:
        dictionary_ext_by_page = client.tools.dictionary_ext_by_page.create(
            config={},
            url="dodopizza.ru/VerkhnyayaPyshma/bonusactions",
        )
        assert_matches_type(DictionaryExtByPageCreateResponse, dictionary_ext_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Keysso) -> None:
        dictionary_ext_by_page = client.tools.dictionary_ext_by_page.create(
            config={
                "list": ["фраза"],
                "more": True,
                "pages": ["example.ru/top"],
                "use_list": True,
                "use_pages": True,
            },
            url="dodopizza.ru/VerkhnyayaPyshma/bonusactions",
            base="msk",
        )
        assert_matches_type(DictionaryExtByPageCreateResponse, dictionary_ext_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Keysso) -> None:
        response = client.tools.dictionary_ext_by_page.with_raw_response.create(
            config={},
            url="dodopizza.ru/VerkhnyayaPyshma/bonusactions",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dictionary_ext_by_page = response.parse()
        assert_matches_type(DictionaryExtByPageCreateResponse, dictionary_ext_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Keysso) -> None:
        with client.tools.dictionary_ext_by_page.with_streaming_response.create(
            config={},
            url="dodopizza.ru/VerkhnyayaPyshma/bonusactions",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dictionary_ext_by_page = response.parse()
            assert_matches_type(DictionaryExtByPageCreateResponse, dictionary_ext_by_page, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDictionaryExtByPage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeysso) -> None:
        dictionary_ext_by_page = await async_client.tools.dictionary_ext_by_page.create(
            config={},
            url="dodopizza.ru/VerkhnyayaPyshma/bonusactions",
        )
        assert_matches_type(DictionaryExtByPageCreateResponse, dictionary_ext_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeysso) -> None:
        dictionary_ext_by_page = await async_client.tools.dictionary_ext_by_page.create(
            config={
                "list": ["фраза"],
                "more": True,
                "pages": ["example.ru/top"],
                "use_list": True,
                "use_pages": True,
            },
            url="dodopizza.ru/VerkhnyayaPyshma/bonusactions",
            base="msk",
        )
        assert_matches_type(DictionaryExtByPageCreateResponse, dictionary_ext_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.dictionary_ext_by_page.with_raw_response.create(
            config={},
            url="dodopizza.ru/VerkhnyayaPyshma/bonusactions",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dictionary_ext_by_page = await response.parse()
        assert_matches_type(DictionaryExtByPageCreateResponse, dictionary_ext_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.dictionary_ext_by_page.with_streaming_response.create(
            config={},
            url="dodopizza.ru/VerkhnyayaPyshma/bonusactions",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dictionary_ext_by_page = await response.parse()
            assert_matches_type(DictionaryExtByPageCreateResponse, dictionary_ext_by_page, path=["response"])

        assert cast(Any, response.is_closed) is True
