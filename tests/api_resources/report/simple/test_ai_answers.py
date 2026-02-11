# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from keysso import Keysso, AsyncKeysso
from tests.utils import assert_matches_type
from keysso.types.report.simple import AIAnswerRetrieveStateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAIAnswers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_state(self, client: Keysso) -> None:
        ai_answer = client.report.simple.ai_answers.retrieve_state(
            domain="domain",
        )
        assert_matches_type(AIAnswerRetrieveStateResponse, ai_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_state_with_all_params(self, client: Keysso) -> None:
        ai_answer = client.report.simple.ai_answers.retrieve_state(
            domain="domain",
            base="msk",
        )
        assert_matches_type(AIAnswerRetrieveStateResponse, ai_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_state(self, client: Keysso) -> None:
        response = client.report.simple.ai_answers.with_raw_response.retrieve_state(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_answer = response.parse()
        assert_matches_type(AIAnswerRetrieveStateResponse, ai_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_state(self, client: Keysso) -> None:
        with client.report.simple.ai_answers.with_streaming_response.retrieve_state(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_answer = response.parse()
            assert_matches_type(AIAnswerRetrieveStateResponse, ai_answer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAIAnswers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_state(self, async_client: AsyncKeysso) -> None:
        ai_answer = await async_client.report.simple.ai_answers.retrieve_state(
            domain="domain",
        )
        assert_matches_type(AIAnswerRetrieveStateResponse, ai_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_state_with_all_params(self, async_client: AsyncKeysso) -> None:
        ai_answer = await async_client.report.simple.ai_answers.retrieve_state(
            domain="domain",
            base="msk",
        )
        assert_matches_type(AIAnswerRetrieveStateResponse, ai_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_state(self, async_client: AsyncKeysso) -> None:
        response = await async_client.report.simple.ai_answers.with_raw_response.retrieve_state(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_answer = await response.parse()
        assert_matches_type(AIAnswerRetrieveStateResponse, ai_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_state(self, async_client: AsyncKeysso) -> None:
        async with async_client.report.simple.ai_answers.with_streaming_response.retrieve_state(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_answer = await response.parse()
            assert_matches_type(AIAnswerRetrieveStateResponse, ai_answer, path=["response"])

        assert cast(Any, response.is_closed) is True
