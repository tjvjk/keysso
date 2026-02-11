# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.report.simple import (
    LinkDomainsBatchResponse,
    LinkRetrievePagesResponse,
    LinkRetrieveOutlinksResponse,
    LinkRetrieveBacklinksResponse,
    LinkRetrieveBacklinksAnchorResponse,
    LinkRetrieveOutlinksDomainsResponse,
    LinkRetrieveBacklinksDomainsResponse,
    LinkRetrieveOutlinksDomainsViewDomainResponse,
    LinkRetrieveBacklinksDomainsViewDomainResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_domains_batch(self, client: Keysso) -> None:
        link = client.report.simple.links.domains_batch(
            data={"domains": "domains"},
        )
        assert_matches_type(LinkDomainsBatchResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_domains_batch_with_all_params(self, client: Keysso) -> None:
        link = client.report.simple.links.domains_batch(
            data={"domains": "domains"},
            base="msk",
            params={
                "filter": "filter",
                "page": 0,
                "per_page": 0,
                "sort": "sort",
            },
        )
        assert_matches_type(LinkDomainsBatchResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_domains_batch(self, client: Keysso) -> None:
        response = client.report.simple.links.with_raw_response.domains_batch(
            data={"domains": "domains"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkDomainsBatchResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_domains_batch(self, client: Keysso) -> None:
        with client.report.simple.links.with_streaming_response.domains_batch(
            data={"domains": "domains"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkDomainsBatchResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_backlinks(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_backlinks(
            domain="domain",
        )
        assert_matches_type(LinkRetrieveBacklinksResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_backlinks_with_all_params(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_backlinks(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveBacklinksResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_backlinks(self, client: Keysso) -> None:
        response = client.report.simple.links.with_raw_response.retrieve_backlinks(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkRetrieveBacklinksResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_backlinks(self, client: Keysso) -> None:
        with client.report.simple.links.with_streaming_response.retrieve_backlinks(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkRetrieveBacklinksResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_backlinks_anchor(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_backlinks_anchor(
            domain="domain",
        )
        assert_matches_type(LinkRetrieveBacklinksAnchorResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_backlinks_anchor_with_all_params(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_backlinks_anchor(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveBacklinksAnchorResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_backlinks_anchor(self, client: Keysso) -> None:
        response = client.report.simple.links.with_raw_response.retrieve_backlinks_anchor(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkRetrieveBacklinksAnchorResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_backlinks_anchor(self, client: Keysso) -> None:
        with client.report.simple.links.with_streaming_response.retrieve_backlinks_anchor(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkRetrieveBacklinksAnchorResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_backlinks_domains(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_backlinks_domains(
            domain="domain",
        )
        assert_matches_type(LinkRetrieveBacklinksDomainsResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_backlinks_domains_with_all_params(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_backlinks_domains(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveBacklinksDomainsResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_backlinks_domains(self, client: Keysso) -> None:
        response = client.report.simple.links.with_raw_response.retrieve_backlinks_domains(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkRetrieveBacklinksDomainsResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_backlinks_domains(self, client: Keysso) -> None:
        with client.report.simple.links.with_streaming_response.retrieve_backlinks_domains(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkRetrieveBacklinksDomainsResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_backlinks_domains_view_domain(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_backlinks_domains_view_domain(
            domain="domain",
            view="domain",
        )
        assert_matches_type(LinkRetrieveBacklinksDomainsViewDomainResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_backlinks_domains_view_domain_with_all_params(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_backlinks_domains_view_domain(
            domain="domain",
            view="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveBacklinksDomainsViewDomainResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_backlinks_domains_view_domain(self, client: Keysso) -> None:
        response = client.report.simple.links.with_raw_response.retrieve_backlinks_domains_view_domain(
            domain="domain",
            view="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkRetrieveBacklinksDomainsViewDomainResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_backlinks_domains_view_domain(self, client: Keysso) -> None:
        with client.report.simple.links.with_streaming_response.retrieve_backlinks_domains_view_domain(
            domain="domain",
            view="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkRetrieveBacklinksDomainsViewDomainResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_outlinks(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_outlinks(
            domain="domain",
        )
        assert_matches_type(LinkRetrieveOutlinksResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_outlinks_with_all_params(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_outlinks(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveOutlinksResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_outlinks(self, client: Keysso) -> None:
        response = client.report.simple.links.with_raw_response.retrieve_outlinks(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkRetrieveOutlinksResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_outlinks(self, client: Keysso) -> None:
        with client.report.simple.links.with_streaming_response.retrieve_outlinks(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkRetrieveOutlinksResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_outlinks_domains(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_outlinks_domains(
            domain="domain",
        )
        assert_matches_type(LinkRetrieveOutlinksDomainsResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_outlinks_domains_with_all_params(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_outlinks_domains(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveOutlinksDomainsResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_outlinks_domains(self, client: Keysso) -> None:
        response = client.report.simple.links.with_raw_response.retrieve_outlinks_domains(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkRetrieveOutlinksDomainsResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_outlinks_domains(self, client: Keysso) -> None:
        with client.report.simple.links.with_streaming_response.retrieve_outlinks_domains(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkRetrieveOutlinksDomainsResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_outlinks_domains_view_domain(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_outlinks_domains_view_domain(
            domain="domain",
            view="domain",
        )
        assert_matches_type(LinkRetrieveOutlinksDomainsViewDomainResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_outlinks_domains_view_domain_with_all_params(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_outlinks_domains_view_domain(
            domain="domain",
            view="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveOutlinksDomainsViewDomainResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_outlinks_domains_view_domain(self, client: Keysso) -> None:
        response = client.report.simple.links.with_raw_response.retrieve_outlinks_domains_view_domain(
            domain="domain",
            view="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkRetrieveOutlinksDomainsViewDomainResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_outlinks_domains_view_domain(self, client: Keysso) -> None:
        with client.report.simple.links.with_streaming_response.retrieve_outlinks_domains_view_domain(
            domain="domain",
            view="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkRetrieveOutlinksDomainsViewDomainResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_pages(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_pages(
            domain="domain",
        )
        assert_matches_type(LinkRetrievePagesResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_pages_with_all_params(self, client: Keysso) -> None:
        link = client.report.simple.links.retrieve_pages(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrievePagesResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_pages(self, client: Keysso) -> None:
        response = client.report.simple.links.with_raw_response.retrieve_pages(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkRetrievePagesResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_pages(self, client: Keysso) -> None:
        with client.report.simple.links.with_streaming_response.retrieve_pages(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkRetrievePagesResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_domains_batch(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.domains_batch(
            data={"domains": "domains"},
        )
        assert_matches_type(LinkDomainsBatchResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_domains_batch_with_all_params(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.domains_batch(
            data={"domains": "domains"},
            base="msk",
            params={
                "filter": "filter",
                "page": 0,
                "per_page": 0,
                "sort": "sort",
            },
        )
        assert_matches_type(LinkDomainsBatchResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_domains_batch(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.links.with_raw_response.domains_batch(
            data={"domains": "domains"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkDomainsBatchResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_domains_batch(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.links.with_streaming_response.domains_batch(
            data={"domains": "domains"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkDomainsBatchResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_backlinks(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_backlinks(
            domain="domain",
        )
        assert_matches_type(LinkRetrieveBacklinksResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_backlinks_with_all_params(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_backlinks(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveBacklinksResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_backlinks(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.links.with_raw_response.retrieve_backlinks(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkRetrieveBacklinksResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_backlinks(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.links.with_streaming_response.retrieve_backlinks(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkRetrieveBacklinksResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_backlinks_anchor(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_backlinks_anchor(
            domain="domain",
        )
        assert_matches_type(LinkRetrieveBacklinksAnchorResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_backlinks_anchor_with_all_params(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_backlinks_anchor(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveBacklinksAnchorResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_backlinks_anchor(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.links.with_raw_response.retrieve_backlinks_anchor(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkRetrieveBacklinksAnchorResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_backlinks_anchor(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.links.with_streaming_response.retrieve_backlinks_anchor(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkRetrieveBacklinksAnchorResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_backlinks_domains(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_backlinks_domains(
            domain="domain",
        )
        assert_matches_type(LinkRetrieveBacklinksDomainsResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_backlinks_domains_with_all_params(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_backlinks_domains(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveBacklinksDomainsResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_backlinks_domains(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.links.with_raw_response.retrieve_backlinks_domains(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkRetrieveBacklinksDomainsResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_backlinks_domains(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.links.with_streaming_response.retrieve_backlinks_domains(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkRetrieveBacklinksDomainsResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_backlinks_domains_view_domain(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_backlinks_domains_view_domain(
            domain="domain",
            view="domain",
        )
        assert_matches_type(LinkRetrieveBacklinksDomainsViewDomainResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_backlinks_domains_view_domain_with_all_params(
        self, async_client: AsyncKeysso
    ) -> None:
        link = await async_client.report.simple.links.retrieve_backlinks_domains_view_domain(
            domain="domain",
            view="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveBacklinksDomainsViewDomainResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_backlinks_domains_view_domain(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.links.with_raw_response.retrieve_backlinks_domains_view_domain(
            domain="domain",
            view="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkRetrieveBacklinksDomainsViewDomainResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_backlinks_domains_view_domain(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.links.with_streaming_response.retrieve_backlinks_domains_view_domain(
            domain="domain",
            view="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkRetrieveBacklinksDomainsViewDomainResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_outlinks(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_outlinks(
            domain="domain",
        )
        assert_matches_type(LinkRetrieveOutlinksResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_outlinks_with_all_params(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_outlinks(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveOutlinksResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_outlinks(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.links.with_raw_response.retrieve_outlinks(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkRetrieveOutlinksResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_outlinks(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.links.with_streaming_response.retrieve_outlinks(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkRetrieveOutlinksResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_outlinks_domains(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_outlinks_domains(
            domain="domain",
        )
        assert_matches_type(LinkRetrieveOutlinksDomainsResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_outlinks_domains_with_all_params(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_outlinks_domains(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveOutlinksDomainsResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_outlinks_domains(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.links.with_raw_response.retrieve_outlinks_domains(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkRetrieveOutlinksDomainsResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_outlinks_domains(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.links.with_streaming_response.retrieve_outlinks_domains(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkRetrieveOutlinksDomainsResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_outlinks_domains_view_domain(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_outlinks_domains_view_domain(
            domain="domain",
            view="domain",
        )
        assert_matches_type(LinkRetrieveOutlinksDomainsViewDomainResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_outlinks_domains_view_domain_with_all_params(
        self, async_client: AsyncKeysso
    ) -> None:
        link = await async_client.report.simple.links.retrieve_outlinks_domains_view_domain(
            domain="domain",
            view="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrieveOutlinksDomainsViewDomainResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_outlinks_domains_view_domain(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.links.with_raw_response.retrieve_outlinks_domains_view_domain(
            domain="domain",
            view="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkRetrieveOutlinksDomainsViewDomainResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_outlinks_domains_view_domain(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.links.with_streaming_response.retrieve_outlinks_domains_view_domain(
            domain="domain",
            view="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkRetrieveOutlinksDomainsViewDomainResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_pages(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_pages(
            domain="domain",
        )
        assert_matches_type(LinkRetrievePagesResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_pages_with_all_params(self, async_client: AsyncKeysso) -> None:
        link = await async_client.report.simple.links.retrieve_pages(
            domain="domain",
            filter="filter",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(LinkRetrievePagesResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_pages(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.links.with_raw_response.retrieve_pages(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkRetrievePagesResponse, link, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_pages(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.links.with_streaming_response.retrieve_pages(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkRetrievePagesResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True
