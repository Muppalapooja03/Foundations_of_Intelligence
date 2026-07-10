Day 7 – Advanced Google Dorking
Analyst

Pooja M

Target

Pixxel (https://pixxel.space)

Objective

To perform an Advanced Google Dorking investigation on Pixxel using Google search operators to identify publicly indexed information, evaluate the organization's search-engine exposure, and gather intelligence through passive Open-Source Intelligence (OSINT) techniques without interacting with protected resources.

Queries Used and Analyst Observations
Query 1

Search Query

site:pixxel.space

Purpose

To identify all publicly indexed pages belonging to Pixxel's official website.

Analyst Observation

Google returned approximately 18 indexed results from the pixxel.space domain. The top results included the official homepage, About Pixxel, and Team pages. The search results describe Pixxel as a space data company and spacecraft manufacturer specializing in high-resolution hyperspectral imaging and Earth observation.

Query 2

Search Query

site:pixxel.space intitle:careers

Purpose

To identify career or recruitment pages indexed by Google.

Analyst Observation

The query returned about one search result, but no official Pixxel Careers page appeared in the results. Instead, Google mainly displayed advertisements from third-party job portals. Based on the observed results, no official career page matching this query was indexed.

Query 3

Search Query

site:pixxel.space "hyperspectral"

Purpose

To identify pages related to Pixxel's hyperspectral imaging technology.

Analyst Observation

Google returned approximately 69 search results. The indexed pages included the official homepage, World's Highest-Resolution Hyperspectral Satellite Imagery, and Pixxel Hyperspectral Academy. These results indicate that Pixxel actively publishes information about its hyperspectral imaging technology and educational resources.

Query 4

Search Query

site:pixxel.space inurl:news

Purpose

To identify publicly indexed news or announcement pages.

Analyst Observation

No search results were returned for this query. This indicates that no pages containing "news" in the URL were indexed by Google at the time of the investigation.

Query 5

Search Query

site:pixxel.space filetype:pdf

Purpose

To identify publicly indexed PDF documents.

Analyst Observation

No PDF documents from the pixxel.space domain were found in Google's index during the investigation.

Query 6

Search Query

site:pixxel.space intitle:"index of"

Purpose

To check for publicly accessible directory listings.

Analyst Observation

No indexed directory listings were identified through Google Search.

Query 7

Search Query

site:pixxel.space inurl:login

Purpose

To identify publicly indexed login pages.

Analyst Observation

No publicly indexed login pages were found during the investigation.

Query 8

Search Query

related:pixxel.space

Purpose

To identify websites or pages that Google considers related to Pixxel.

Analyst Observation

Google returned Pixxel's official pages along with related resources such as Wikipedia. The results also displayed shortcuts to Pixxel's Contact and Blogs sections, providing additional publicly accessible information about the organization.

High-Confidence Findings
Approximately 18 pages from the Pixxel website are indexed by Google.
Pixxel's homepage, About page, and Team page are publicly searchable.
Information related to hyperspectral imaging is extensively indexed, with around 69 search results.
No publicly indexed PDF documents were identified.
No publicly indexed directory listings were observed.
No publicly indexed login pages were found.
No pages containing "news" in the URL were indexed during this investigation.
Inferred Findings
Pixxel's public search presence mainly focuses on its technology, company information, and educational content.
Google indexing appears to prioritize official informational pages rather than downloadable documents.
No evidence of sensitive resources or administrative pages being publicly indexed was observed during the investigation.
The organization's indexed content appears to be intentionally published for public visibility.
Investigation Scope and Ethical Considerations

This investigation was conducted using passive OSINT techniques only.

The following activities were intentionally excluded:

No login attempts were performed.
No interaction with authentication portals.
No vulnerability scanning or exploitation.
No access to restricted or private resources.
No attempts were made to bypass security controls.

Only information indexed by Google Search was analyzed.

Analyst Assessment

The Advanced Google Dorking investigation indicates that Pixxel maintains a controlled public web presence. Google's indexed results primarily consist of official company information and technical resources related to hyperspectral imaging. Queries targeting sensitive resources such as login pages, directory listings, and PDF documents did not return results, suggesting that these resources are not publicly indexed through Google.

Conclusion

The Advanced Google Dorking assessment successfully identified Pixxel's publicly indexed web presence while remaining within ethical OSINT boundaries. The investigation found that the organization's search visibility is focused on official company information and hyperspectral imaging technology. No evidence of publicly indexed sensitive resources, including login pages, directory listings, or PDF documents, was observed during this investigation.
