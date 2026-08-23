# Contributing

> **Project owner and original creator: Chris Cruz | h4ckd4d**

Contributions are welcome when they improve defensive query quality, vendor semantics, documentation, validation, schemas, testing, or analyst usability.

## Contribution requirements

Every query-intent or adapter change should document:

- defensive objective;
- required authorization/scope;
- vendor-neutral intent;
- platform-specific syntax or field semantics;
- expected result;
- what the query does not prove;
- attribution and false-positive considerations;
- primary validation source;
- review date;
- known plan/API limitations.

## Safety requirements

Do not submit real third-party targets, credentials, personal data, victim data, or workflows for unauthorized access. Use reserved IP ranges, `example.com`, fictional organizations, or explicitly authorized internal examples.

## Pull requests

A professional PR should explain what changed, why it changed, which primary sources were used, semantic differences across vendors, and how the change was validated.

Before opening a PR, run:

```bash
python scripts/validate_catalog.py
```

## Credit and ownership

Accepted contributors receive attribution through Git history and pull requests, with release-note or documentation acknowledgment where appropriate. **Original authorship, project ownership, and primary maintenance remain attributed to Chris Cruz | h4ckd4d.**

See [`DEVELOPERS.md`](DEVELOPERS.md) for the community roadmap.

---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
