# BinaryEdge Adapter

> **Original creator, project owner, and primary maintainer: Chris Cruz | h4ckd4d**

**Adapter confidence:** `experimental`.

BinaryEdge publishes detailed documentation for data schemas, sensors, and scanning modules. The Atlas does not currently have enough primary-source evidence to claim that a stable executable search expression is semantically equivalent to the Shodan/FOFA representations used by `H4D-QRY-0001`.

## v1 behavior

The adapter therefore publishes **no executable translation** for the initial HTTPS-inventory intent.

```text
UNPUBLISHED: stable cross-platform search translation requires additional primary-source validation
```

This is intentional. A professional query atlas should expose uncertainty rather than manufacture parity between vendors.

## What is validated

BinaryEdge documentation clearly exposes structured network/security data and module schemas, including target IP/port/protocol fields and service-specific result structures. Those semantics are useful for future normalization work, but they are not automatically equivalent to a portal search-language filter.

## Contribution opportunity

Developers familiar with current BinaryEdge search/API capabilities are invited to contribute a primary-source-validated adapter through a pull request. See `DEVELOPERS.md` and `docs/query-standard.md`.

## Primary reference

- https://docs.binaryedge.io/

Reviewed: **2026-08-23**.

---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
