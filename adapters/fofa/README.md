# FOFA Adapter

> **Original creator, project owner, and primary maintainer: Chris Cruz | h4ckd4d**

**Adapter confidence:** `partial`.

FOFA supports field-oriented search expressions. This adapter intentionally documents only conservative syntax that can be cross-checked against the current FOFA interface/API pages and avoids claiming equivalence for fields that are plan-dependent or insufficiently documented.

## Documentation-safe representation

For the Atlas intent `H4D-QRY-0001`:

```text
ip="203.0.113.0/24" && port="443"
```

The Atlas deliberately does **not** add a TLS-equivalence field to this v1 translation. The intent therefore remains `partial` rather than pretending the FOFA expression is semantically identical to the Shodan representation.

## Semantic notes

- field availability and query permissions can depend on FOFA account level;
- query syntax and data normalization are vendor-specific;
- a match does not prove ownership, vulnerability, or current exposure;
- reserved/example scope should be used in repository documentation;
- operational use requires explicit authorization.

## Primary references

- https://en.fofa.info/api
- https://en.fofa.info/api/introd

Reviewed: **2026-08-23**.

---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
