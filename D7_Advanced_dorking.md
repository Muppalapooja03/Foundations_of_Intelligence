# Day 7 – Advanced Google Dorking

## Analyst

Pooja M

## Target

**Pixxel** (https://pixxel.space)

## Objective

To perform an advanced Google Dorking investigation on Pixxel using chained Google search operators to identify publicly indexed information, assess search-engine exposure, and gather intelligence through passive Open-Source Intelligence (OSINT) techniques without interacting with protected resources.

---

# Queries Used and Analyst Observations

### Query 1

**Search Query**

```text
site:pixxel.space filetype:pdf
```

**Purpose**
To identify publicly available PDF documents such as brochures, whitepapers, presentations, or reports.

**Analyst Observation**
Google indexed official PDF documents related to Pixxel's products and company information. No confidential documents were observed.

---

### Query 2

**Search Query**

```text
site:pixxel.space filetype:pdf intitle:hyperspectral
```

**Purpose**
To locate technical documents related to Pixxel's hyperspectral imaging technology.

**Analyst Observation**
Technical resources describing hyperspectral imaging and Earth observation were publicly available, supporting the company's research and product information.

---

### Query 3

**Search Query**

```text
site:pixxel.space intitle:careers
```

**Purpose**
To identify recruitment or career-related pages.

**Analyst Observation**
Official career pages were indexed, providing information about current opportunities and company growth.

---

### Query 4

**Search Query**

```text
site:pixxel.space inurl:login
```

**Purpose**
To identify publicly indexed login portals.

**Analyst Observation**
No publicly indexed login portals of concern were observed. Any authentication pages appeared to be intended for legitimate users.

---

### Query 5

**Search Query**

```text
site:pixxel.space intitle:"index of"
```

**Purpose**
To check for publicly accessible directory listings.

**Analyst Observation**
No indexed directory listings were identified, indicating that directory browsing is likely disabled or properly restricted.

---

### Query 6

**Search Query**

```text
site:pixxel.space filetype:env
```

**Purpose**
To determine whether configuration files were accidentally indexed.

**Analyst Observation**
No exposed configuration or environment files were discovered during the search.

---

### Query 7

**Search Query**

```text
cache:pixxel.space
```

**Purpose**
To review Google's cached version of the official website.

**Analyst Observation**
Google cache reflected previously indexed versions of the website where available. No unusual or sensitive information was observed.

---

### Query 8

**Search Query**

```text
related:pixxel.space
```

**Purpose**
To identify organizations and websites operating in similar domains.

**Analyst Observation**
Google returned organizations related to satellite imaging, geospatial technology, and Earth observation, confirming Pixxel's industry position.

---

# High-Confidence Findings

* Official Pixxel documents are publicly indexed.
* Product and technology information is accessible through search engines.
* Career-related information is publicly available.
* No exposed directory listings were observed.
* No configuration files were found through Google indexing.

---

# Inferred Findings

* Pixxel maintains a controlled public web presence.
* Publicly indexed information appears to be intentionally published for customers, partners, and researchers.
* Sensitive files and internal resources are not exposed through Google's search index.
* The organization's search-engine visibility supports transparency while maintaining good security practices.

---

# Investigation Scope and Ethical Considerations

This investigation followed passive OSINT principles.

The following activities were intentionally excluded:

* No login attempts were performed.
* No interaction with authentication portals.
* No vulnerability scanning or exploitation.
* No access to non-public resources.
* No attempts were made to bypass security controls.

Only publicly indexed information available through Google Search was analyzed.

---

# Analyst Assessment

The advanced Google Dorking assessment indicates that Pixxel maintains a well-managed digital footprint. Publicly indexed resources primarily include official documentation, company information, technology-related content, and recruitment pages. No evidence of exposed configuration files, directory listings, or sensitive information was identified through search-engine indexing.

---

# Conclusion

Advanced Google Dorking provided valuable insights into Pixxel's public search-engine presence while remaining within ethical OSINT boundaries. The investigation confirms that the organization effectively manages its publicly accessible information, with no significant exposure of sensitive resources observed through Google indexing. This reflects good information management and responsible security practices.
