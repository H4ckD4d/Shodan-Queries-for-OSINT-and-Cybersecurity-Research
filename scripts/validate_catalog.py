#!/usr/bin/env python3
"""Validate h4ckd4d Internet Exposure Query Atlas consistency.

Static/offline validation only. This script does not contact search platforms,
execute queries, scan networks, or interact with external systems.
"""

from __future__ import annotations

import ipaddress
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "query-catalog.json"
INTENTS = ROOT / "intents"
ALLOWED_VENDORS = {"shodan", "fofa", "binaryedge"}
ALLOWED_CONFIDENCE = {"validated", "partial", "experimental"}
ALLOWED_STATUS = {"experimental", "test", "stable", "deprecated"}
SAFE_NETWORKS = {
    ipaddress.ip_network("192.0.2.0/24"),
    ipaddress.ip_network("198.51.100.0/24"),
    ipaddress.ip_network("203.0.113.0/24"),
}
IPV4_RE = re.compile(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def safe_ip_token(token: str) -> bool:
    try:
        obj = ipaddress.ip_network(token, strict=False)
    except ValueError:
        return False
    return any(obj.subnet_of(safe) for safe in SAFE_NETWORKS)


def main() -> int:
    errors: list[str] = []
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    entries = catalog.get("intents", [])
    if not entries:
        fail(errors, "query catalog contains no intents")

    seen_ids: set[str] = set()
    catalog_ids: set[str] = set()

    for entry in entries:
        intent_id = str(entry.get("id", ""))
        if not re.fullmatch(r"H4D-QRY-\d{4}", intent_id):
            fail(errors, f"invalid intent id: {intent_id}")
            continue
        if intent_id in seen_ids:
            fail(errors, f"duplicate intent id: {intent_id}")
        seen_ids.add(intent_id)
        catalog_ids.add(intent_id)

        if entry.get("status") not in ALLOWED_STATUS:
            fail(errors, f"{intent_id}: invalid status {entry.get('status')}")

        path = ROOT / str(entry.get("path", ""))
        if not path.is_file():
            fail(errors, f"{intent_id}: missing intent file {entry.get('path')}")
            continue

        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("id") != intent_id:
            fail(errors, f"{intent_id}: catalog id does not match intent file")
        if data.get("scope_required") is not True:
            fail(errors, f"{intent_id}: scope_required must be true")

        constraints = data.get("constraints", {})
        network = constraints.get("network")
        if network and not safe_ip_token(str(network)):
            fail(errors, f"{intent_id}: repository example network is not documentation-safe: {network}")
        domain = constraints.get("domain")
        if domain and str(domain).lower() != "example.com":
            fail(errors, f"{intent_id}: repository example domain must be example.com")

        adapters = data.get("adapters", [])
        if not adapters:
            fail(errors, f"{intent_id}: no adapters")

        vendors: set[str] = set()
        whole_text = path.read_text(encoding="utf-8")
        for token in IPV4_RE.findall(whole_text):
            if not safe_ip_token(token):
                fail(errors, f"{intent_id}: non-documentation IPv4 value found: {token}")

        for adapter in adapters:
            vendor = str(adapter.get("vendor", ""))
            if vendor not in ALLOWED_VENDORS:
                fail(errors, f"{intent_id}: unsupported vendor {vendor}")
            if vendor in vendors:
                fail(errors, f"{intent_id}: duplicate adapter {vendor}")
            vendors.add(vendor)
            if adapter.get("confidence") not in ALLOWED_CONFIDENCE:
                fail(errors, f"{intent_id}/{vendor}: invalid confidence")
            if not str(adapter.get("source", "")).startswith("https://"):
                fail(errors, f"{intent_id}/{vendor}: source must be https primary reference")
            if not str(adapter.get("representation", "")).strip():
                fail(errors, f"{intent_id}/{vendor}: representation cannot be empty")

        declared = set(entry.get("vendors", []))
        if declared != vendors:
            fail(errors, f"{intent_id}: catalog vendors {sorted(declared)} do not match adapters {sorted(vendors)}")

    file_ids: set[str] = set()
    for path in sorted(INTENTS.rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        file_ids.add(str(data.get("id", "")))

    if file_ids != catalog_ids:
        fail(errors, f"catalog/file intent mismatch: catalog={sorted(catalog_ids)} files={sorted(file_ids)}")

    if errors:
        print("Query Atlas validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Query Atlas validation passed: {len(entries)} intent(s), documentation-safe examples only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
