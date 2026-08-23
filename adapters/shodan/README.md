# Shodan Adapter

> **Original creator, project owner, and primary maintainer: Chris Cruz | h4ckd4d**

**Adapter confidence:** `validated` for the core syntax documented here.

Shodan search filters use the form:

```text
filter:value
```

Values containing spaces should be quoted. Multiple filters can be combined to narrow results.

## Documentation-safe representation

For the Atlas intent `H4D-QRY-0001`:

```text
net:"203.0.113.0/24" port:443 has_ssl:true
```

This is a documentation-only network from RFC 5737 and is not a real operational target.

## Validation mechanisms

Shodan exposes API methods that are useful for maintaining this adapter:

- `/shodan/host/search/filters` — current search filters;
- `/shodan/host/search/tokens` — query tokenization;
- `/shodan/host/count` — result counts without host results;
- `/shodan/host/search` — banner search.

## Semantic notes

- a Shodan result is an observation, not proof of current ownership;
- `has_ssl:true` indicates indexed SSL/TLS-related data, not a security-quality judgment;
- telemetry can become stale;
- cloud/CDN/shared infrastructure can complicate attribution;
- public visibility does not grant permission to interact with a service.

## Primary references

- https://help.shodan.io/the-basics/search-query-fundamentals
- https://developer.shodan.io/api
- https://trends.shodan.io/search/filters

Reviewed: **2026-08-23**.

---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
