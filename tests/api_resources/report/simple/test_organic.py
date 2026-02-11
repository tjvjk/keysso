# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.report.simple import (
    OrganicRetrieveAIAnswersResponse,
    OrganicRetrieveLostPagesResponse,
    OrganicRetrieveConcurentsResponse,
    OrganicRetrieveLostKeywordsResponse,
    OrganicRetrieveConcurentPagesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganic:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_ai_answers(self, client: Keysso) -> None:
        organic = client.report.simple.organic.retrieve_ai_answers(
            domain="domain",
        )
        assert_matches_type(OrganicRetrieveAIAnswersResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_ai_answers_with_all_params(self, client: Keysso) -> None:
        organic = client.report.simple.organic.retrieve_ai_answers(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(OrganicRetrieveAIAnswersResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_ai_answers(self, client: Keysso) -> None:
        response = client.report.simple.organic.with_raw_response.retrieve_ai_answers(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organic = response.parse()
        assert_matches_type(OrganicRetrieveAIAnswersResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_ai_answers(self, client: Keysso) -> None:
        with client.report.simple.organic.with_streaming_response.retrieve_ai_answers(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organic = response.parse()
            assert_matches_type(OrganicRetrieveAIAnswersResponse, organic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_concurent_pages(self, client: Keysso) -> None:
        organic = client.report.simple.organic.retrieve_concurent_pages(
            domain="domain",
            page_url="page_url",
        )
        assert_matches_type(OrganicRetrieveConcurentPagesResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_concurent_pages_with_all_params(self, client: Keysso) -> None:
        organic = client.report.simple.organic.retrieve_concurent_pages(
            domain="domain",
            page_url="page_url",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(OrganicRetrieveConcurentPagesResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_concurent_pages(self, client: Keysso) -> None:
        response = client.report.simple.organic.with_raw_response.retrieve_concurent_pages(
            domain="domain",
            page_url="page_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organic = response.parse()
        assert_matches_type(OrganicRetrieveConcurentPagesResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_concurent_pages(self, client: Keysso) -> None:
        with client.report.simple.organic.with_streaming_response.retrieve_concurent_pages(
            domain="domain",
            page_url="page_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organic = response.parse()
            assert_matches_type(OrganicRetrieveConcurentPagesResponse, organic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_concurents(self, client: Keysso) -> None:
        organic = client.report.simple.organic.retrieve_concurents(
            domain="domain",
        )
        assert_matches_type(OrganicRetrieveConcurentsResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_concurents_with_all_params(self, client: Keysso) -> None:
        organic = client.report.simple.organic.retrieve_concurents(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
            top=10,
        )
        assert_matches_type(OrganicRetrieveConcurentsResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_concurents(self, client: Keysso) -> None:
        response = client.report.simple.organic.with_raw_response.retrieve_concurents(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organic = response.parse()
        assert_matches_type(OrganicRetrieveConcurentsResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_concurents(self, client: Keysso) -> None:
        with client.report.simple.organic.with_streaming_response.retrieve_concurents(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organic = response.parse()
            assert_matches_type(OrganicRetrieveConcurentsResponse, organic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_lost_keywords(self, client: Keysso) -> None:
        organic = client.report.simple.organic.retrieve_lost_keywords(
            domain="domain",
        )
        assert_matches_type(OrganicRetrieveLostKeywordsResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_lost_keywords_with_all_params(self, client: Keysso) -> None:
        organic = client.report.simple.organic.retrieve_lost_keywords(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(OrganicRetrieveLostKeywordsResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_lost_keywords(self, client: Keysso) -> None:
        response = client.report.simple.organic.with_raw_response.retrieve_lost_keywords(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organic = response.parse()
        assert_matches_type(OrganicRetrieveLostKeywordsResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_lost_keywords(self, client: Keysso) -> None:
        with client.report.simple.organic.with_streaming_response.retrieve_lost_keywords(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organic = response.parse()
            assert_matches_type(OrganicRetrieveLostKeywordsResponse, organic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_lost_pages(self, client: Keysso) -> None:
        organic = client.report.simple.organic.retrieve_lost_pages(
            domain="domain",
        )
        assert_matches_type(OrganicRetrieveLostPagesResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_lost_pages_with_all_params(self, client: Keysso) -> None:
        organic = client.report.simple.organic.retrieve_lost_pages(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(OrganicRetrieveLostPagesResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_lost_pages(self, client: Keysso) -> None:
        response = client.report.simple.organic.with_raw_response.retrieve_lost_pages(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organic = response.parse()
        assert_matches_type(OrganicRetrieveLostPagesResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_lost_pages(self, client: Keysso) -> None:
        with client.report.simple.organic.with_streaming_response.retrieve_lost_pages(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organic = response.parse()
            assert_matches_type(OrganicRetrieveLostPagesResponse, organic, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganic:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_ai_answers(self, async_client: AsyncKeysso) -> None:
        organic = await async_client.report.simple.organic.retrieve_ai_answers(
            domain="domain",
        )
        assert_matches_type(OrganicRetrieveAIAnswersResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_ai_answers_with_all_params(self, async_client: AsyncKeysso) -> None:
        organic = await async_client.report.simple.organic.retrieve_ai_answers(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(OrganicRetrieveAIAnswersResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_ai_answers(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.organic.with_raw_response.retrieve_ai_answers(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organic = await response.parse()
        assert_matches_type(OrganicRetrieveAIAnswersResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_ai_answers(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.organic.with_streaming_response.retrieve_ai_answers(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organic = await response.parse()
            assert_matches_type(OrganicRetrieveAIAnswersResponse, organic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_concurent_pages(self, async_client: AsyncKeysso) -> None:
        organic = await async_client.report.simple.organic.retrieve_concurent_pages(
            domain="domain",
            page_url="page_url",
        )
        assert_matches_type(OrganicRetrieveConcurentPagesResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_concurent_pages_with_all_params(self, async_client: AsyncKeysso) -> None:
        organic = await async_client.report.simple.organic.retrieve_concurent_pages(
            domain="domain",
            page_url="page_url",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(OrganicRetrieveConcurentPagesResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_concurent_pages(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.organic.with_raw_response.retrieve_concurent_pages(
            domain="domain",
            page_url="page_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organic = await response.parse()
        assert_matches_type(OrganicRetrieveConcurentPagesResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_concurent_pages(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.organic.with_streaming_response.retrieve_concurent_pages(
            domain="domain",
            page_url="page_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organic = await response.parse()
            assert_matches_type(OrganicRetrieveConcurentPagesResponse, organic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_concurents(self, async_client: AsyncKeysso) -> None:
        organic = await async_client.report.simple.organic.retrieve_concurents(
            domain="domain",
        )
        assert_matches_type(OrganicRetrieveConcurentsResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_concurents_with_all_params(self, async_client: AsyncKeysso) -> None:
        organic = await async_client.report.simple.organic.retrieve_concurents(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
            top=10,
        )
        assert_matches_type(OrganicRetrieveConcurentsResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_concurents(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.organic.with_raw_response.retrieve_concurents(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organic = await response.parse()
        assert_matches_type(OrganicRetrieveConcurentsResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_concurents(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.organic.with_streaming_response.retrieve_concurents(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organic = await response.parse()
            assert_matches_type(OrganicRetrieveConcurentsResponse, organic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_lost_keywords(self, async_client: AsyncKeysso) -> None:
        organic = await async_client.report.simple.organic.retrieve_lost_keywords(
            domain="domain",
        )
        assert_matches_type(OrganicRetrieveLostKeywordsResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_lost_keywords_with_all_params(self, async_client: AsyncKeysso) -> None:
        organic = await async_client.report.simple.organic.retrieve_lost_keywords(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(OrganicRetrieveLostKeywordsResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_lost_keywords(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.organic.with_raw_response.retrieve_lost_keywords(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organic = await response.parse()
        assert_matches_type(OrganicRetrieveLostKeywordsResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_lost_keywords(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.organic.with_streaming_response.retrieve_lost_keywords(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organic = await response.parse()
            assert_matches_type(OrganicRetrieveLostKeywordsResponse, organic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_lost_pages(self, async_client: AsyncKeysso) -> None:
        organic = await async_client.report.simple.organic.retrieve_lost_pages(
            domain="domain",
        )
        assert_matches_type(OrganicRetrieveLostPagesResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_lost_pages_with_all_params(self, async_client: AsyncKeysso) -> None:
        organic = await async_client.report.simple.organic.retrieve_lost_pages(
            domain="domain",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(OrganicRetrieveLostPagesResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_lost_pages(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.organic.with_raw_response.retrieve_lost_pages(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organic = await response.parse()
        assert_matches_type(OrganicRetrieveLostPagesResponse, organic, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_lost_pages(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.organic.with_streaming_response.retrieve_lost_pages(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organic = await response.parse()
            assert_matches_type(OrganicRetrieveLostPagesResponse, organic, path=["response"])

        assert cast(Any, response.is_closed) is True
