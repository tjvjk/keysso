# Report

Types:

```python
from keysso.types import (
    ReportCompareBacklinksResponse,
    ReportCompareContextResponse,
    ReportCompareOrganicResponse,
    ReportCreateSystemKeywordsResponse,
)
```

Methods:

- <code title="get /report/compare?view=backlinks">client.report.<a href="./src/keysso/resources/report/report.py">compare_backlinks</a>(\*\*<a href="src/keysso/types/report_compare_backlinks_params.py">params</a>) -> <a href="./src/keysso/types/report_compare_backlinks_response.py">ReportCompareBacklinksResponse</a></code>
- <code title="get /report/compare?view=context">client.report.<a href="./src/keysso/resources/report/report.py">compare_context</a>(\*\*<a href="src/keysso/types/report_compare_context_params.py">params</a>) -> <a href="./src/keysso/types/report_compare_context_response.py">ReportCompareContextResponse</a></code>
- <code title="get /report/compare?view=organic">client.report.<a href="./src/keysso/resources/report/report.py">compare_organic</a>(\*\*<a href="src/keysso/types/report_compare_organic_params.py">params</a>) -> <a href="./src/keysso/types/report_compare_organic_response.py">ReportCompareOrganicResponse</a></code>
- <code title="post /report/system_keywords">client.report.<a href="./src/keysso/resources/report/report.py">create_system_keywords</a>(\*\*<a href="src/keysso/types/report_create_system_keywords_params.py">params</a>) -> <a href="./src/keysso/types/report_create_system_keywords_response.py">ReportCreateSystemKeywordsResponse</a></code>

## Simple

Types:

```python
from keysso.types.report import (
    SimpleRetrieveDomainAdHistoryResponse,
    SimpleRetrieveDomainDashboardResponse,
    SimpleRetrieveKeywordDashboardResponse,
    SimpleRetrieveSimilarkeysResponse,
    SimpleRetrieveTopDomainVisibilityResponse,
)
```

Methods:

- <code title="get /report/simple/domain_ad_history">client.report.simple.<a href="./src/keysso/resources/report/simple/simple.py">retrieve_domain_ad_history</a>(\*\*<a href="src/keysso/types/report/simple_retrieve_domain_ad_history_params.py">params</a>) -> <a href="./src/keysso/types/report/simple_retrieve_domain_ad_history_response.py">SimpleRetrieveDomainAdHistoryResponse</a></code>
- <code title="get /report/simple/domain_dashboard">client.report.simple.<a href="./src/keysso/resources/report/simple/simple.py">retrieve_domain_dashboard</a>(\*\*<a href="src/keysso/types/report/simple_retrieve_domain_dashboard_params.py">params</a>) -> <a href="./src/keysso/types/report/simple_retrieve_domain_dashboard_response.py">SimpleRetrieveDomainDashboardResponse</a></code>
- <code title="get /report/simple/keyword_dashboard">client.report.simple.<a href="./src/keysso/resources/report/simple/simple.py">retrieve_keyword_dashboard</a>(\*\*<a href="src/keysso/types/report/simple_retrieve_keyword_dashboard_params.py">params</a>) -> <a href="./src/keysso/types/report/simple_retrieve_keyword_dashboard_response.py">SimpleRetrieveKeywordDashboardResponse</a></code>
- <code title="get /report/simple/similarkeys">client.report.simple.<a href="./src/keysso/resources/report/simple/simple.py">retrieve_similarkeys</a>(\*\*<a href="src/keysso/types/report/simple_retrieve_similarkeys_params.py">params</a>) -> <a href="./src/keysso/types/report/simple_retrieve_similarkeys_response.py">SimpleRetrieveSimilarkeysResponse</a></code>
- <code title="get /report/simple/top_domain_visibility">client.report.simple.<a href="./src/keysso/resources/report/simple/simple.py">retrieve_top_domain_visibility</a>(\*\*<a href="src/keysso/types/report/simple_retrieve_top_domain_visibility_params.py">params</a>) -> <a href="./src/keysso/types/report/simple_retrieve_top_domain_visibility_response.py">SimpleRetrieveTopDomainVisibilityResponse</a></code>

### Organic

Types:

```python
from keysso.types.report.simple import (
    OrganicRetrieveAIAnswersResponse,
    OrganicRetrieveConcurentPagesResponse,
    OrganicRetrieveConcurentsResponse,
    OrganicRetrieveLostKeywordsResponse,
    OrganicRetrieveLostPagesResponse,
)
```

Methods:

- <code title="get /report/simple/organic/ai-answers">client.report.simple.organic.<a href="./src/keysso/resources/report/simple/organic/organic.py">retrieve_ai_answers</a>(\*\*<a href="src/keysso/types/report/simple/organic_retrieve_ai_answers_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/organic_retrieve_ai_answers_response.py">OrganicRetrieveAIAnswersResponse</a></code>
- <code title="get /report/simple/organic/concurent_pages">client.report.simple.organic.<a href="./src/keysso/resources/report/simple/organic/organic.py">retrieve_concurent_pages</a>(\*\*<a href="src/keysso/types/report/simple/organic_retrieve_concurent_pages_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/organic_retrieve_concurent_pages_response.py">OrganicRetrieveConcurentPagesResponse</a></code>
- <code title="get /report/simple/organic/concurents">client.report.simple.organic.<a href="./src/keysso/resources/report/simple/organic/organic.py">retrieve_concurents</a>(\*\*<a href="src/keysso/types/report/simple/organic_retrieve_concurents_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/organic_retrieve_concurents_response.py">OrganicRetrieveConcurentsResponse</a></code>
- <code title="get /report/simple/organic/lost_keywords">client.report.simple.organic.<a href="./src/keysso/resources/report/simple/organic/organic.py">retrieve_lost_keywords</a>(\*\*<a href="src/keysso/types/report/simple/organic_retrieve_lost_keywords_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/organic_retrieve_lost_keywords_response.py">OrganicRetrieveLostKeywordsResponse</a></code>
- <code title="get /report/simple/organic/lost_pages">client.report.simple.organic.<a href="./src/keysso/resources/report/simple/organic/organic.py">retrieve_lost_pages</a>(\*\*<a href="src/keysso/types/report/simple/organic_retrieve_lost_pages_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/organic_retrieve_lost_pages_response.py">OrganicRetrieveLostPagesResponse</a></code>

#### Sitepages

Types:

```python
from keysso.types.report.simple.organic import (
    SitepageListResponse,
    SitepageRetrieveWithkeysResponse,
)
```

Methods:

- <code title="get /report/simple/organic/sitepages">client.report.simple.organic.sitepages.<a href="./src/keysso/resources/report/simple/organic/sitepages.py">list</a>(\*\*<a href="src/keysso/types/report/simple/organic/sitepage_list_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/organic/sitepage_list_response.py">SitepageListResponse</a></code>
- <code title="get /report/simple/organic/sitepages/withkeys">client.report.simple.organic.sitepages.<a href="./src/keysso/resources/report/simple/organic/sitepages.py">retrieve_withkeys</a>(\*\*<a href="src/keysso/types/report/simple/organic/sitepage_retrieve_withkeys_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/organic/sitepage_retrieve_withkeys_response.py">SitepageRetrieveWithkeysResponse</a></code>

#### Keywords

Types:

```python
from keysso.types.report.simple.organic import KeywordListResponse, KeywordRetrieveBypageResponse
```

Methods:

- <code title="get /report/simple/organic/keywords">client.report.simple.organic.keywords.<a href="./src/keysso/resources/report/simple/organic/keywords.py">list</a>(\*\*<a href="src/keysso/types/report/simple/organic/keyword_list_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/organic/keyword_list_response.py">KeywordListResponse</a></code>
- <code title="get /report/simple/organic/keywords/bypage">client.report.simple.organic.keywords.<a href="./src/keysso/resources/report/simple/organic/keywords.py">retrieve_bypage</a>(\*\*<a href="src/keysso/types/report/simple/organic/keyword_retrieve_bypage_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/organic/keyword_retrieve_bypage_response.py">KeywordRetrieveBypageResponse</a></code>

### Context

Types:

```python
from keysso.types.report.simple import ContextRetrieveConcurentsResponse
```

Methods:

- <code title="get /report/simple/context/concurents">client.report.simple.context.<a href="./src/keysso/resources/report/simple/context/context.py">retrieve_concurents</a>(\*\*<a href="src/keysso/types/report/simple/context_retrieve_concurents_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/context_retrieve_concurents_response.py">ContextRetrieveConcurentsResponse</a></code>

#### Keywords

Types:

```python
from keysso.types.report.simple.context import KeywordListResponse, KeywordRetrieveByadsResponse
```

Methods:

- <code title="get /report/simple/context/keywords">client.report.simple.context.keywords.<a href="./src/keysso/resources/report/simple/context/keywords.py">list</a>(\*\*<a href="src/keysso/types/report/simple/context/keyword_list_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/context/keyword_list_response.py">KeywordListResponse</a></code>
- <code title="get /report/simple/context/keywords/byads">client.report.simple.context.keywords.<a href="./src/keysso/resources/report/simple/context/keywords.py">retrieve_byads</a>(\*\*<a href="src/keysso/types/report/simple/context/keyword_retrieve_byads_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/context/keyword_retrieve_byads_response.py">KeywordRetrieveByadsResponse</a></code>

#### Ads

Types:

```python
from keysso.types.report.simple.context import (
    AdRetrieveResponse,
    AdRetrieveFactsResponse,
    AdRetrieveLinksResponse,
)
```

Methods:

- <code title="get /report/simple/context/ads/">client.report.simple.context.ads.<a href="./src/keysso/resources/report/simple/context/ads.py">retrieve</a>(\*\*<a href="src/keysso/types/report/simple/context/ad_retrieve_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/context/ad_retrieve_response.py">AdRetrieveResponse</a></code>
- <code title="get /report/simple/context/ads/facts">client.report.simple.context.ads.<a href="./src/keysso/resources/report/simple/context/ads.py">retrieve_facts</a>(\*\*<a href="src/keysso/types/report/simple/context/ad_retrieve_facts_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/context/ad_retrieve_facts_response.py">AdRetrieveFactsResponse</a></code>
- <code title="get /report/simple/context/ads/links">client.report.simple.context.ads.<a href="./src/keysso/resources/report/simple/context/ads.py">retrieve_links</a>(\*\*<a href="src/keysso/types/report/simple/context/ad_retrieve_links_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/context/ad_retrieve_links_response.py">AdRetrieveLinksResponse</a></code>

### AIAnswers

Types:

```python
from keysso.types.report.simple import AIAnswerRetrieveStateResponse
```

Methods:

- <code title="get /report/simple/ai-answers/state">client.report.simple.ai_answers.<a href="./src/keysso/resources/report/simple/ai_answers.py">retrieve_state</a>(\*\*<a href="src/keysso/types/report/simple/ai_answer_retrieve_state_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/ai_answer_retrieve_state_response.py">AIAnswerRetrieveStateResponse</a></code>

### Links

Types:

```python
from keysso.types.report.simple import (
    LinkDomainsBatchResponse,
    LinkRetrieveBacklinksResponse,
    LinkRetrieveBacklinksAnchorResponse,
    LinkRetrieveBacklinksDomainsResponse,
    LinkRetrieveBacklinksDomainsViewDomainResponse,
    LinkRetrieveOutlinksResponse,
    LinkRetrieveOutlinksDomainsResponse,
    LinkRetrieveOutlinksDomainsViewDomainResponse,
    LinkRetrievePagesResponse,
)
```

Methods:

- <code title="post /report/simple/links/domains-batch">client.report.simple.links.<a href="./src/keysso/resources/report/simple/links/links.py">domains_batch</a>(\*\*<a href="src/keysso/types/report/simple/link_domains_batch_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/link_domains_batch_response.py">LinkDomainsBatchResponse</a></code>
- <code title="get /report/simple/links/backlinks">client.report.simple.links.<a href="./src/keysso/resources/report/simple/links/links.py">retrieve_backlinks</a>(\*\*<a href="src/keysso/types/report/simple/link_retrieve_backlinks_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/link_retrieve_backlinks_response.py">LinkRetrieveBacklinksResponse</a></code>
- <code title="get /report/simple/links/backlinks-anchor">client.report.simple.links.<a href="./src/keysso/resources/report/simple/links/links.py">retrieve_backlinks_anchor</a>(\*\*<a href="src/keysso/types/report/simple/link_retrieve_backlinks_anchor_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/link_retrieve_backlinks_anchor_response.py">LinkRetrieveBacklinksAnchorResponse</a></code>
- <code title="get /report/simple/links/backlinks-domains">client.report.simple.links.<a href="./src/keysso/resources/report/simple/links/links.py">retrieve_backlinks_domains</a>(\*\*<a href="src/keysso/types/report/simple/link_retrieve_backlinks_domains_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/link_retrieve_backlinks_domains_response.py">LinkRetrieveBacklinksDomainsResponse</a></code>
- <code title="get /report/simple/links/backlinks-domains?view=domain">client.report.simple.links.<a href="./src/keysso/resources/report/simple/links/links.py">retrieve_backlinks_domains_view_domain</a>(\*\*<a href="src/keysso/types/report/simple/link_retrieve_backlinks_domains_view_domain_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/link_retrieve_backlinks_domains_view_domain_response.py">LinkRetrieveBacklinksDomainsViewDomainResponse</a></code>
- <code title="get /report/simple/links/outlinks">client.report.simple.links.<a href="./src/keysso/resources/report/simple/links/links.py">retrieve_outlinks</a>(\*\*<a href="src/keysso/types/report/simple/link_retrieve_outlinks_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/link_retrieve_outlinks_response.py">LinkRetrieveOutlinksResponse</a></code>
- <code title="get /report/simple/links/outlinks-domains">client.report.simple.links.<a href="./src/keysso/resources/report/simple/links/links.py">retrieve_outlinks_domains</a>(\*\*<a href="src/keysso/types/report/simple/link_retrieve_outlinks_domains_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/link_retrieve_outlinks_domains_response.py">LinkRetrieveOutlinksDomainsResponse</a></code>
- <code title="get /report/simple/links/outlinks-domains?view=domain">client.report.simple.links.<a href="./src/keysso/resources/report/simple/links/links.py">retrieve_outlinks_domains_view_domain</a>(\*\*<a href="src/keysso/types/report/simple/link_retrieve_outlinks_domains_view_domain_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/link_retrieve_outlinks_domains_view_domain_response.py">LinkRetrieveOutlinksDomainsViewDomainResponse</a></code>
- <code title="get /report/simple/links/pages">client.report.simple.links.<a href="./src/keysso/resources/report/simple/links/links.py">retrieve_pages</a>(\*\*<a href="src/keysso/types/report/simple/link_retrieve_pages_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/link_retrieve_pages_response.py">LinkRetrievePagesResponse</a></code>

#### BacklinksIP

Types:

```python
from keysso.types.report.simple.links import (
    BacklinksIPRetrieveBacklinksIPResponse,
    BacklinksIPRetrieveSubnetResponse,
)
```

Methods:

- <code title="get /report/simple/links/backlinks-ip">client.report.simple.links.backlinks_ip.<a href="./src/keysso/resources/report/simple/links/backlinks_ip.py">retrieve_backlinks_ip</a>(\*\*<a href="src/keysso/types/report/simple/links/backlinks_ip_retrieve_backlinks_ip_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/links/backlinks_ip_retrieve_backlinks_ip_response.py">BacklinksIPRetrieveBacklinksIPResponse</a></code>
- <code title="get /report/simple/links/backlinks-ip/subnet">client.report.simple.links.backlinks_ip.<a href="./src/keysso/resources/report/simple/links/backlinks_ip.py">retrieve_subnet</a>(\*\*<a href="src/keysso/types/report/simple/links/backlinks_ip_retrieve_subnet_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/links/backlinks_ip_retrieve_subnet_response.py">BacklinksIPRetrieveSubnetResponse</a></code>

### Direct

Types:

```python
from keysso.types.report.simple import DirectRetrieveAdsResponse, DirectRetrieveDomainResponse
```

Methods:

- <code title="get /report/simple/direct/ads">client.report.simple.direct.<a href="./src/keysso/resources/report/simple/direct.py">retrieve_ads</a>(\*\*<a href="src/keysso/types/report/simple/direct_retrieve_ads_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/direct_retrieve_ads_response.py">DirectRetrieveAdsResponse</a></code>
- <code title="get /report/simple/direct/domain">client.report.simple.direct.<a href="./src/keysso/resources/report/simple/direct.py">retrieve_domain</a>(\*\*<a href="src/keysso/types/report/simple/direct_retrieve_domain_params.py">params</a>) -> <a href="./src/keysso/types/report/simple/direct_retrieve_domain_response.py">DirectRetrieveDomainResponse</a></code>

## Group

Types:

```python
from keysso.types.report import Base, GroupCreateResponse, GroupListResponse
```

Methods:

- <code title="post /report/group">client.report.group.<a href="./src/keysso/resources/report/group.py">create</a>(\*\*<a href="src/keysso/types/report/group_create_params.py">params</a>) -> <a href="./src/keysso/types/report/group_create_response.py">GroupCreateResponse</a></code>
- <code title="get /report/group/list">client.report.group.<a href="./src/keysso/resources/report/group.py">list</a>(\*\*<a href="src/keysso/types/report/group_list_params.py">params</a>) -> <a href="./src/keysso/types/report/group_list_response.py">GroupListResponse</a></code>

## Ads

### Rsya

Types:

```python
from keysso.types.report.ads import RsyaRetrieveResponse
```

Methods:

- <code title="get /report/ads/rsya">client.report.ads.rsya.<a href="./src/keysso/resources/report/ads/rsya.py">retrieve</a>(\*\*<a href="src/keysso/types/report/ads/rsya_retrieve_params.py">params</a>) -> <a href="./src/keysso/types/report/ads/rsya_retrieve_response.py">RsyaRetrieveResponse</a></code>

## Owner

Types:

```python
from keysso.types.report import OwnerRetrieveSubdomainsResponse
```

Methods:

- <code title="get /report/owner/subdomains">client.report.owner.<a href="./src/keysso/resources/report/owner.py">retrieve_subdomains</a>(\*\*<a href="src/keysso/types/report/owner_retrieve_subdomains_params.py">params</a>) -> <a href="./src/keysso/types/report/owner_retrieve_subdomains_response.py">OwnerRetrieveSubdomainsResponse</a></code>

# Tools

Types:

```python
from keysso.types import (
    ToolCheckTopResponse,
    ToolCheckTopConcurentsDomainsResponse,
    ToolCheckTopConcurentsURLsResponse,
    ToolCombineResponse,
    ToolCompareResponse,
    ToolCreateDomainsBatchResponse,
    ToolCreateHistorySerpResponse,
    ToolCreateUniqueResponse,
    ToolDeleteDoubleResponse,
    ToolListSiteThemesResponse,
    ToolSuggestResponse,
)
```

Methods:

- <code title="post /tools/check-top">client.tools.<a href="./src/keysso/resources/tools/tools.py">check_top</a>(\*\*<a href="src/keysso/types/tool_check_top_params.py">params</a>) -> <a href="./src/keysso/types/tool_check_top_response.py">ToolCheckTopResponse</a></code>
- <code title="post /tools/check-top-concurents-domains">client.tools.<a href="./src/keysso/resources/tools/tools.py">check_top_concurents_domains</a>(\*\*<a href="src/keysso/types/tool_check_top_concurents_domains_params.py">params</a>) -> <a href="./src/keysso/types/tool_check_top_concurents_domains_response.py">ToolCheckTopConcurentsDomainsResponse</a></code>
- <code title="post /tools/check-top-concurents-urls">client.tools.<a href="./src/keysso/resources/tools/tools.py">check_top_concurents_urls</a>(\*\*<a href="src/keysso/types/tool_check_top_concurents_urls_params.py">params</a>) -> <a href="./src/keysso/types/tool_check_top_concurents_urls_response.py">ToolCheckTopConcurentsURLsResponse</a></code>
- <code title="post /tools/combine">client.tools.<a href="./src/keysso/resources/tools/tools.py">combine</a>(\*\*<a href="src/keysso/types/tool_combine_params.py">params</a>) -> str</code>
- <code title="post /tools/compare">client.tools.<a href="./src/keysso/resources/tools/tools.py">compare</a>(\*\*<a href="src/keysso/types/tool_compare_params.py">params</a>) -> <a href="./src/keysso/types/tool_compare_response.py">ToolCompareResponse</a></code>
- <code title="post /tools/domains-batch">client.tools.<a href="./src/keysso/resources/tools/tools.py">create_domains_batch</a>(\*\*<a href="src/keysso/types/tool_create_domains_batch_params.py">params</a>) -> <a href="./src/keysso/types/tool_create_domains_batch_response.py">ToolCreateDomainsBatchResponse</a></code>
- <code title="post /tools/history-serp">client.tools.<a href="./src/keysso/resources/tools/tools.py">create_history_serp</a>(\*\*<a href="src/keysso/types/tool_create_history_serp_params.py">params</a>) -> <a href="./src/keysso/types/tool_create_history_serp_response.py">ToolCreateHistorySerpResponse</a></code>
- <code title="post /tools/unique">client.tools.<a href="./src/keysso/resources/tools/tools.py">create_unique</a>(\*\*<a href="src/keysso/types/tool_create_unique_params.py">params</a>) -> <a href="./src/keysso/types/tool_create_unique_response.py">ToolCreateUniqueResponse</a></code>
- <code title="post /tools/delete_double">client.tools.<a href="./src/keysso/resources/tools/tools.py">delete_double</a>(\*\*<a href="src/keysso/types/tool_delete_double_params.py">params</a>) -> <a href="./src/keysso/types/tool_delete_double_response.py">ToolDeleteDoubleResponse</a></code>
- <code title="get /tools/site-themes">client.tools.<a href="./src/keysso/resources/tools/tools.py">list_site_themes</a>(\*\*<a href="src/keysso/types/tool_list_site_themes_params.py">params</a>) -> <a href="./src/keysso/types/tool_list_site_themes_response.py">ToolListSiteThemesResponse</a></code>
- <code title="post /tools/suggest">client.tools.<a href="./src/keysso/resources/tools/tools.py">suggest</a>(\*\*<a href="src/keysso/types/tool_suggest_params.py">params</a>) -> <a href="./src/keysso/types/tool_suggest_response.py">ToolSuggestResponse</a></code>

## ExtendedKeywords

Types:

```python
from keysso.types.tools import ExtendedKeywordCreateResponse
```

Methods:

- <code title="post /tools/extended_keywords">client.tools.extended_keywords.<a href="./src/keysso/resources/tools/extended_keywords.py">create</a>(\*\*<a href="src/keysso/types/tools/extended_keyword_create_params.py">params</a>) -> <a href="./src/keysso/types/tools/extended_keyword_create_response.py">ExtendedKeywordCreateResponse</a></code>

## KeywordsByList

Types:

```python
from keysso.types.tools import KeywordsByListCreateResponse
```

Methods:

- <code title="post /tools/keywords_by_list">client.tools.keywords_by_list.<a href="./src/keysso/resources/tools/keywords_by_list.py">create</a>(\*\*<a href="src/keysso/types/tools/keywords_by_list_create_params.py">params</a>) -> <a href="./src/keysso/types/tools/keywords_by_list_create_response.py">KeywordsByListCreateResponse</a></code>

## ConcurentsByKeywords

Types:

```python
from keysso.types.tools import ConcurentsByKeywordCreateResponse
```

Methods:

- <code title="post /tools/concurents_by_keywords">client.tools.concurents_by_keywords.<a href="./src/keysso/resources/tools/concurents_by_keywords.py">create</a>(\*\*<a href="src/keysso/types/tools/concurents_by_keyword_create_params.py">params</a>) -> <a href="./src/keysso/types/tools/concurents_by_keyword_create_response.py">ConcurentsByKeywordCreateResponse</a></code>

## KeywordsByPages

Types:

```python
from keysso.types.tools import KeywordsByPageCreateResponse
```

Methods:

- <code title="post /tools/keywords_by_pages">client.tools.keywords_by_pages.<a href="./src/keysso/resources/tools/keywords_by_pages.py">create</a>(\*\*<a href="src/keysso/types/tools/keywords_by_page_create_params.py">params</a>) -> <a href="./src/keysso/types/tools/keywords_by_page_create_response.py">KeywordsByPageCreateResponse</a></code>

## DictionaryExtByPage

Types:

```python
from keysso.types.tools import DictionaryExtByPageCreateResponse
```

Methods:

- <code title="post /tools/dictionary-ext-by-page">client.tools.dictionary_ext_by_page.<a href="./src/keysso/resources/tools/dictionary_ext_by_page.py">create</a>(\*\*<a href="src/keysso/types/tools/dictionary_ext_by_page_create_params.py">params</a>) -> <a href="./src/keysso/types/tools/dictionary_ext_by_page_create_response.py">DictionaryExtByPageCreateResponse</a></code>

## DictionaryByPages

Types:

```python
from keysso.types.tools import DictionaryByPageCreateResponse
```

Methods:

- <code title="post /tools/dictionary-by-pages">client.tools.dictionary_by_pages.<a href="./src/keysso/resources/tools/dictionary_by_pages.py">create</a>(\*\*<a href="src/keysso/types/tools/dictionary_by_page_create_params.py">params</a>) -> <a href="./src/keysso/types/tools/dictionary_by_page_create_response.py">DictionaryByPageCreateResponse</a></code>

# Clustering

Types:

```python
from keysso.types import ClusteringCreateResponse, ClusteringListResponse
```

Methods:

- <code title="post /clustering">client.clustering.<a href="./src/keysso/resources/clustering.py">create</a>(\*\*<a href="src/keysso/types/clustering_create_params.py">params</a>) -> <a href="./src/keysso/types/clustering_create_response.py">ClusteringCreateResponse</a></code>
- <code title="get /clustering/list">client.clustering.<a href="./src/keysso/resources/clustering.py">list</a>(\*\*<a href="src/keysso/types/clustering_list_params.py">params</a>) -> <a href="./src/keysso/types/clustering_list_response.py">ClusteringListResponse</a></code>

## Uid

Types:

```python
from keysso.types.clustering import Items
```

# Projects

Types:

```python
from keysso.types import (
    ProjectCreateResponse,
    ProjectListResponse,
    ProjectDeleteResponse,
    ProjectGetRecommendedCompetitorsResponse,
)
```

Methods:

- <code title="post /projects">client.projects.<a href="./src/keysso/resources/projects/projects.py">create</a>(\*\*<a href="src/keysso/types/project_create_params.py">params</a>) -> <a href="./src/keysso/types/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="get /projects">client.projects.<a href="./src/keysso/resources/projects/projects.py">list</a>() -> <a href="./src/keysso/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="post /projects/delete">client.projects.<a href="./src/keysso/resources/projects/projects.py">delete</a>(\*\*<a href="src/keysso/types/project_delete_params.py">params</a>) -> <a href="./src/keysso/types/project_delete_response.py">ProjectDeleteResponse</a></code>
- <code title="get /projects/recommended-competitors">client.projects.<a href="./src/keysso/resources/projects/projects.py">get_recommended_competitors</a>(\*\*<a href="src/keysso/types/project_get_recommended_competitors_params.py">params</a>) -> <a href="./src/keysso/types/project_get_recommended_competitors_response.py">ProjectGetRecommendedCompetitorsResponse</a></code>

## Competitors

Types:

```python
from keysso.types.projects import CompetitorListResponse, CompetitorCompareResponse
```

Methods:

- <code title="get /projects/competitors">client.projects.competitors.<a href="./src/keysso/resources/projects/competitors.py">list</a>(\*\*<a href="src/keysso/types/projects/competitor_list_params.py">params</a>) -> <a href="./src/keysso/types/projects/competitor_list_response.py">CompetitorListResponse</a></code>
- <code title="post /projects/competitors/compare">client.projects.competitors.<a href="./src/keysso/resources/projects/competitors.py">compare</a>(\*\*<a href="src/keysso/types/projects/competitor_compare_params.py">params</a>) -> <a href="./src/keysso/types/projects/competitor_compare_response.py">CompetitorCompareResponse</a></code>

# Robots

Types:

```python
from keysso.types import RobotListDatesResponse, RobotRetrieveDataResponse
```

Methods:

- <code title="get /robots/dates">client.robots.<a href="./src/keysso/resources/robots.py">list_dates</a>(\*\*<a href="src/keysso/types/robot_list_dates_params.py">params</a>) -> <a href="./src/keysso/types/robot_list_dates_response.py">RobotListDatesResponse</a></code>
- <code title="get /robots/data">client.robots.<a href="./src/keysso/resources/robots.py">retrieve_data</a>(\*\*<a href="src/keysso/types/robot_retrieve_data_params.py">params</a>) -> <a href="./src/keysso/types/robot_retrieve_data_response.py">RobotRetrieveDataResponse</a></code>

# Wordstat

Types:

```python
from keysso.types import (
    TypeBase,
    WordstatListResponse,
    WordstatCreateProjectResponse,
    WordstatDeleteProjectResponse,
    WordstatDeleteWordsResponse,
    WordstatGetProjectStatusResponse,
    WordstatGetProjectsCompletedResponse,
    WordstatReportResponse,
)
```

Methods:

- <code title="get /wordstat/list">client.wordstat.<a href="./src/keysso/resources/wordstat.py">list</a>(\*\*<a href="src/keysso/types/wordstat_list_params.py">params</a>) -> <a href="./src/keysso/types/wordstat_list_response.py">WordstatListResponse</a></code>
- <code title="post /wordstat/create-project">client.wordstat.<a href="./src/keysso/resources/wordstat.py">create_project</a>(\*\*<a href="src/keysso/types/wordstat_create_project_params.py">params</a>) -> <a href="./src/keysso/types/wordstat_create_project_response.py">WordstatCreateProjectResponse</a></code>
- <code title="delete /wordstat/delete-project">client.wordstat.<a href="./src/keysso/resources/wordstat.py">delete_project</a>(\*\*<a href="src/keysso/types/wordstat_delete_project_params.py">params</a>) -> <a href="./src/keysso/types/wordstat_delete_project_response.py">WordstatDeleteProjectResponse</a></code>
- <code title="delete /wordstat/delete-words">client.wordstat.<a href="./src/keysso/resources/wordstat.py">delete_words</a>(\*\*<a href="src/keysso/types/wordstat_delete_words_params.py">params</a>) -> <a href="./src/keysso/types/wordstat_delete_words_response.py">WordstatDeleteWordsResponse</a></code>
- <code title="get /wordstat/get-project-status">client.wordstat.<a href="./src/keysso/resources/wordstat.py">get_project_status</a>(\*\*<a href="src/keysso/types/wordstat_get_project_status_params.py">params</a>) -> <a href="./src/keysso/types/wordstat_get_project_status_response.py">WordstatGetProjectStatusResponse</a></code>
- <code title="get /wordstat/get-projects-completed">client.wordstat.<a href="./src/keysso/resources/wordstat.py">get_projects_completed</a>(\*\*<a href="src/keysso/types/wordstat_get_projects_completed_params.py">params</a>) -> <a href="./src/keysso/types/wordstat_get_projects_completed_response.py">WordstatGetProjectsCompletedResponse</a></code>
- <code title="get /wordstat/report">client.wordstat.<a href="./src/keysso/resources/wordstat.py">report</a>(\*\*<a href="src/keysso/types/wordstat_report_params.py">params</a>) -> <a href="./src/keysso/types/wordstat_report_response.py">WordstatReportResponse</a></code>

## ID

Types:

```python
from keysso.types.wordstat import Item
```

# Serp

Types:

```python
from keysso.types import Engine, SerpCreateResponse, SerpListResponse
```

Methods:

- <code title="post /serp">client.serp.<a href="./src/keysso/resources/serp.py">create</a>(\*\*<a href="src/keysso/types/serp_create_params.py">params</a>) -> <a href="./src/keysso/types/serp_create_response.py">SerpCreateResponse</a></code>
- <code title="get /serp">client.serp.<a href="./src/keysso/resources/serp.py">list</a>(\*\*<a href="src/keysso/types/serp_list_params.py">params</a>) -> <a href="./src/keysso/types/serp_list_response.py">SerpListResponse</a></code>

## ID

Types:

```python
from keysso.types.serp import SerpType
```

# Zen

Types:

```python
from keysso.types import ZenRetrieveDashboardResponse
```

Methods:

- <code title="get /zen/dashboard">client.zen.<a href="./src/keysso/resources/zen/zen.py">retrieve_dashboard</a>(\*\*<a href="src/keysso/types/zen_retrieve_dashboard_params.py">params</a>) -> <a href="./src/keysso/types/zen_retrieve_dashboard_response.py">ZenRetrieveDashboardResponse</a></code>

## Top

Types:

```python
from keysso.types.zen import TopListChannelsResponse
```

Methods:

- <code title="get /zen/top/channels">client.zen.top.<a href="./src/keysso/resources/zen/top.py">list_channels</a>(\*\*<a href="src/keysso/types/zen/top_list_channels_params.py">params</a>) -> <a href="./src/keysso/types/zen/top_list_channels_response.py">TopListChannelsResponse</a></code>

## Channel

Types:

```python
from keysso.types.zen import ChannelListPublicationsResponse
```

Methods:

- <code title="get /zen/channel/publications">client.zen.channel.<a href="./src/keysso/resources/zen/channel/channel.py">list_publications</a>(\*\*<a href="src/keysso/types/zen/channel_list_publications_params.py">params</a>) -> <a href="./src/keysso/types/zen/channel_list_publications_response.py">ChannelListPublicationsResponse</a></code>

### New

#### Top

Types:

```python
from keysso.types.zen.channel.new import TopListPublicationsResponse
```

Methods:

- <code title="get /zen/channel/new/top/publications">client.zen.channel.new.top.<a href="./src/keysso/resources/zen/channel/new/top.py">list_publications</a>(\*\*<a href="src/keysso/types/zen/channel/new/top_list_publications_params.py">params</a>) -> <a href="./src/keysso/types/zen/channel/new/top_list_publications_response.py">TopListPublicationsResponse</a></code>

# Limits

Types:

```python
from keysso.types import LimitListResponse
```

Methods:

- <code title="get /limits/all">client.limits.<a href="./src/keysso/resources/limits.py">list</a>() -> <a href="./src/keysso/types/limit_list_response.py">LimitListResponse</a></code>

# Monitoring

Types:

```python
from keysso.types import (
    AlertSetting,
    SchedulerSetting,
    SearchSetting,
    MonitoringCreateResponse,
    MonitoringListResponse,
    MonitoringGetStateResponse,
)
```

Methods:

- <code title="post /monitoring">client.monitoring.<a href="./src/keysso/resources/monitoring.py">create</a>(\*\*<a href="src/keysso/types/monitoring_create_params.py">params</a>) -> <a href="./src/keysso/types/monitoring_create_response.py">MonitoringCreateResponse</a></code>
- <code title="get /monitoring">client.monitoring.<a href="./src/keysso/resources/monitoring.py">list</a>(\*\*<a href="src/keysso/types/monitoring_list_params.py">params</a>) -> <a href="./src/keysso/types/monitoring_list_response.py">MonitoringListResponse</a></code>
- <code title="get /monitoring/state">client.monitoring.<a href="./src/keysso/resources/monitoring.py">get_state</a>(\*\*<a href="src/keysso/types/monitoring_get_state_params.py">params</a>) -> <a href="./src/keysso/types/monitoring_get_state_response.py">MonitoringGetStateResponse</a></code>

# AITracker

Types:

```python
from keysso.types import (
    SystemItem,
    AITrackerCreateResponse,
    AITrackerListResponse,
    AITrackerGetStateResponse,
)
```

Methods:

- <code title="post /ai_tracker">client.ai_tracker.<a href="./src/keysso/resources/ai_tracker.py">create</a>(\*\*<a href="src/keysso/types/ai_tracker_create_params.py">params</a>) -> <a href="./src/keysso/types/ai_tracker_create_response.py">AITrackerCreateResponse</a></code>
- <code title="get /ai_tracker">client.ai_tracker.<a href="./src/keysso/resources/ai_tracker.py">list</a>(\*\*<a href="src/keysso/types/ai_tracker_list_params.py">params</a>) -> <a href="./src/keysso/types/ai_tracker_list_response.py">AITrackerListResponse</a></code>
- <code title="get /ai_tracker/state">client.ai_tracker.<a href="./src/keysso/resources/ai_tracker.py">get_state</a>(\*\*<a href="src/keysso/types/ai_tracker_get_state_params.py">params</a>) -> <a href="./src/keysso/types/ai_tracker_get_state_response.py">AITrackerGetStateResponse</a></code>

## ID

Types:

```python
from keysso.types.ai_tracker import Reference, ReferenceDataItem, System
```
