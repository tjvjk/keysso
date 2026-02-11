# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types import (
    ToolCompareResponse,
    ToolSuggestResponse,
    ToolCheckTopResponse,
    ToolCreateUniqueResponse,
    ToolDeleteDoubleResponse,
    ToolListSiteThemesResponse,
    ToolCreateHistorySerpResponse,
    ToolCreateDomainsBatchResponse,
    ToolCheckTopConcurentsURLsResponse,
    ToolCheckTopConcurentsDomainsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_top(self, client: Keysso) -> None:
        tool = client.tools.check_top(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )
        assert_matches_type(ToolCheckTopResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_top_with_all_params(self, client: Keysso) -> None:
        tool = client.tools.check_top(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            base="msk",
        )
        assert_matches_type(ToolCheckTopResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check_top(self, client: Keysso) -> None:
        response = client.tools.with_raw_response.check_top(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolCheckTopResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check_top(self, client: Keysso) -> None:
        with client.tools.with_streaming_response.check_top(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolCheckTopResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_top_concurents_domains(self, client: Keysso) -> None:
        tool = client.tools.check_top_concurents_domains(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )
        assert_matches_type(ToolCheckTopConcurentsDomainsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_top_concurents_domains_with_all_params(self, client: Keysso) -> None:
        tool = client.tools.check_top_concurents_domains(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            base="msk",
            page=1,
            per_page=25,
        )
        assert_matches_type(ToolCheckTopConcurentsDomainsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check_top_concurents_domains(self, client: Keysso) -> None:
        response = client.tools.with_raw_response.check_top_concurents_domains(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolCheckTopConcurentsDomainsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check_top_concurents_domains(self, client: Keysso) -> None:
        with client.tools.with_streaming_response.check_top_concurents_domains(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolCheckTopConcurentsDomainsResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_top_concurents_urls(self, client: Keysso) -> None:
        tool = client.tools.check_top_concurents_urls(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )
        assert_matches_type(ToolCheckTopConcurentsURLsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_top_concurents_urls_with_all_params(self, client: Keysso) -> None:
        tool = client.tools.check_top_concurents_urls(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            base="msk",
            page=1,
            per_page=25,
        )
        assert_matches_type(ToolCheckTopConcurentsURLsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check_top_concurents_urls(self, client: Keysso) -> None:
        response = client.tools.with_raw_response.check_top_concurents_urls(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolCheckTopConcurentsURLsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check_top_concurents_urls(self, client: Keysso) -> None:
        with client.tools.with_streaming_response.check_top_concurents_urls(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolCheckTopConcurentsURLsResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_combine(self, client: Keysso) -> None:
        tool = client.tools.combine(
            lists=[[{}]],
        )
        assert_matches_type(str, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_combine_with_all_params(self, client: Keysso) -> None:
        tool = client.tools.combine(
            lists=[[{}]],
            options=["quotes", "brackets", "simple", "stop_word"],
        )
        assert_matches_type(str, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_combine(self, client: Keysso) -> None:
        response = client.tools.with_raw_response.combine(
            lists=[[{}]],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(str, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_combine(self, client: Keysso) -> None:
        with client.tools.with_streaming_response.combine(
            lists=[[{}]],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(str, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compare(self, client: Keysso) -> None:
        tool = client.tools.compare(
            left=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            options="present_right",
            right=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )
        assert_matches_type(ToolCompareResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_compare(self, client: Keysso) -> None:
        response = client.tools.with_raw_response.compare(
            left=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            options="present_right",
            right=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolCompareResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_compare(self, client: Keysso) -> None:
        with client.tools.with_streaming_response.compare(
            left=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            options="present_right",
            right=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolCompareResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_domains_batch(self, client: Keysso) -> None:
        tool = client.tools.create_domains_batch(
            data={"domains": "domains"},
        )
        assert_matches_type(ToolCreateDomainsBatchResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_domains_batch_with_all_params(self, client: Keysso) -> None:
        tool = client.tools.create_domains_batch(
            data={"domains": "domains"},
            base="msk",
            params={
                "filter": "filter",
                "page": 0,
                "per_page": 0,
                "sort": "sort",
            },
        )
        assert_matches_type(ToolCreateDomainsBatchResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_domains_batch(self, client: Keysso) -> None:
        response = client.tools.with_raw_response.create_domains_batch(
            data={"domains": "domains"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolCreateDomainsBatchResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_domains_batch(self, client: Keysso) -> None:
        with client.tools.with_streaming_response.create_domains_batch(
            data={"domains": "domains"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolCreateDomainsBatchResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_history_serp(self, client: Keysso) -> None:
        tool = client.tools.create_history_serp(
            keyword="купить телефон",
        )
        assert_matches_type(ToolCreateHistorySerpResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_history_serp_with_all_params(self, client: Keysso) -> None:
        tool = client.tools.create_history_serp(
            keyword="купить телефон",
            base="msk",
        )
        assert_matches_type(ToolCreateHistorySerpResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_history_serp(self, client: Keysso) -> None:
        response = client.tools.with_raw_response.create_history_serp(
            keyword="купить телефон",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolCreateHistorySerpResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_history_serp(self, client: Keysso) -> None:
        with client.tools.with_streaming_response.create_history_serp(
            keyword="купить телефон",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolCreateHistorySerpResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_unique(self, client: Keysso) -> None:
        tool = client.tools.create_unique(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )
        assert_matches_type(ToolCreateUniqueResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_unique(self, client: Keysso) -> None:
        response = client.tools.with_raw_response.create_unique(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolCreateUniqueResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_unique(self, client: Keysso) -> None:
        with client.tools.with_streaming_response.create_unique(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolCreateUniqueResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_double(self, client: Keysso) -> None:
        tool = client.tools.delete_double(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        )
        assert_matches_type(ToolDeleteDoubleResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_double(self, client: Keysso) -> None:
        response = client.tools.with_raw_response.delete_double(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolDeleteDoubleResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_double(self, client: Keysso) -> None:
        with client.tools.with_streaming_response.delete_double(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolDeleteDoubleResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_site_themes(self, client: Keysso) -> None:
        tool = client.tools.list_site_themes(
            site="site",
        )
        assert_matches_type(ToolListSiteThemesResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_site_themes_with_all_params(self, client: Keysso) -> None:
        tool = client.tools.list_site_themes(
            site="site",
            base="msk",
            filter="filter",
            like="like",
            max_pos=0,
            max_ws=0,
            max_wsk=0,
            min_pos=0,
            min_ws=0,
            min_wsk=0,
            not_like="notLike",
            page=0,
            per_page=0,
            qby_url=0,
            sort="sort",
            words="words",
        )
        assert_matches_type(ToolListSiteThemesResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_site_themes(self, client: Keysso) -> None:
        response = client.tools.with_raw_response.list_site_themes(
            site="site",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListSiteThemesResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_site_themes(self, client: Keysso) -> None:
        with client.tools.with_streaming_response.list_site_themes(
            site="site",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListSiteThemesResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_suggest(self, client: Keysso) -> None:
        tool = client.tools.suggest(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            region=1,
        )
        assert_matches_type(ToolSuggestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_suggest(self, client: Keysso) -> None:
        response = client.tools.with_raw_response.suggest(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            region=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolSuggestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_suggest(self, client: Keysso) -> None:
        with client.tools.with_streaming_response.suggest(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            region=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolSuggestResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_top(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.check_top(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )
        assert_matches_type(ToolCheckTopResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_top_with_all_params(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.check_top(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            base="msk",
        )
        assert_matches_type(ToolCheckTopResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check_top(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.with_raw_response.check_top(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolCheckTopResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check_top(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.with_streaming_response.check_top(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolCheckTopResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_top_concurents_domains(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.check_top_concurents_domains(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )
        assert_matches_type(ToolCheckTopConcurentsDomainsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_top_concurents_domains_with_all_params(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.check_top_concurents_domains(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            base="msk",
            page=1,
            per_page=25,
        )
        assert_matches_type(ToolCheckTopConcurentsDomainsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check_top_concurents_domains(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.with_raw_response.check_top_concurents_domains(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolCheckTopConcurentsDomainsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check_top_concurents_domains(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.with_streaming_response.check_top_concurents_domains(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolCheckTopConcurentsDomainsResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_top_concurents_urls(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.check_top_concurents_urls(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )
        assert_matches_type(ToolCheckTopConcurentsURLsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_top_concurents_urls_with_all_params(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.check_top_concurents_urls(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            base="msk",
            page=1,
            per_page=25,
        )
        assert_matches_type(ToolCheckTopConcurentsURLsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check_top_concurents_urls(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.with_raw_response.check_top_concurents_urls(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolCheckTopConcurentsURLsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check_top_concurents_urls(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.with_streaming_response.check_top_concurents_urls(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolCheckTopConcurentsURLsResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_combine(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.combine(
            lists=[[{}]],
        )
        assert_matches_type(str, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_combine_with_all_params(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.combine(
            lists=[[{}]],
            options=["quotes", "brackets", "simple", "stop_word"],
        )
        assert_matches_type(str, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_combine(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.with_raw_response.combine(
            lists=[[{}]],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(str, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_combine(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.with_streaming_response.combine(
            lists=[[{}]],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(str, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compare(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.compare(
            left=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            options="present_right",
            right=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )
        assert_matches_type(ToolCompareResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_compare(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.with_raw_response.compare(
            left=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            options="present_right",
            right=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolCompareResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_compare(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.with_streaming_response.compare(
            left=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            options="present_right",
            right=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolCompareResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_domains_batch(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.create_domains_batch(
            data={"domains": "domains"},
        )
        assert_matches_type(ToolCreateDomainsBatchResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_domains_batch_with_all_params(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.create_domains_batch(
            data={"domains": "domains"},
            base="msk",
            params={
                "filter": "filter",
                "page": 0,
                "per_page": 0,
                "sort": "sort",
            },
        )
        assert_matches_type(ToolCreateDomainsBatchResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_domains_batch(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.with_raw_response.create_domains_batch(
            data={"domains": "domains"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolCreateDomainsBatchResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_domains_batch(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.with_streaming_response.create_domains_batch(
            data={"domains": "domains"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolCreateDomainsBatchResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_history_serp(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.create_history_serp(
            keyword="купить телефон",
        )
        assert_matches_type(ToolCreateHistorySerpResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_history_serp_with_all_params(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.create_history_serp(
            keyword="купить телефон",
            base="msk",
        )
        assert_matches_type(ToolCreateHistorySerpResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_history_serp(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.with_raw_response.create_history_serp(
            keyword="купить телефон",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolCreateHistorySerpResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_history_serp(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.with_streaming_response.create_history_serp(
            keyword="купить телефон",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolCreateHistorySerpResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_unique(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.create_unique(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )
        assert_matches_type(ToolCreateUniqueResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_unique(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.with_raw_response.create_unique(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolCreateUniqueResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_unique(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.with_streaming_response.create_unique(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolCreateUniqueResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_double(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.delete_double(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        )
        assert_matches_type(ToolDeleteDoubleResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_double(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.with_raw_response.delete_double(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolDeleteDoubleResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_double(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.with_streaming_response.delete_double(
            list=["одежда для беременных", "для беременных одежда", "одежда"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolDeleteDoubleResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_site_themes(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.list_site_themes(
            site="site",
        )
        assert_matches_type(ToolListSiteThemesResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_site_themes_with_all_params(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.list_site_themes(
            site="site",
            base="msk",
            filter="filter",
            like="like",
            max_pos=0,
            max_ws=0,
            max_wsk=0,
            min_pos=0,
            min_ws=0,
            min_wsk=0,
            not_like="notLike",
            page=0,
            per_page=0,
            qby_url=0,
            sort="sort",
            words="words",
        )
        assert_matches_type(ToolListSiteThemesResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_site_themes(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.with_raw_response.list_site_themes(
            site="site",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListSiteThemesResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_site_themes(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.with_streaming_response.list_site_themes(
            site="site",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListSiteThemesResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_suggest(self, async_client: AsyncKeysso) -> None:
        tool = await async_client.tools.suggest(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            region=1,
        )
        assert_matches_type(ToolSuggestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_suggest(self, async_client: AsyncKeysso) -> None:
        response = await async_client.tools.with_raw_response.suggest(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            region=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolSuggestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_suggest(self, async_client: AsyncKeysso) -> None:
        async with async_client.tools.with_streaming_response.suggest(
            list=["справка от фтизиатра онлайн", "заключение от фтизиатра", "запись на прием к врачу"],
            region=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolSuggestResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
