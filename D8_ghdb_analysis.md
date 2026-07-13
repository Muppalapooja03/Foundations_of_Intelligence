# Day 8 – GHDB Analysis 
**Date:** 11 July 2026  

This analysis explores 10 Google Dorks from the Google Hacking Database (GHDB), categorized across multiple investigation areas. 
Each entry explains the query, its category, what it reveals, and the real-world risk it represents. 
All examples are tested safely on public scopes without unauthorized probing.

---

## Dork 1
- **Query:** `site:gov.in filetype:pdf`
- **Category:** Files
- **What it reveals:** Publicly available government PDF documents.
- **Risk:** May expose sensitive reports, citizen data, or internal policies unintentionally published.

---

## Dork 2
- **Query:** `intitle:"index of" admin`
- **Category:** Directories
- **What it reveals:** Exposed directory listings containing administrative files.
- **Risk:** Attackers could browse restricted files or configuration data.

---

## Dork 3
- **Query:** `inurl:login`
- **Category:** Login Portals
- **What it reveals:** Publicly accessible login pages.
- **Risk:** Targets for brute force or credential stuffing attacks.

---

## Dork 4
- **Query:** `"SQL syntax error" filetype:log`
- **Category:** Error Messages
- **What it reveals:** Logs containing SQL error messages.
- **Risk:** Indicates possible SQL injection vulnerabilities.

---

## Dork 5
- **Query:** `filetype:xls inurl:"contacts"`
- **Category:** Sensitive Information
- **What it reveals:** Excel files containing contact lists.
- **Risk:** Leakage of personal or organizational data.

---

## Dork 6
- **Query:** `intitle:"phpMyAdmin" "Welcome to"`
- **Category:** Vulnerable Servers
- **What it reveals:** Publicly exposed phpMyAdmin interfaces.
- **Risk:** Could allow attackers to manipulate databases if not secured.

---

## Dork 7
- **Query:** `inurl:/config.php`
- **Category:** Configuration Files
- **What it reveals:** Configuration files indexed by search engines.
- **Risk:** May expose database credentials or API keys.

---

## Dork 8
- **Query:** `filetype:docx "confidential"`
- **Category:** Files
- **What it reveals:** Word documents containing the keyword “confidential.”
- **Risk:** Disclosure of sensitive internal communications.

---

## Dork 9
- **Query:** `intitle:"Dashboard" inurl:admin`
- **Category:** Login Portals
- **What it reveals:** Administrative dashboards.
- **Risk:** Could expose control panels to unauthorized access attempts.

---

## Dork 10
- **Query:** `"Index of /backup"`
- **Category:** Directories
- **What it reveals:** Backup directories exposed to the public.
- **Risk:** May contain sensitive archives, databases, or system snapshots.

---

# Analysis
These 10 dorks demonstrate how GHDB categorizes queries into **Files, Directories, Login Portals, Error Messages, Sensitive Information, and Vulnerable Servers**. Each query highlights the potential risks of improperly managed digital footprints.  

- **Files**: Risk of leaking confidential documents.  
- **Directories**: Risk of exposing internal structures or backups.  
- **Login Portals**: Risk of brute force or credential attacks.  
- **Error Messages**: Risk of revealing exploitable vulnerabilities.  
- **Sensitive Info**: Risk of privacy violations.  
- **Vulnerable Servers**: Risk of direct exploitation.  

---

# Conclusion
The GHDB provides a structured way to understand how search engines index content and how attackers might exploit misconfigurations. By testing these dorks safely, analysts gain awareness of real-world risks and help organizations strengthen their security posture.

---

# References
- Official [Google Hacking Database (GHDB)](https://www.exploit-db.com/google-hacking-database)  
- [Google Search Operators Documentation](https://support.google.com/websearch/answer/2466433)  
- Open Source Intelligence (OSINT) Methodology – industry best practices and frameworks
