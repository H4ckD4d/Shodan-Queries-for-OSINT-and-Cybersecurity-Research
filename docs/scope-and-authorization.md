# Scope and Authorization

> **Original creator, project owner, and primary maintainer: Chris Cruz | h4ckd4d**

The Atlas is designed around an authorization-first workflow. A query should be constructed from a known, documented ownership boundary rather than from an arbitrary technology or exposure target.

## Preferred scope anchors

Use one or more of:

- owned CIDRs;
- owned ASNs;
- approved organization identifiers;
- owned domains and hostnames;
- approved cloud inventory;
- internal asset inventory references.

## Documentation-safe values

Repository examples should use:

- `203.0.113.0/24`;
- `198.51.100.0/24`;
- `192.0.2.0/24`;
- `example.com`;
- `Example Organization`;
- private synthetic identifiers.

## Authorization reference

Machine-readable intents should carry an authorization reference when used outside documentation examples. The project does not validate legal authorization; it requires the analyst or organization to establish it before operational use.

## Interpretation boundary

Public indexing means a service was observed by a data provider. It does not establish ownership, permission, current exposure, vulnerability, exploitability, or compromise.

---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
