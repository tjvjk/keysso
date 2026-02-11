# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.tools import KeywordsByPageCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeywordsByPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Keysso) -> None:
        keywords_by_page = client.tools.keywords_by_pages.create(
            list=[
                "dodopizza.ru/VerkhnyayaPyshma/bonusactions",
                "dodopizza.ru/moscow/product/pepperoni-tomat",
                "dodopizza.ru/verkhnyayapyshma/verkhnyayapyshma",
            ],
        )
        assert_matches_type(KeywordsByPageCreateResponse, keywords_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Keysso) -> None:
        keywords_by_page = client.tools.keywords_by_pages.create(
            list=[
                "dodopizza.ru/VerkhnyayaPyshma/bonusactions",
                "dodopizza.ru/moscow/product/pepperoni-tomat",
                "dodopizza.ru/verkhnyayapyshma/verkhnyayapyshma",
            ],
            base="msk",
            top=10,
        )
        assert_matches_type(KeywordsByPageCreateResponse, keywords_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Keysso) -> None:
        response = client.tools.keywords_by_pages.with_raw_response.create(
            list=[
                "dodopizza.ru/VerkhnyayaPyshma/bonusactions",
                "dodopizza.ru/moscow/product/pepperoni-tomat",
                "dodopizza.ru/verkhnyayapyshma/verkhnyayapyshma",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keywords_by_page = response.parse()
        assert_matches_type(KeywordsByPageCreateResponse, keywords_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Keysso) -> None:
        with client.tools.keywords_by_pages.with_streaming_response.create(
            list=[
                "dodopizza.ru/VerkhnyayaPyshma/bonusactions",
                "dodopizza.ru/moscow/product/pepperoni-tomat",
                "dodopizza.ru/verkhnyayapyshma/verkhnyayapyshma",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keywords_by_page = response.parse()
            assert_matches_type(KeywordsByPageCreateResponse, keywords_by_page, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKeywordsByPages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeysso) -> None:
        keywords_by_page = await async_client.tools.keywords_by_pages.create(
            list=[
                "dodopizza.ru/VerkhnyayaPyshma/bonusactions",
                "dodopizza.ru/moscow/product/pepperoni-tomat",
                "dodopizza.ru/verkhnyayapyshma/verkhnyayapyshma",
            ],
        )
        assert_matches_type(KeywordsByPageCreateResponse, keywords_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeysso) -> None:
        keywords_by_page = await async_client.tools.keywords_by_pages.create(
            list=[
                "dodopizza.ru/VerkhnyayaPyshma/bonusactions",
                "dodopizza.ru/moscow/product/pepperoni-tomat",
                "dodopizza.ru/verkhnyayapyshma/verkhnyayapyshma",
            ],
            base="msk",
            top=10,
        )
        assert_matches_type(KeywordsByPageCreateResponse, keywords_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.keywords_by_pages.with_raw_response.create(
            list=[
                "dodopizza.ru/VerkhnyayaPyshma/bonusactions",
                "dodopizza.ru/moscow/product/pepperoni-tomat",
                "dodopizza.ru/verkhnyayapyshma/verkhnyayapyshma",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keywords_by_page = await response.parse()
        assert_matches_type(KeywordsByPageCreateResponse, keywords_by_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.keywords_by_pages.with_streaming_response.create(
            list=[
                "dodopizza.ru/VerkhnyayaPyshma/bonusactions",
                "dodopizza.ru/moscow/product/pepperoni-tomat",
                "dodopizza.ru/verkhnyayapyshma/verkhnyayapyshma",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keywords_by_page = await response.parse()
            assert_matches_type(KeywordsByPageCreateResponse, keywords_by_page, path=["response"])

        assert cast(Any, response.is_closed) is True
