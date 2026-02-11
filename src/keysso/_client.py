# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import KeyssoError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        zen,
        serp,
        tools,
        limits,
        report,
        robots,
        projects,
        wordstat,
        ai_tracker,
        clustering,
        monitoring,
    )
    from .resources.limits import LimitsResource, AsyncLimitsResource
    from .resources.robots import RobotsResource, AsyncRobotsResource
    from .resources.zen.zen import ZenResource, AsyncZenResource
    from .resources.serp.serp import SerpResource, AsyncSerpResource
    from .resources.tools.tools import ToolsResource, AsyncToolsResource
    from .resources.report.report import ReportResource, AsyncReportResource
    from .resources.projects.projects import ProjectsResource, AsyncProjectsResource
    from .resources.wordstat.wordstat import WordstatResource, AsyncWordstatResource
    from .resources.ai_tracker.ai_tracker import AITrackerResource, AsyncAITrackerResource
    from .resources.clustering.clustering import ClusteringResource, AsyncClusteringResource
    from .resources.monitoring.monitoring import MonitoringResource, AsyncMonitoringResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Keysso", "AsyncKeysso", "Client", "AsyncClient"]


class Keysso(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Keysso client instance.

        This automatically infers the `api_key` argument from the `KEYSSO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("KEYSSO_API_KEY")
        if api_key is None:
            raise KeyssoError(
                "The api_key client option must be set either by passing api_key to the client or by setting the KEYSSO_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("KEYSSO_BASE_URL")
        if base_url is None:
            base_url = f"https://api.keys.so"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def report(self) -> ReportResource:
        from .resources.report import ReportResource

        return ReportResource(self)

    @cached_property
    def tools(self) -> ToolsResource:
        from .resources.tools import ToolsResource

        return ToolsResource(self)

    @cached_property
    def clustering(self) -> ClusteringResource:
        from .resources.clustering import ClusteringResource

        return ClusteringResource(self)

    @cached_property
    def projects(self) -> ProjectsResource:
        from .resources.projects import ProjectsResource

        return ProjectsResource(self)

    @cached_property
    def robots(self) -> RobotsResource:
        from .resources.robots import RobotsResource

        return RobotsResource(self)

    @cached_property
    def wordstat(self) -> WordstatResource:
        from .resources.wordstat import WordstatResource

        return WordstatResource(self)

    @cached_property
    def serp(self) -> SerpResource:
        from .resources.serp import SerpResource

        return SerpResource(self)

    @cached_property
    def zen(self) -> ZenResource:
        from .resources.zen import ZenResource

        return ZenResource(self)

    @cached_property
    def limits(self) -> LimitsResource:
        from .resources.limits import LimitsResource

        return LimitsResource(self)

    @cached_property
    def monitoring(self) -> MonitoringResource:
        from .resources.monitoring import MonitoringResource

        return MonitoringResource(self)

    @cached_property
    def ai_tracker(self) -> AITrackerResource:
        from .resources.ai_tracker import AITrackerResource

        return AITrackerResource(self)

    @cached_property
    def with_raw_response(self) -> KeyssoWithRawResponse:
        return KeyssoWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeyssoWithStreamedResponse:
        return KeyssoWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-Keyso-TOKEN": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncKeysso(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncKeysso client instance.

        This automatically infers the `api_key` argument from the `KEYSSO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("KEYSSO_API_KEY")
        if api_key is None:
            raise KeyssoError(
                "The api_key client option must be set either by passing api_key to the client or by setting the KEYSSO_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("KEYSSO_BASE_URL")
        if base_url is None:
            base_url = f"https://api.keys.so"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def report(self) -> AsyncReportResource:
        from .resources.report import AsyncReportResource

        return AsyncReportResource(self)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        from .resources.tools import AsyncToolsResource

        return AsyncToolsResource(self)

    @cached_property
    def clustering(self) -> AsyncClusteringResource:
        from .resources.clustering import AsyncClusteringResource

        return AsyncClusteringResource(self)

    @cached_property
    def projects(self) -> AsyncProjectsResource:
        from .resources.projects import AsyncProjectsResource

        return AsyncProjectsResource(self)

    @cached_property
    def robots(self) -> AsyncRobotsResource:
        from .resources.robots import AsyncRobotsResource

        return AsyncRobotsResource(self)

    @cached_property
    def wordstat(self) -> AsyncWordstatResource:
        from .resources.wordstat import AsyncWordstatResource

        return AsyncWordstatResource(self)

    @cached_property
    def serp(self) -> AsyncSerpResource:
        from .resources.serp import AsyncSerpResource

        return AsyncSerpResource(self)

    @cached_property
    def zen(self) -> AsyncZenResource:
        from .resources.zen import AsyncZenResource

        return AsyncZenResource(self)

    @cached_property
    def limits(self) -> AsyncLimitsResource:
        from .resources.limits import AsyncLimitsResource

        return AsyncLimitsResource(self)

    @cached_property
    def monitoring(self) -> AsyncMonitoringResource:
        from .resources.monitoring import AsyncMonitoringResource

        return AsyncMonitoringResource(self)

    @cached_property
    def ai_tracker(self) -> AsyncAITrackerResource:
        from .resources.ai_tracker import AsyncAITrackerResource

        return AsyncAITrackerResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncKeyssoWithRawResponse:
        return AsyncKeyssoWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeyssoWithStreamedResponse:
        return AsyncKeyssoWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-Keyso-TOKEN": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class KeyssoWithRawResponse:
    _client: Keysso

    def __init__(self, client: Keysso) -> None:
        self._client = client

    @cached_property
    def report(self) -> report.ReportResourceWithRawResponse:
        from .resources.report import ReportResourceWithRawResponse

        return ReportResourceWithRawResponse(self._client.report)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithRawResponse:
        from .resources.tools import ToolsResourceWithRawResponse

        return ToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def clustering(self) -> clustering.ClusteringResourceWithRawResponse:
        from .resources.clustering import ClusteringResourceWithRawResponse

        return ClusteringResourceWithRawResponse(self._client.clustering)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithRawResponse:
        from .resources.projects import ProjectsResourceWithRawResponse

        return ProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def robots(self) -> robots.RobotsResourceWithRawResponse:
        from .resources.robots import RobotsResourceWithRawResponse

        return RobotsResourceWithRawResponse(self._client.robots)

    @cached_property
    def wordstat(self) -> wordstat.WordstatResourceWithRawResponse:
        from .resources.wordstat import WordstatResourceWithRawResponse

        return WordstatResourceWithRawResponse(self._client.wordstat)

    @cached_property
    def serp(self) -> serp.SerpResourceWithRawResponse:
        from .resources.serp import SerpResourceWithRawResponse

        return SerpResourceWithRawResponse(self._client.serp)

    @cached_property
    def zen(self) -> zen.ZenResourceWithRawResponse:
        from .resources.zen import ZenResourceWithRawResponse

        return ZenResourceWithRawResponse(self._client.zen)

    @cached_property
    def limits(self) -> limits.LimitsResourceWithRawResponse:
        from .resources.limits import LimitsResourceWithRawResponse

        return LimitsResourceWithRawResponse(self._client.limits)

    @cached_property
    def monitoring(self) -> monitoring.MonitoringResourceWithRawResponse:
        from .resources.monitoring import MonitoringResourceWithRawResponse

        return MonitoringResourceWithRawResponse(self._client.monitoring)

    @cached_property
    def ai_tracker(self) -> ai_tracker.AITrackerResourceWithRawResponse:
        from .resources.ai_tracker import AITrackerResourceWithRawResponse

        return AITrackerResourceWithRawResponse(self._client.ai_tracker)


class AsyncKeyssoWithRawResponse:
    _client: AsyncKeysso

    def __init__(self, client: AsyncKeysso) -> None:
        self._client = client

    @cached_property
    def report(self) -> report.AsyncReportResourceWithRawResponse:
        from .resources.report import AsyncReportResourceWithRawResponse

        return AsyncReportResourceWithRawResponse(self._client.report)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithRawResponse:
        from .resources.tools import AsyncToolsResourceWithRawResponse

        return AsyncToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def clustering(self) -> clustering.AsyncClusteringResourceWithRawResponse:
        from .resources.clustering import AsyncClusteringResourceWithRawResponse

        return AsyncClusteringResourceWithRawResponse(self._client.clustering)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithRawResponse:
        from .resources.projects import AsyncProjectsResourceWithRawResponse

        return AsyncProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def robots(self) -> robots.AsyncRobotsResourceWithRawResponse:
        from .resources.robots import AsyncRobotsResourceWithRawResponse

        return AsyncRobotsResourceWithRawResponse(self._client.robots)

    @cached_property
    def wordstat(self) -> wordstat.AsyncWordstatResourceWithRawResponse:
        from .resources.wordstat import AsyncWordstatResourceWithRawResponse

        return AsyncWordstatResourceWithRawResponse(self._client.wordstat)

    @cached_property
    def serp(self) -> serp.AsyncSerpResourceWithRawResponse:
        from .resources.serp import AsyncSerpResourceWithRawResponse

        return AsyncSerpResourceWithRawResponse(self._client.serp)

    @cached_property
    def zen(self) -> zen.AsyncZenResourceWithRawResponse:
        from .resources.zen import AsyncZenResourceWithRawResponse

        return AsyncZenResourceWithRawResponse(self._client.zen)

    @cached_property
    def limits(self) -> limits.AsyncLimitsResourceWithRawResponse:
        from .resources.limits import AsyncLimitsResourceWithRawResponse

        return AsyncLimitsResourceWithRawResponse(self._client.limits)

    @cached_property
    def monitoring(self) -> monitoring.AsyncMonitoringResourceWithRawResponse:
        from .resources.monitoring import AsyncMonitoringResourceWithRawResponse

        return AsyncMonitoringResourceWithRawResponse(self._client.monitoring)

    @cached_property
    def ai_tracker(self) -> ai_tracker.AsyncAITrackerResourceWithRawResponse:
        from .resources.ai_tracker import AsyncAITrackerResourceWithRawResponse

        return AsyncAITrackerResourceWithRawResponse(self._client.ai_tracker)


class KeyssoWithStreamedResponse:
    _client: Keysso

    def __init__(self, client: Keysso) -> None:
        self._client = client

    @cached_property
    def report(self) -> report.ReportResourceWithStreamingResponse:
        from .resources.report import ReportResourceWithStreamingResponse

        return ReportResourceWithStreamingResponse(self._client.report)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithStreamingResponse:
        from .resources.tools import ToolsResourceWithStreamingResponse

        return ToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def clustering(self) -> clustering.ClusteringResourceWithStreamingResponse:
        from .resources.clustering import ClusteringResourceWithStreamingResponse

        return ClusteringResourceWithStreamingResponse(self._client.clustering)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithStreamingResponse:
        from .resources.projects import ProjectsResourceWithStreamingResponse

        return ProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def robots(self) -> robots.RobotsResourceWithStreamingResponse:
        from .resources.robots import RobotsResourceWithStreamingResponse

        return RobotsResourceWithStreamingResponse(self._client.robots)

    @cached_property
    def wordstat(self) -> wordstat.WordstatResourceWithStreamingResponse:
        from .resources.wordstat import WordstatResourceWithStreamingResponse

        return WordstatResourceWithStreamingResponse(self._client.wordstat)

    @cached_property
    def serp(self) -> serp.SerpResourceWithStreamingResponse:
        from .resources.serp import SerpResourceWithStreamingResponse

        return SerpResourceWithStreamingResponse(self._client.serp)

    @cached_property
    def zen(self) -> zen.ZenResourceWithStreamingResponse:
        from .resources.zen import ZenResourceWithStreamingResponse

        return ZenResourceWithStreamingResponse(self._client.zen)

    @cached_property
    def limits(self) -> limits.LimitsResourceWithStreamingResponse:
        from .resources.limits import LimitsResourceWithStreamingResponse

        return LimitsResourceWithStreamingResponse(self._client.limits)

    @cached_property
    def monitoring(self) -> monitoring.MonitoringResourceWithStreamingResponse:
        from .resources.monitoring import MonitoringResourceWithStreamingResponse

        return MonitoringResourceWithStreamingResponse(self._client.monitoring)

    @cached_property
    def ai_tracker(self) -> ai_tracker.AITrackerResourceWithStreamingResponse:
        from .resources.ai_tracker import AITrackerResourceWithStreamingResponse

        return AITrackerResourceWithStreamingResponse(self._client.ai_tracker)


class AsyncKeyssoWithStreamedResponse:
    _client: AsyncKeysso

    def __init__(self, client: AsyncKeysso) -> None:
        self._client = client

    @cached_property
    def report(self) -> report.AsyncReportResourceWithStreamingResponse:
        from .resources.report import AsyncReportResourceWithStreamingResponse

        return AsyncReportResourceWithStreamingResponse(self._client.report)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithStreamingResponse:
        from .resources.tools import AsyncToolsResourceWithStreamingResponse

        return AsyncToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def clustering(self) -> clustering.AsyncClusteringResourceWithStreamingResponse:
        from .resources.clustering import AsyncClusteringResourceWithStreamingResponse

        return AsyncClusteringResourceWithStreamingResponse(self._client.clustering)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithStreamingResponse:
        from .resources.projects import AsyncProjectsResourceWithStreamingResponse

        return AsyncProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def robots(self) -> robots.AsyncRobotsResourceWithStreamingResponse:
        from .resources.robots import AsyncRobotsResourceWithStreamingResponse

        return AsyncRobotsResourceWithStreamingResponse(self._client.robots)

    @cached_property
    def wordstat(self) -> wordstat.AsyncWordstatResourceWithStreamingResponse:
        from .resources.wordstat import AsyncWordstatResourceWithStreamingResponse

        return AsyncWordstatResourceWithStreamingResponse(self._client.wordstat)

    @cached_property
    def serp(self) -> serp.AsyncSerpResourceWithStreamingResponse:
        from .resources.serp import AsyncSerpResourceWithStreamingResponse

        return AsyncSerpResourceWithStreamingResponse(self._client.serp)

    @cached_property
    def zen(self) -> zen.AsyncZenResourceWithStreamingResponse:
        from .resources.zen import AsyncZenResourceWithStreamingResponse

        return AsyncZenResourceWithStreamingResponse(self._client.zen)

    @cached_property
    def limits(self) -> limits.AsyncLimitsResourceWithStreamingResponse:
        from .resources.limits import AsyncLimitsResourceWithStreamingResponse

        return AsyncLimitsResourceWithStreamingResponse(self._client.limits)

    @cached_property
    def monitoring(self) -> monitoring.AsyncMonitoringResourceWithStreamingResponse:
        from .resources.monitoring import AsyncMonitoringResourceWithStreamingResponse

        return AsyncMonitoringResourceWithStreamingResponse(self._client.monitoring)

    @cached_property
    def ai_tracker(self) -> ai_tracker.AsyncAITrackerResourceWithStreamingResponse:
        from .resources.ai_tracker import AsyncAITrackerResourceWithStreamingResponse

        return AsyncAITrackerResourceWithStreamingResponse(self._client.ai_tracker)


Client = Keysso

AsyncClient = AsyncKeysso
