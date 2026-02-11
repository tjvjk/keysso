# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.report import (
    SimpleRetrieveSimilarkeysResponse,
    SimpleRetrieveDomainAdHistoryResponse,
    SimpleRetrieveDomainDashboardResponse,
    SimpleRetrieveKeywordDashboardResponse,
    SimpleRetrieveTopDomainVisibilityResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimple:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_domain_ad_history(self, client: Keysso) -> None:
        simple = client.report.simple.retrieve_domain_ad_history(
            domain="domain",
        )
        assert_matches_type(SimpleRetrieveDomainAdHistoryResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_domain_ad_history_with_all_params(self, client: Keysso) -> None:
        simple = client.report.simple.retrieve_domain_ad_history(
            domain="domain",
            base="msk",
        )
        assert_matches_type(SimpleRetrieveDomainAdHistoryResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_domain_ad_history(self, client: Keysso) -> None:
        response = client.report.simple.with_raw_response.retrieve_domain_ad_history(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = response.parse()
        assert_matches_type(SimpleRetrieveDomainAdHistoryResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_domain_ad_history(self, client: Keysso) -> None:
        with client.report.simple.with_streaming_response.retrieve_domain_ad_history(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = response.parse()
            assert_matches_type(SimpleRetrieveDomainAdHistoryResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_domain_dashboard(self, client: Keysso) -> None:
        simple = client.report.simple.retrieve_domain_dashboard(
            domain="domain",
        )
        assert_matches_type(SimpleRetrieveDomainDashboardResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_domain_dashboard_with_all_params(self, client: Keysso) -> None:
        simple = client.report.simple.retrieve_domain_dashboard(
            domain="domain",
            base="msk",
        )
        assert_matches_type(SimpleRetrieveDomainDashboardResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_domain_dashboard(self, client: Keysso) -> None:
        response = client.report.simple.with_raw_response.retrieve_domain_dashboard(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = response.parse()
        assert_matches_type(SimpleRetrieveDomainDashboardResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_domain_dashboard(self, client: Keysso) -> None:
        with client.report.simple.with_streaming_response.retrieve_domain_dashboard(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = response.parse()
            assert_matches_type(SimpleRetrieveDomainDashboardResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_keyword_dashboard(self, client: Keysso) -> None:
        simple = client.report.simple.retrieve_keyword_dashboard(
            keyword="keyword",
        )
        assert_matches_type(SimpleRetrieveKeywordDashboardResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_keyword_dashboard_with_all_params(self, client: Keysso) -> None:
        simple = client.report.simple.retrieve_keyword_dashboard(
            keyword="keyword",
            base="msk",
        )
        assert_matches_type(SimpleRetrieveKeywordDashboardResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_keyword_dashboard(self, client: Keysso) -> None:
        response = client.report.simple.with_raw_response.retrieve_keyword_dashboard(
            keyword="keyword",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = response.parse()
        assert_matches_type(SimpleRetrieveKeywordDashboardResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_keyword_dashboard(self, client: Keysso) -> None:
        with client.report.simple.with_streaming_response.retrieve_keyword_dashboard(
            keyword="keyword",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = response.parse()
            assert_matches_type(SimpleRetrieveKeywordDashboardResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_similarkeys(self, client: Keysso) -> None:
        simple = client.report.simple.retrieve_similarkeys(
            keyword="keyword",
        )
        assert_matches_type(SimpleRetrieveSimilarkeysResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_similarkeys_with_all_params(self, client: Keysso) -> None:
        simple = client.report.simple.retrieve_similarkeys(
            keyword="keyword",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(SimpleRetrieveSimilarkeysResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_similarkeys(self, client: Keysso) -> None:
        response = client.report.simple.with_raw_response.retrieve_similarkeys(
            keyword="keyword",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = response.parse()
        assert_matches_type(SimpleRetrieveSimilarkeysResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_similarkeys(self, client: Keysso) -> None:
        with client.report.simple.with_streaming_response.retrieve_similarkeys(
            keyword="keyword",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = response.parse()
            assert_matches_type(SimpleRetrieveSimilarkeysResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_top_domain_visibility(self, client: Keysso) -> None:
        simple = client.report.simple.retrieve_top_domain_visibility(
            domain="domain",
        )
        assert_matches_type(SimpleRetrieveTopDomainVisibilityResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_top_domain_visibility_with_all_params(self, client: Keysso) -> None:
        simple = client.report.simple.retrieve_top_domain_visibility(
            domain="domain",
            base="msk",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(SimpleRetrieveTopDomainVisibilityResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_top_domain_visibility(self, client: Keysso) -> None:
        response = client.report.simple.with_raw_response.retrieve_top_domain_visibility(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = response.parse()
        assert_matches_type(SimpleRetrieveTopDomainVisibilityResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_top_domain_visibility(self, client: Keysso) -> None:
        with client.report.simple.with_streaming_response.retrieve_top_domain_visibility(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = response.parse()
            assert_matches_type(SimpleRetrieveTopDomainVisibilityResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSimple:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_domain_ad_history(self, async_client: AsyncKeysso) -> None:
        simple = await async_client.report.simple.retrieve_domain_ad_history(
            domain="domain",
        )
        assert_matches_type(SimpleRetrieveDomainAdHistoryResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_domain_ad_history_with_all_params(self, async_client: AsyncKeysso) -> None:
        simple = await async_client.report.simple.retrieve_domain_ad_history(
            domain="domain",
            base="msk",
        )
        assert_matches_type(SimpleRetrieveDomainAdHistoryResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_domain_ad_history(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.with_raw_response.retrieve_domain_ad_history(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = await response.parse()
        assert_matches_type(SimpleRetrieveDomainAdHistoryResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_domain_ad_history(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.with_streaming_response.retrieve_domain_ad_history(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = await response.parse()
            assert_matches_type(SimpleRetrieveDomainAdHistoryResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_domain_dashboard(self, async_client: AsyncKeysso) -> None:
        simple = await async_client.report.simple.retrieve_domain_dashboard(
            domain="domain",
        )
        assert_matches_type(SimpleRetrieveDomainDashboardResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_domain_dashboard_with_all_params(self, async_client: AsyncKeysso) -> None:
        simple = await async_client.report.simple.retrieve_domain_dashboard(
            domain="domain",
            base="msk",
        )
        assert_matches_type(SimpleRetrieveDomainDashboardResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_domain_dashboard(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.with_raw_response.retrieve_domain_dashboard(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = await response.parse()
        assert_matches_type(SimpleRetrieveDomainDashboardResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_domain_dashboard(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.with_streaming_response.retrieve_domain_dashboard(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = await response.parse()
            assert_matches_type(SimpleRetrieveDomainDashboardResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_keyword_dashboard(self, async_client: AsyncKeysso) -> None:
        simple = await async_client.report.simple.retrieve_keyword_dashboard(
            keyword="keyword",
        )
        assert_matches_type(SimpleRetrieveKeywordDashboardResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_keyword_dashboard_with_all_params(self, async_client: AsyncKeysso) -> None:
        simple = await async_client.report.simple.retrieve_keyword_dashboard(
            keyword="keyword",
            base="msk",
        )
        assert_matches_type(SimpleRetrieveKeywordDashboardResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_keyword_dashboard(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.with_raw_response.retrieve_keyword_dashboard(
            keyword="keyword",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = await response.parse()
        assert_matches_type(SimpleRetrieveKeywordDashboardResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_keyword_dashboard(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.with_streaming_response.retrieve_keyword_dashboard(
            keyword="keyword",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = await response.parse()
            assert_matches_type(SimpleRetrieveKeywordDashboardResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_similarkeys(self, async_client: AsyncKeysso) -> None:
        simple = await async_client.report.simple.retrieve_similarkeys(
            keyword="keyword",
        )
        assert_matches_type(SimpleRetrieveSimilarkeysResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_similarkeys_with_all_params(self, async_client: AsyncKeysso) -> None:
        simple = await async_client.report.simple.retrieve_similarkeys(
            keyword="keyword",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(SimpleRetrieveSimilarkeysResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_similarkeys(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.with_raw_response.retrieve_similarkeys(
            keyword="keyword",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = await response.parse()
        assert_matches_type(SimpleRetrieveSimilarkeysResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_similarkeys(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.with_streaming_response.retrieve_similarkeys(
            keyword="keyword",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = await response.parse()
            assert_matches_type(SimpleRetrieveSimilarkeysResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_top_domain_visibility(self, async_client: AsyncKeysso) -> None:
        simple = await async_client.report.simple.retrieve_top_domain_visibility(
            domain="domain",
        )
        assert_matches_type(SimpleRetrieveTopDomainVisibilityResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_top_domain_visibility_with_all_params(self, async_client: AsyncKeysso) -> None:
        simple = await async_client.report.simple.retrieve_top_domain_visibility(
            domain="domain",
            base="msk",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(SimpleRetrieveTopDomainVisibilityResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_top_domain_visibility(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.with_raw_response.retrieve_top_domain_visibility(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = await response.parse()
        assert_matches_type(SimpleRetrieveTopDomainVisibilityResponse, simple, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_top_domain_visibility(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.with_streaming_response.retrieve_top_domain_visibility(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = await response.parse()
            assert_matches_type(SimpleRetrieveTopDomainVisibilityResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True
