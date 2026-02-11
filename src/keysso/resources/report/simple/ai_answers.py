# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.report import Base
from ....types.report.base import Base
from ....types.report.simple import ai_answer_retrieve_state_params
from ....types.report.simple.ai_answer_retrieve_state_response import AIAnswerRetrieveStateResponse

__all__ = ["AIAnswersResource", "AsyncAIAnswersResource"]


class AIAnswersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AIAnswersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AIAnswersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIAnswersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AIAnswersResourceWithStreamingResponse(self)

    def retrieve_state(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIAnswerRetrieveStateResponse:
        """Возвращает текущий статус построения ИИ-отчёта для домена.

        Используется для
        проверки готовности отчёта перед запросом данных.

        Пример запроса:
        `https://api.keys.so/report/simple/ai-answers/state?base=msk&domain=wildberries.ru`

        Args:
          domain: Имя домена

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/report/simple/ai-answers/state",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                    },
                    ai_answer_retrieve_state_params.AIAnswerRetrieveStateParams,
                ),
            ),
            cast_to=AIAnswerRetrieveStateResponse,
        )


class AsyncAIAnswersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAIAnswersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncAIAnswersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIAnswersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncAIAnswersResourceWithStreamingResponse(self)

    async def retrieve_state(
        self,
        *,
        domain: str,
        base: Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIAnswerRetrieveStateResponse:
        """Возвращает текущий статус построения ИИ-отчёта для домена.

        Используется для
        проверки готовности отчёта перед запросом данных.

        Пример запроса:
        `https://api.keys.so/report/simple/ai-answers/state?base=msk&domain=wildberries.ru`

        Args:
          domain: Имя домена

          base: Региональная база данных, по которой происходит выборка `msk` - Яндекс: Москва
              `gru` - Google: Москва `zen` - Дзен `gkv` - Google: Киев `rnd` - Яндекс:
              Ростов-на-Дону `ekb` - Яндекс: Екатеринбург `ufa` - Яндекс: Уфа `sar` - Яндекс:
              Саратов `krr` - Яндекс: Краснодар `prm` - Яндекс: Пермь `sam` - Яндекс: Самара
              `kry` - Яндекс: Красноярск `oms` - Яндекс: Омск `kzn` - Яндекс: Казань `che` -
              Яндекс: Челябинск `nsk` - Яндекс: Новосибирск `nnv` - Яндекс: Н. Новгород
              `vlg` - Яндекс: Волгоград `vrn` - Яндекс: Воронеж `spb` - Яндекс:
              Санкт-Петербург `mns` - Яндекс: Минск `tmn` - Яндекс: Тюмень `gmns` - Google:
              Минск `tom` - Яндекс: Томск `gny` - Google: New York

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/report/simple/ai-answers/state",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "base": base,
                    },
                    ai_answer_retrieve_state_params.AIAnswerRetrieveStateParams,
                ),
            ),
            cast_to=AIAnswerRetrieveStateResponse,
        )


class AIAnswersResourceWithRawResponse:
    def __init__(self, ai_answers: AIAnswersResource) -> None:
        self._ai_answers = ai_answers

        self.retrieve_state = to_raw_response_wrapper(
            ai_answers.retrieve_state,
        )


class AsyncAIAnswersResourceWithRawResponse:
    def __init__(self, ai_answers: AsyncAIAnswersResource) -> None:
        self._ai_answers = ai_answers

        self.retrieve_state = async_to_raw_response_wrapper(
            ai_answers.retrieve_state,
        )


class AIAnswersResourceWithStreamingResponse:
    def __init__(self, ai_answers: AIAnswersResource) -> None:
        self._ai_answers = ai_answers

        self.retrieve_state = to_streamed_response_wrapper(
            ai_answers.retrieve_state,
        )


class AsyncAIAnswersResourceWithStreamingResponse:
    def __init__(self, ai_answers: AsyncAIAnswersResource) -> None:
        self._ai_answers = ai_answers

        self.retrieve_state = async_to_streamed_response_wrapper(
            ai_answers.retrieve_state,
        )
