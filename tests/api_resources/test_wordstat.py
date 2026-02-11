# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types import (
    WordstatListResponse,
    WordstatReportResponse,
    WordstatDeleteWordsResponse,
    WordstatCreateProjectResponse,
    WordstatDeleteProjectResponse,
    WordstatGetProjectStatusResponse,
    WordstatGetProjectsCompletedResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWordstat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Keysso) -> None:
        wordstat = client.wordstat.list()
        assert_matches_type(WordstatListResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Keysso) -> None:
        wordstat = client.wordstat.list(
            is_main=True,
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(WordstatListResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Keysso) -> None:
        response = client.wordstat.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = response.parse()
        assert_matches_type(WordstatListResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Keysso) -> None:
        with client.wordstat.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = response.parse()
            assert_matches_type(WordstatListResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_project(self, client: Keysso) -> None:
        wordstat = client.wordstat.create_project(
            data={},
        )
        assert_matches_type(WordstatCreateProjectResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_project(self, client: Keysso) -> None:
        response = client.wordstat.with_raw_response.create_project(
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = response.parse()
        assert_matches_type(WordstatCreateProjectResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_project(self, client: Keysso) -> None:
        with client.wordstat.with_streaming_response.create_project(
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = response.parse()
            assert_matches_type(WordstatCreateProjectResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_project(self, client: Keysso) -> None:
        wordstat = client.wordstat.delete_project(
            data={},
        )
        assert_matches_type(WordstatDeleteProjectResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_project_with_all_params(self, client: Keysso) -> None:
        wordstat = client.wordstat.delete_project(
            data={"project_id": 1},
        )
        assert_matches_type(WordstatDeleteProjectResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_project(self, client: Keysso) -> None:
        response = client.wordstat.with_raw_response.delete_project(
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = response.parse()
        assert_matches_type(WordstatDeleteProjectResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_project(self, client: Keysso) -> None:
        with client.wordstat.with_streaming_response.delete_project(
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = response.parse()
            assert_matches_type(WordstatDeleteProjectResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_words(self, client: Keysso) -> None:
        wordstat = client.wordstat.delete_words(
            data={},
        )
        assert_matches_type(WordstatDeleteWordsResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_words_with_all_params(self, client: Keysso) -> None:
        wordstat = client.wordstat.delete_words(
            data={
                "project_id": 1,
                "words": ["фраза1", "фраза2", "фраза3"],
            },
        )
        assert_matches_type(WordstatDeleteWordsResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_words(self, client: Keysso) -> None:
        response = client.wordstat.with_raw_response.delete_words(
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = response.parse()
        assert_matches_type(WordstatDeleteWordsResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_words(self, client: Keysso) -> None:
        with client.wordstat.with_streaming_response.delete_words(
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = response.parse()
            assert_matches_type(WordstatDeleteWordsResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_project_status(self, client: Keysso) -> None:
        wordstat = client.wordstat.get_project_status()
        assert_matches_type(WordstatGetProjectStatusResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_project_status_with_all_params(self, client: Keysso) -> None:
        wordstat = client.wordstat.get_project_status(
            id=0,
        )
        assert_matches_type(WordstatGetProjectStatusResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_project_status(self, client: Keysso) -> None:
        response = client.wordstat.with_raw_response.get_project_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = response.parse()
        assert_matches_type(WordstatGetProjectStatusResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_project_status(self, client: Keysso) -> None:
        with client.wordstat.with_streaming_response.get_project_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = response.parse()
            assert_matches_type(WordstatGetProjectStatusResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_projects_completed(self, client: Keysso) -> None:
        wordstat = client.wordstat.get_projects_completed()
        assert_matches_type(WordstatGetProjectsCompletedResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_projects_completed_with_all_params(self, client: Keysso) -> None:
        wordstat = client.wordstat.get_projects_completed(
            ids="ids",
        )
        assert_matches_type(WordstatGetProjectsCompletedResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_projects_completed(self, client: Keysso) -> None:
        response = client.wordstat.with_raw_response.get_projects_completed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = response.parse()
        assert_matches_type(WordstatGetProjectsCompletedResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_projects_completed(self, client: Keysso) -> None:
        with client.wordstat.with_streaming_response.get_projects_completed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = response.parse()
            assert_matches_type(WordstatGetProjectsCompletedResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report(self, client: Keysso) -> None:
        wordstat = client.wordstat.report(
            project_id=0,
        )
        assert_matches_type(WordstatReportResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_with_all_params(self, client: Keysso) -> None:
        wordstat = client.wordstat.report(
            project_id=0,
            full="full",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(WordstatReportResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_report(self, client: Keysso) -> None:
        response = client.wordstat.with_raw_response.report(
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = response.parse()
        assert_matches_type(WordstatReportResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_report(self, client: Keysso) -> None:
        with client.wordstat.with_streaming_response.report(
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = response.parse()
            assert_matches_type(WordstatReportResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWordstat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.list()
        assert_matches_type(WordstatListResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.list(
            is_main=True,
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(WordstatListResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeysso) -> None:
        response = await async_client.wordstat.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = await response.parse()
        assert_matches_type(WordstatListResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeysso) -> None:
        async with async_client.wordstat.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = await response.parse()
            assert_matches_type(WordstatListResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_project(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.create_project(
            data={},
        )
        assert_matches_type(WordstatCreateProjectResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_project(self, async_client: AsyncKeysso) -> None:
        response = await async_client.wordstat.with_raw_response.create_project(
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = await response.parse()
        assert_matches_type(WordstatCreateProjectResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_project(self, async_client: AsyncKeysso) -> None:
        async with async_client.wordstat.with_streaming_response.create_project(
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = await response.parse()
            assert_matches_type(WordstatCreateProjectResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_project(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.delete_project(
            data={},
        )
        assert_matches_type(WordstatDeleteProjectResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_project_with_all_params(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.delete_project(
            data={"project_id": 1},
        )
        assert_matches_type(WordstatDeleteProjectResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_project(self, async_client: AsyncKeysso) -> None:
        response = await async_client.wordstat.with_raw_response.delete_project(
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = await response.parse()
        assert_matches_type(WordstatDeleteProjectResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_project(self, async_client: AsyncKeysso) -> None:
        async with async_client.wordstat.with_streaming_response.delete_project(
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = await response.parse()
            assert_matches_type(WordstatDeleteProjectResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_words(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.delete_words(
            data={},
        )
        assert_matches_type(WordstatDeleteWordsResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_words_with_all_params(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.delete_words(
            data={
                "project_id": 1,
                "words": ["фраза1", "фраза2", "фраза3"],
            },
        )
        assert_matches_type(WordstatDeleteWordsResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_words(self, async_client: AsyncKeysso) -> None:
        response = await async_client.wordstat.with_raw_response.delete_words(
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = await response.parse()
        assert_matches_type(WordstatDeleteWordsResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_words(self, async_client: AsyncKeysso) -> None:
        async with async_client.wordstat.with_streaming_response.delete_words(
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = await response.parse()
            assert_matches_type(WordstatDeleteWordsResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_project_status(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.get_project_status()
        assert_matches_type(WordstatGetProjectStatusResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_project_status_with_all_params(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.get_project_status(
            id=0,
        )
        assert_matches_type(WordstatGetProjectStatusResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_project_status(self, async_client: AsyncKeysso) -> None:
        response = await async_client.wordstat.with_raw_response.get_project_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = await response.parse()
        assert_matches_type(WordstatGetProjectStatusResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_project_status(self, async_client: AsyncKeysso) -> None:
        async with async_client.wordstat.with_streaming_response.get_project_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = await response.parse()
            assert_matches_type(WordstatGetProjectStatusResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_projects_completed(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.get_projects_completed()
        assert_matches_type(WordstatGetProjectsCompletedResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_projects_completed_with_all_params(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.get_projects_completed(
            ids="ids",
        )
        assert_matches_type(WordstatGetProjectsCompletedResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_projects_completed(self, async_client: AsyncKeysso) -> None:
        response = await async_client.wordstat.with_raw_response.get_projects_completed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = await response.parse()
        assert_matches_type(WordstatGetProjectsCompletedResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_projects_completed(self, async_client: AsyncKeysso) -> None:
        async with async_client.wordstat.with_streaming_response.get_projects_completed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = await response.parse()
            assert_matches_type(WordstatGetProjectsCompletedResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.report(
            project_id=0,
        )
        assert_matches_type(WordstatReportResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_with_all_params(self, async_client: AsyncKeysso) -> None:
        wordstat = await async_client.wordstat.report(
            project_id=0,
            full="full",
            page=0,
            per_page=0,
            sort="sort",
        )
        assert_matches_type(WordstatReportResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_report(self, async_client: AsyncKeysso) -> None:
        response = await async_client.wordstat.with_raw_response.report(
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wordstat = await response.parse()
        assert_matches_type(WordstatReportResponse, wordstat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_report(self, async_client: AsyncKeysso) -> None:
        async with async_client.wordstat.with_streaming_response.report(
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wordstat = await response.parse()
            assert_matches_type(WordstatReportResponse, wordstat, path=["response"])

        assert cast(Any, response.is_closed) is True
