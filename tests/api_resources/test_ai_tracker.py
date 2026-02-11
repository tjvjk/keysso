# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types import (
    AITrackerListResponse,
    AITrackerCreateResponse,
    AITrackerGetStateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAITracker:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Keysso) -> None:
        ai_tracker = client.ai_tracker.create(
            brand="keys.so",
            description=["SEO"],
            systems=[3, 6, 7],
        )
        assert_matches_type(AITrackerCreateResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Keysso) -> None:
        ai_tracker = client.ai_tracker.create(
            brand="keys.so",
            description=["SEO"],
            systems=[3, 6, 7],
            competitors=["Keysso", "Кейссо"],
            prompts=[
                {
                    "groups": ["SEO", "Marketing"],
                    "prompt": "Отзывы о keys.so",
                }
            ],
            start=True,
            synonyms=["кейсо"],
        )
        assert_matches_type(AITrackerCreateResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Keysso) -> None:
        response = client.ai_tracker.with_raw_response.create(
            brand="keys.so",
            description=["SEO"],
            systems=[3, 6, 7],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_tracker = response.parse()
        assert_matches_type(AITrackerCreateResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Keysso) -> None:
        with client.ai_tracker.with_streaming_response.create(
            brand="keys.so",
            description=["SEO"],
            systems=[3, 6, 7],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_tracker = response.parse()
            assert_matches_type(AITrackerCreateResponse, ai_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Keysso) -> None:
        ai_tracker = client.ai_tracker.list()
        assert_matches_type(AITrackerListResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Keysso) -> None:
        ai_tracker = client.ai_tracker.list(
            page=0,
            per_page=0,
            search="search",
        )
        assert_matches_type(AITrackerListResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Keysso) -> None:
        response = client.ai_tracker.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_tracker = response.parse()
        assert_matches_type(AITrackerListResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Keysso) -> None:
        with client.ai_tracker.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_tracker = response.parse()
            assert_matches_type(AITrackerListResponse, ai_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_state(self, client: Keysso) -> None:
        ai_tracker = client.ai_tracker.get_state(
            ids=[0],
        )
        assert_matches_type(AITrackerGetStateResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_state(self, client: Keysso) -> None:
        response = client.ai_tracker.with_raw_response.get_state(
            ids=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_tracker = response.parse()
        assert_matches_type(AITrackerGetStateResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_state(self, client: Keysso) -> None:
        with client.ai_tracker.with_streaming_response.get_state(
            ids=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_tracker = response.parse()
            assert_matches_type(AITrackerGetStateResponse, ai_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAITracker:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKeysso) -> None:
        ai_tracker = await async_client.ai_tracker.create(
            brand="keys.so",
            description=["SEO"],
            systems=[3, 6, 7],
        )
        assert_matches_type(AITrackerCreateResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKeysso) -> None:
        ai_tracker = await async_client.ai_tracker.create(
            brand="keys.so",
            description=["SEO"],
            systems=[3, 6, 7],
            competitors=["Keysso", "Кейссо"],
            prompts=[
                {
                    "groups": ["SEO", "Marketing"],
                    "prompt": "Отзывы о keys.so",
                }
            ],
            start=True,
            synonyms=["кейсо"],
        )
        assert_matches_type(AITrackerCreateResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKeysso) -> None:
        response = await async_client.ai_tracker.with_raw_response.create(
            brand="keys.so",
            description=["SEO"],
            systems=[3, 6, 7],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_tracker = await response.parse()
        assert_matches_type(AITrackerCreateResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKeysso) -> None:
        async with async_client.ai_tracker.with_streaming_response.create(
            brand="keys.so",
            description=["SEO"],
            systems=[3, 6, 7],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_tracker = await response.parse()
            assert_matches_type(AITrackerCreateResponse, ai_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKeysso) -> None:
        ai_tracker = await async_client.ai_tracker.list()
        assert_matches_type(AITrackerListResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKeysso) -> None:
        ai_tracker = await async_client.ai_tracker.list(
            page=0,
            per_page=0,
            search="search",
        )
        assert_matches_type(AITrackerListResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKeysso) -> None:
        response = await async_client.ai_tracker.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_tracker = await response.parse()
        assert_matches_type(AITrackerListResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKeysso) -> None:
        async with async_client.ai_tracker.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_tracker = await response.parse()
            assert_matches_type(AITrackerListResponse, ai_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_state(self, async_client: AsyncKeysso) -> None:
        ai_tracker = await async_client.ai_tracker.get_state(
            ids=[0],
        )
        assert_matches_type(AITrackerGetStateResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_state(self, async_client: AsyncKeysso) -> None:
        response = await async_client.ai_tracker.with_raw_response.get_state(
            ids=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_tracker = await response.parse()
        assert_matches_type(AITrackerGetStateResponse, ai_tracker, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_state(self, async_client: AsyncKeysso) -> None:
        async with async_client.ai_tracker.with_streaming_response.get_state(
            ids=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_tracker = await response.parse()
            assert_matches_type(AITrackerGetStateResponse, ai_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True
