# Vendor Semantics

> **Original creator, project owner, and primary maintainer: Chris Cruz | h4ckd4d**

Internet-exposure platforms collect, normalize, and expose data differently. The Atlas therefore treats vendor translation as a semantic mapping problem rather than a string-conversion problem.

## Confidence states

### Validated

Use only when the relevant syntax and field meaning are confirmed from current primary documentation.

### Partial

Use when some required fields are confirmed but the full intent cannot be represented faithfully.

### Experimental

Use when public documentation is incomplete, plan-dependent, or ambiguous enough that the project should not claim a stable translation.

## Current adapter posture

| Platform | Initial posture | Notes |
| --- | --- | --- |
| Shodan | Validated core | Official search syntax uses `filter:value`; current filters can be retrieved through the API. |
| FOFA | Partial | Basic documented/search-interface fields can be represented conservatively; plan-specific syntax must be noted. |
| BinaryEdge | Experimental | Public documentation strongly documents data schemas and scanning modules, while a stable cross-platform search-query translation requires additional validation. |

## Review rule

A vendor adapter may become more restrictive when documentation changes. Backward compatibility is less important than avoiding false claims about query semantics.

## Primary-source policy

Prefer vendor-owned documentation, API references, schemas, and maintained specifications. Secondary blog posts can provide context but should not be the sole source for a production adapter.

---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
