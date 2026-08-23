# Architecture

> **Original creator, project owner, and primary maintainer: Chris Cruz | h4ckd4d**

The Atlas separates **defensive intent** from **vendor syntax** so analysts can reason about what they are trying to learn before choosing a platform-specific representation.

## Pipeline

```text
Authorization Reference
        ↓
Scope Definition
        ↓
Query Intent
        ↓
Semantic Validation
        ↓
Vendor Adapter
        ↓
Platform Query / Field Mapping
        ↓
Analyst Review
        ↓
Exposure Observation
        ↓
Attribution / Validation
```

## Trust boundaries

### Intent layer

Describes the defensive objective without vendor syntax. Examples include authorized HTTPS inventory, certificate review, or known-network service inventory.

### Adapter layer

Translates only the semantics that can be validated for a platform. An adapter may support an intent fully, partially, or not at all.

### Analyst layer

Reviews the generated representation, account/plan constraints, result freshness, ownership confidence, and vendor-specific semantics before drawing a conclusion.

## Translation confidence

Adapters use three confidence states:

- `validated` — syntax/semantics confirmed from current primary documentation;
- `partial` — some fields are confirmed but the intent cannot be translated completely;
- `experimental` — documentation is incomplete or semantics require further validation.

The project must prefer `partial` or `experimental` over pretending two vendors are equivalent.

## Safety model

The Atlas does not execute scans, authenticate to services, or test third-party systems. Query examples are restricted to reserved IP ranges, `example.com`, fictional organizations, or explicit authorized scope.

---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
