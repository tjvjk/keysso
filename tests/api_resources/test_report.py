# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types import (
    ReportCompareContextResponse,
    ReportCompareOrganicResponse,
    ReportCompareBacklinksResponse,
    ReportCreateSystemKeywordsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare_backlinks(self, client: Keysso) -> None:
        report = client.report.compare_backlinks(
            excl="excl",
            incl="incl",
        )
        assert_matches_type(ReportCompareBacklinksResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare_backlinks_with_all_params(self, client: Keysso) -> None:
        report = client.report.compare_backlinks(
            excl="excl",
            incl="incl",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
            view="organic",
        )
        assert_matches_type(ReportCompareBacklinksResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_compare_backlinks(self, client: Keysso) -> None:
        response = client.report.with_raw_response.compare_backlinks(
            excl="excl",
            incl="incl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportCompareBacklinksResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_compare_backlinks(self, client: Keysso) -> None:
        with client.report.with_streaming_response.compare_backlinks(
            excl="excl",
            incl="incl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportCompareBacklinksResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare_context(self, client: Keysso) -> None:
        report = client.report.compare_context(
            excl="excl",
            incl="incl",
        )
        assert_matches_type(ReportCompareContextResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare_context_with_all_params(self, client: Keysso) -> None:
        report = client.report.compare_context(
            excl="excl",
            incl="incl",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
            view="organic",
        )
        assert_matches_type(ReportCompareContextResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_compare_context(self, client: Keysso) -> None:
        response = client.report.with_raw_response.compare_context(
            excl="excl",
            incl="incl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportCompareContextResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_compare_context(self, client: Keysso) -> None:
        with client.report.with_streaming_response.compare_context(
            excl="excl",
            incl="incl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportCompareContextResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare_organic(self, client: Keysso) -> None:
        report = client.report.compare_organic(
            excl="excl",
            incl="incl",
        )
        assert_matches_type(ReportCompareOrganicResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare_organic_with_all_params(self, client: Keysso) -> None:
        report = client.report.compare_organic(
            excl="excl",
            incl="incl",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
            view="organic",
        )
        assert_matches_type(ReportCompareOrganicResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_compare_organic(self, client: Keysso) -> None:
        response = client.report.with_raw_response.compare_organic(
            excl="excl",
            incl="incl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportCompareOrganicResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_compare_organic(self, client: Keysso) -> None:
        with client.report.with_streaming_response.compare_organic(
            excl="excl",
            incl="incl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportCompareOrganicResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_system_keywords(self, client: Keysso) -> None:
        report = client.report.create_system_keywords(
            hideadult=True,
            strict=True,
        )
        assert_matches_type(ReportCreateSystemKeywordsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_system_keywords_with_all_params(self, client: Keysso) -> None:
        report = client.report.create_system_keywords(
            hideadult=True,
            strict=True,
            page=0,
            sort="sort",
            params={
                "filter": "filter",
                "page": 0,
                "per_page": 0,
                "sort": "sort",
            },
        )
        assert_matches_type(ReportCreateSystemKeywordsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_system_keywords(self, client: Keysso) -> None:
        response = client.report.with_raw_response.create_system_keywords(
            hideadult=True,
            strict=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportCreateSystemKeywordsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_system_keywords(self, client: Keysso) -> None:
        with client.report.with_streaming_response.create_system_keywords(
            hideadult=True,
            strict=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportCreateSystemKeywordsResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare_backlinks(self, async_client: AsyncKeysso) -> None:
        report = await async_client.report.compare_backlinks(
            excl="excl",
            incl="incl",
        )
        assert_matches_type(ReportCompareBacklinksResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare_backlinks_with_all_params(self, async_client: AsyncKeysso) -> None:
        report = await async_client.report.compare_backlinks(
            excl="excl",
            incl="incl",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
            view="organic",
        )
        assert_matches_type(ReportCompareBacklinksResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_compare_backlinks(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.with_raw_response.compare_backlinks(
            excl="excl",
            incl="incl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportCompareBacklinksResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_compare_backlinks(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.with_streaming_response.compare_backlinks(
            excl="excl",
            incl="incl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportCompareBacklinksResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare_context(self, async_client: AsyncKeysso) -> None:
        report = await async_client.report.compare_context(
            excl="excl",
            incl="incl",
        )
        assert_matches_type(ReportCompareContextResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare_context_with_all_params(self, async_client: AsyncKeysso) -> None:
        report = await async_client.report.compare_context(
            excl="excl",
            incl="incl",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
            view="organic",
        )
        assert_matches_type(ReportCompareContextResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_compare_context(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.with_raw_response.compare_context(
            excl="excl",
            incl="incl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportCompareContextResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_compare_context(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.with_streaming_response.compare_context(
            excl="excl",
            incl="incl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportCompareContextResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare_organic(self, async_client: AsyncKeysso) -> None:
        report = await async_client.report.compare_organic(
            excl="excl",
            incl="incl",
        )
        assert_matches_type(ReportCompareOrganicResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare_organic_with_all_params(self, async_client: AsyncKeysso) -> None:
        report = await async_client.report.compare_organic(
            excl="excl",
            incl="incl",
            base="msk",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
            view="organic",
        )
        assert_matches_type(ReportCompareOrganicResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_compare_organic(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.with_raw_response.compare_organic(
            excl="excl",
            incl="incl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportCompareOrganicResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_compare_organic(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.with_streaming_response.compare_organic(
            excl="excl",
            incl="incl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportCompareOrganicResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_system_keywords(self, async_client: AsyncKeysso) -> None:
        report = await async_client.report.create_system_keywords(
            hideadult=True,
            strict=True,
        )
        assert_matches_type(ReportCreateSystemKeywordsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_system_keywords_with_all_params(self, async_client: AsyncKeysso) -> None:
        report = await async_client.report.create_system_keywords(
            hideadult=True,
            strict=True,
            page=0,
            sort="sort",
            params={
                "filter": "filter",
                "page": 0,
                "per_page": 0,
                "sort": "sort",
            },
        )
        assert_matches_type(ReportCreateSystemKeywordsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_system_keywords(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.with_raw_response.create_system_keywords(
            hideadult=True,
            strict=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportCreateSystemKeywordsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_system_keywords(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.with_streaming_response.create_system_keywords(
            hideadult=True,
            strict=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportCreateSystemKeywordsResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True
