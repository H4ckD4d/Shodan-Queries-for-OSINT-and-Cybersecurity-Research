# h4ckd4d Internet Exposure Query Atlas

> **Original creator, project owner, and primary maintainer: Chris Cruz | h4ckd4d**

**h4ckd4d Internet Exposure Query Atlas** is a defensive, vendor-aware query-intelligence project for translating an authorized Internet-exposure research objective into documented query patterns for public Internet search platforms.

The project complements **h4ckd4d Internet Exposure Intelligence** and **h4ckd4d Detection Engineering** by creating a portable, analyst-readable layer between defensive research intent and platform-specific syntax.

> **Authorized use only:** Query examples must be limited to assets you own, administer, or are explicitly authorized to assess. Repository examples use reserved domains, reserved IP ranges, or fictional organizations.

## Project status

**Milestone:** `1.0.0-rc.1`  
**Reference review:** August 23, 2026  
**Owner:** Chris Cruz | h4ckd4d

Current adapter posture:

| Platform | Confidence | v1 posture |
| --- | --- | --- |
| Shodan | Validated core | Core `filter:value` semantics and API validation mechanisms documented. |
| FOFA | Partial | Conservative IP/port representation; unsupported equivalence is intentionally omitted. |
| BinaryEdge | Experimental | No executable cross-platform translation published until primary-source semantics are sufficiently validated. |

## Core architecture

```text
Defensive Research Objective
          ↓
Authorization Reference
          ↓
Authorized Scope
          ↓
Vendor-Neutral Query Intent
          ↓
Semantic Validation
          ↓
Vendor Adapter
          ↓
┌─────────┼──────────┬────────────┐
│         │          │            │
Shodan   FOFA    BinaryEdge    Future adapters
│         │          │            │
└─────────┼──────────┴────────────┘
          ↓
Analyst Review
          ↓
Exposure Observation
          ↓
Attribution / Validation
```

The Atlas does **not** treat equivalent-looking filters as automatically equivalent. Every adapter records translation confidence, limitations, primary references, and review date.

## First query intent

`H4D-QRY-0001` models **authorized HTTPS inventory** using the documentation-only network `203.0.113.0/24`.

- [`intents/asset-inventory/authorized-https-inventory.json`](intents/asset-inventory/authorized-https-inventory.json)
- [`catalog/query-catalog.json`](catalog/query-catalog.json)
- [`schemas/query-intent.schema.json`](schemas/query-intent.schema.json)

The Shodan representation is fully documented for the selected fields, FOFA remains partial, and BinaryEdge is deliberately unpublished as executable syntax in v1.

## Professional query standard

Every maintained query intent should document:

1. Defensive objective.
2. Authorized scope requirement.
3. Vendor-neutral intent.
4. Platform-specific representation.
5. Fields or filters used.
6. Expected observation.
7. What the query does **not** prove.
8. Semantic differences across vendors.
9. False-positive and attribution considerations.
10. Primary validation source, confidence, and review date.

See [`docs/query-standard.md`](docs/query-standard.md).

## Repository structure

```text
.
├── README.md
├── DEVELOPERS.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── LICENSE
├── docs/
│   ├── architecture.md
│   ├── query-standard.md
│   ├── scope-and-authorization.md
│   └── vendor-semantics.md
├── intents/
│   └── asset-inventory/
├── adapters/
│   ├── shodan/
│   ├── fofa/
│   └── binaryedge/
├── schemas/
│   └── query-intent.schema.json
├── catalog/
│   └── query-catalog.json
├── scripts/
│   └── validate_catalog.py
└── .github/
    ├── CODEOWNERS
    ├── ISSUE_TEMPLATE/
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/
```

## Safety-by-design validation

The repository CI validates that:

- every catalog entry references an existing intent;
- intent IDs are unique and correctly formatted;
- `scope_required` is always `true`;
- repository example IPv4 values stay inside RFC 5737 documentation ranges;
- example domains use `example.com`;
- vendor confidence values are explicit;
- adapter sources use HTTPS primary references;
- catalog vendor declarations match the intent adapters;
- Markdown and JSON documents are structurally valid.

Run locally:

```bash
python scripts/validate_catalog.py
```

## Vendor adapters

- [`adapters/shodan/README.md`](adapters/shodan/README.md)
- [`adapters/fofa/README.md`](adapters/fofa/README.md)
- [`adapters/binaryedge/README.md`](adapters/binaryedge/README.md)

See [`docs/vendor-semantics.md`](docs/vendor-semantics.md) for translation-confidence policy.

## Scope and interpretation

Relationship is not ownership. Ownership is not authorization. An indexed service is an observation, not proof of vulnerability, exploitability, compromise, or current state.

See [`docs/scope-and-authorization.md`](docs/scope-and-authorization.md).

## Developers wanted

**Developers, OSINT researchers, EASM practitioners, security engineers, technical writers, data-model designers, and maintainers of Internet-intelligence tooling are invited to help build the Atlas professionally.**

Priority contribution areas:

- primary-source validation of vendor syntax;
- new defensive query intents;
- vendor-semantic corrections;
- schemas and validation tooling;
- safe fixtures/examples;
- adapters and portability testing;
- attribution and false-positive analysis;
- CI/CD and documentation improvements.

Read [`DEVELOPERS.md`](DEVELOPERS.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md) before contributing.

Accepted contributors receive credit through Git history, pull requests, release notes, and acknowledgments where appropriate. **Original authorship, project ownership, and primary maintenance remain attributed to Chris Cruz | h4ckd4d.**

## Project ecosystem

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

Released under the MIT License. See [`LICENSE`](LICENSE).

---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
