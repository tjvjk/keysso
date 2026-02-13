# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ..types import (
    wordstat_list_params,
    wordstat_report_params,
    wordstat_delete_words_params,
    wordstat_create_project_params,
    wordstat_delete_project_params,
    wordstat_get_project_status_params,
    wordstat_get_projects_completed_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.wordstat_list_response import WordstatListResponse
from ..types.wordstat_report_response import WordstatReportResponse
from ..types.wordstat_delete_words_response import WordstatDeleteWordsResponse
from ..types.wordstat_create_project_response import WordstatCreateProjectResponse
from ..types.wordstat_delete_project_response import WordstatDeleteProjectResponse
from ..types.wordstat_get_project_status_response import WordstatGetProjectStatusResponse
from ..types.wordstat_get_projects_completed_response import WordstatGetProjectsCompletedResponse

__all__ = ["WordstatResource", "AsyncWordstatResource"]


class WordstatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WordstatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return WordstatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WordstatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return WordstatResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        is_main: bool | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatListResponse:
        """
        Пример запроса
        `https://api.keys.so/wordstat/list?sort=created_at%7Cdesc&page=1&per_page=25`

        Args:
          is_main: **Список проектов:** `true` — только созданные вручную `false` — все проекты,
              включая созданные автоматически родительскими типами проектов

              **Иерархия проектов:** `Мониторинг » Кластеризатор » Выдача | Wordstat`

          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/wordstat/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_main": is_main,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    wordstat_list_params.WordstatListParams,
                ),
            ),
            cast_to=WordstatListResponse,
        )

    def create_project(
        self,
        *,
        data: Union[wordstat_create_project_params.DataType1, wordstat_create_project_params.DataType0],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatCreateProjectResponse:
        """
        Пример запроса: `https://api.keys.so/wordstat/create-project`

        Args:
          data: Данные для парсинга

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/wordstat/create-project",
            body=maybe_transform({"data": data}, wordstat_create_project_params.WordstatCreateProjectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WordstatCreateProjectResponse,
        )

    def delete_project(
        self,
        *,
        data: wordstat_delete_project_params.Data,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatDeleteProjectResponse:
        """
        Пример запроса `https://api.keys.so/wordstat/delete-project`

        Args:
          data: Данные

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/wordstat/delete-project",
            body=maybe_transform({"data": data}, wordstat_delete_project_params.WordstatDeleteProjectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WordstatDeleteProjectResponse,
        )

    def delete_words(
        self,
        *,
        data: wordstat_delete_words_params.Data,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatDeleteWordsResponse:
        """
        Пример запроса `https://api.keys.so/wordstat/delete-words`

        Args:
          data: Данные для парсинга

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/wordstat/delete-words",
            body=maybe_transform({"data": data}, wordstat_delete_words_params.WordstatDeleteWordsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WordstatDeleteWordsResponse,
        )

    def get_project_status(
        self,
        *,
        id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatGetProjectStatusResponse:
        """
        Пример запроса `https://api.keys.so/wordstat/get-project-status?id=5672`

        Args:
          id: ID проекта

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/wordstat/get-project-status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, wordstat_get_project_status_params.WordstatGetProjectStatusParams),
            ),
            cast_to=WordstatGetProjectStatusResponse,
        )

    def get_projects_completed(
        self,
        *,
        ids: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatGetProjectsCompletedResponse:
        """
        Пример запроса
        `https://api.keys.so/wordstat/get-projects-completed?ids=5672,3421,342`

        Args:
          ids: ID проектов через запятую

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/wordstat/get-projects-completed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"ids": ids}, wordstat_get_projects_completed_params.WordstatGetProjectsCompletedParams
                ),
            ),
            cast_to=WordstatGetProjectsCompletedResponse,
        )

    def report(
        self,
        *,
        project_id: int,
        full: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatReportResponse:
        """
        Пример запроса
        `https://api.keys.so/wordstat/report?projectId=1&sort=swsk%7Cdesc&page=1&per_page=25`

        Args:
          project_id: Идентификатор проекта

          full: При наличии данного параметра будет отдан полный отчет, при отсутствии ответ
              будет сгруппирован по запросу

          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/wordstat/report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "project_id": project_id,
                        "full": full,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    wordstat_report_params.WordstatReportParams,
                ),
            ),
            cast_to=WordstatReportResponse,
        )


class AsyncWordstatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWordstatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tjvjk/keysso#accessing-raw-response-data-eg-headers
        """
        return AsyncWordstatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWordstatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tjvjk/keysso#with_streaming_response
        """
        return AsyncWordstatResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        is_main: bool | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatListResponse:
        """
        Пример запроса
        `https://api.keys.so/wordstat/list?sort=created_at%7Cdesc&page=1&per_page=25`

        Args:
          is_main: **Список проектов:** `true` — только созданные вручную `false` — все проекты,
              включая созданные автоматически родительскими типами проектов

              **Иерархия проектов:** `Мониторинг » Кластеризатор » Выдача | Wordstat`

          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/wordstat/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "is_main": is_main,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    wordstat_list_params.WordstatListParams,
                ),
            ),
            cast_to=WordstatListResponse,
        )

    async def create_project(
        self,
        *,
        data: Union[wordstat_create_project_params.DataType1, wordstat_create_project_params.DataType0],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatCreateProjectResponse:
        """
        Пример запроса: `https://api.keys.so/wordstat/create-project`

        Args:
          data: Данные для парсинга

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/wordstat/create-project",
            body=await async_maybe_transform(
                {"data": data}, wordstat_create_project_params.WordstatCreateProjectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WordstatCreateProjectResponse,
        )

    async def delete_project(
        self,
        *,
        data: wordstat_delete_project_params.Data,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatDeleteProjectResponse:
        """
        Пример запроса `https://api.keys.so/wordstat/delete-project`

        Args:
          data: Данные

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/wordstat/delete-project",
            body=await async_maybe_transform(
                {"data": data}, wordstat_delete_project_params.WordstatDeleteProjectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WordstatDeleteProjectResponse,
        )

    async def delete_words(
        self,
        *,
        data: wordstat_delete_words_params.Data,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatDeleteWordsResponse:
        """
        Пример запроса `https://api.keys.so/wordstat/delete-words`

        Args:
          data: Данные для парсинга

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/wordstat/delete-words",
            body=await async_maybe_transform({"data": data}, wordstat_delete_words_params.WordstatDeleteWordsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WordstatDeleteWordsResponse,
        )

    async def get_project_status(
        self,
        *,
        id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatGetProjectStatusResponse:
        """
        Пример запроса `https://api.keys.so/wordstat/get-project-status?id=5672`

        Args:
          id: ID проекта

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/wordstat/get-project-status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"id": id}, wordstat_get_project_status_params.WordstatGetProjectStatusParams
                ),
            ),
            cast_to=WordstatGetProjectStatusResponse,
        )

    async def get_projects_completed(
        self,
        *,
        ids: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatGetProjectsCompletedResponse:
        """
        Пример запроса
        `https://api.keys.so/wordstat/get-projects-completed?ids=5672,3421,342`

        Args:
          ids: ID проектов через запятую

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/wordstat/get-projects-completed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"ids": ids}, wordstat_get_projects_completed_params.WordstatGetProjectsCompletedParams
                ),
            ),
            cast_to=WordstatGetProjectsCompletedResponse,
        )

    async def report(
        self,
        *,
        project_id: int,
        full: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WordstatReportResponse:
        """
        Пример запроса
        `https://api.keys.so/wordstat/report?projectId=1&sort=swsk%7Cdesc&page=1&per_page=25`

        Args:
          project_id: Идентификатор проекта

          full: При наличии данного параметра будет отдан полный отчет, при отсутствии ответ
              будет сгруппирован по запросу

          page: Порядковый номер страницы результатов

          per_page: Количество результатов на одной странице

          sort: Сортировка данных по полям.

              Формат: `field|direction`, где

              `field` - имя колонки `direction` - направление сортировки, asc - по
              возрастанию, desc - по убыванию

              Например: `pos|asc`, либо по двум полям `pos|asc,wsk|desc`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/wordstat/report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "project_id": project_id,
                        "full": full,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    wordstat_report_params.WordstatReportParams,
                ),
            ),
            cast_to=WordstatReportResponse,
        )


class WordstatResourceWithRawResponse:
    def __init__(self, wordstat: WordstatResource) -> None:
        self._wordstat = wordstat

        self.list = to_raw_response_wrapper(
            wordstat.list,
        )
        self.create_project = to_raw_response_wrapper(
            wordstat.create_project,
        )
        self.delete_project = to_raw_response_wrapper(
            wordstat.delete_project,
        )
        self.delete_words = to_raw_response_wrapper(
            wordstat.delete_words,
        )
        self.get_project_status = to_raw_response_wrapper(
            wordstat.get_project_status,
        )
        self.get_projects_completed = to_raw_response_wrapper(
            wordstat.get_projects_completed,
        )
        self.report = to_raw_response_wrapper(
            wordstat.report,
        )


class AsyncWordstatResourceWithRawResponse:
    def __init__(self, wordstat: AsyncWordstatResource) -> None:
        self._wordstat = wordstat

        self.list = async_to_raw_response_wrapper(
            wordstat.list,
        )
        self.create_project = async_to_raw_response_wrapper(
            wordstat.create_project,
        )
        self.delete_project = async_to_raw_response_wrapper(
            wordstat.delete_project,
        )
        self.delete_words = async_to_raw_response_wrapper(
            wordstat.delete_words,
        )
        self.get_project_status = async_to_raw_response_wrapper(
            wordstat.get_project_status,
        )
        self.get_projects_completed = async_to_raw_response_wrapper(
            wordstat.get_projects_completed,
        )
        self.report = async_to_raw_response_wrapper(
            wordstat.report,
        )


class WordstatResourceWithStreamingResponse:
    def __init__(self, wordstat: WordstatResource) -> None:
        self._wordstat = wordstat

        self.list = to_streamed_response_wrapper(
            wordstat.list,
        )
        self.create_project = to_streamed_response_wrapper(
            wordstat.create_project,
        )
        self.delete_project = to_streamed_response_wrapper(
            wordstat.delete_project,
        )
        self.delete_words = to_streamed_response_wrapper(
            wordstat.delete_words,
        )
        self.get_project_status = to_streamed_response_wrapper(
            wordstat.get_project_status,
        )
        self.get_projects_completed = to_streamed_response_wrapper(
            wordstat.get_projects_completed,
        )
        self.report = to_streamed_response_wrapper(
            wordstat.report,
        )


class AsyncWordstatResourceWithStreamingResponse:
    def __init__(self, wordstat: AsyncWordstatResource) -> None:
        self._wordstat = wordstat

        self.list = async_to_streamed_response_wrapper(
            wordstat.list,
        )
        self.create_project = async_to_streamed_response_wrapper(
            wordstat.create_project,
        )
        self.delete_project = async_to_streamed_response_wrapper(
            wordstat.delete_project,
        )
        self.delete_words = async_to_streamed_response_wrapper(
            wordstat.delete_words,
        )
        self.get_project_status = async_to_streamed_response_wrapper(
            wordstat.get_project_status,
        )
        self.get_projects_completed = async_to_streamed_response_wrapper(
            wordstat.get_projects_completed,
        )
        self.report = async_to_streamed_response_wrapper(
            wordstat.report,
        )
