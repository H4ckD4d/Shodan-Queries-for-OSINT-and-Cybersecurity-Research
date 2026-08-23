# h4ckd4d Internet Exposure Query Atlas

> **Original creator, project owner, and primary maintainer: Chris Cruz | h4ckd4d**

**h4ckd4d Internet Exposure Query Atlas** is a defensive, vendor-aware query-intelligence project for translating an authorized Internet-exposure research objective into documented query patterns for public Internet search platforms.

The project is designed to complement **h4ckd4d Internet Exposure Intelligence** and **h4ckd4d Detection Engineering** by creating a portable, analyst-readable layer between defensive research intent and platform-specific query syntax.

> **Authorized use only:** Query examples must be limited to assets you own, administer, or are explicitly authorized to assess. Documentation-safe examples use reserved domains, reserved IP ranges, or fictional organizations.

## Core idea

```text
Defensive Research Objective
          ↓
Authorized Scope
          ↓
Vendor-Neutral Query Intent
          ↓
Query Translation
          ↓
┌─────────┼──────────┬────────────┐
│         │          │            │
Shodan   FOFA    BinaryEdge    Future adapters
│         │          │            │
└─────────┼──────────┴────────────┘
          ↓
Analyst Review
          ↓
Normalized Exposure Context
```

The Atlas does **not** treat equivalent-looking vendor filters as semantically identical. Every adapter must document differences, limitations, plan/API requirements, and confidence in the translation.

## Initial platform tracks

- **Shodan** — Internet service and banner telemetry.
- **FOFA** — Internet asset and fingerprint search syntax.
- **BinaryEdge** — Internet exposure and service intelligence syntax.
- **Future adapters** — additional platforms only after their syntax and terms can be validated from primary documentation.

## Professional query standard

Every maintained query pattern should document:

1. Defensive objective.
2. Authorized scope requirement.
3. Vendor-neutral intent.
4. Platform-specific syntax.
5. Filters or fields used.
6. Expected result.
7. What the query does **not** prove.
8. Known semantic differences across vendors.
9. False-positive / attribution considerations.
10. Validation source and review date.

## Repository roadmap

```text
README.md
DEVELOPERS.md
CONTRIBUTING.md
SECURITY.md
CHANGELOG.md
LICENSE

docs/
├── architecture.md
├── query-standard.md
├── scope-and-authorization.md
└── vendor-semantics.md

intents/
├── asset-inventory/
├── web-services/
├── tls-certificates/
├── cloud-inventory/
└── remote-access/

adapters/
├── shodan/
├── fofa/
└── binaryedge/

schemas/
└── query-intent.schema.json

catalog/
└── query-catalog.json

scripts/
└── validate_catalog.py
```

## Example intent

```yaml
id: H4D-QRY-0001
objective: authorized_https_inventory
scope_required: true
constraints:
  port: 443
  tls: true
```

A platform adapter can then document a safe representation using a fictional organization or documentation-only network.

## Design principles

- authorization before discovery;
- no real third-party targets in examples;
- platform syntax validated against primary sources;
- semantics documented, not guessed;
- attribution is separate from observation;
- observation is separate from finding;
- no exploitation or authentication workflow;
- reproducible examples and machine-readable metadata;
- analyst review before any security conclusion.

## Developers wanted

**Developers, OSINT researchers, EASM practitioners, security engineers, technical writers, and maintainers of Internet-intelligence tooling are invited to help build the Atlas professionally.**

High-value contributions include:

- validating vendor syntax against official documentation;
- documenting semantic differences between platforms;
- adding defensive query intents;
- building schemas and static validation tooling;
- creating documentation-safe examples;
- improving adapters, tests, CI, and analyst documentation;
- reviewing false-positive and attribution risks.

Accepted contributors receive credit through Git history, pull requests, release notes, and acknowledgments where appropriate. **Original authorship, project ownership, and primary maintenance remain attributed to Chris Cruz | h4ckd4d.**

## Project ecosystem

The intended Project h4ckd4d defensive engineering stack is:

```text
Internet Exposure Query Atlas
            ↓
Internet Exposure Intelligence / EASM / OSINT / CTI
            ↓
Detection Engineering / SOC / Blue Team
            ↓
Protect. Detect. Defend.
```

## License

The project will be maintained as an open collaboration with clear attribution and responsible-use boundaries.

---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
