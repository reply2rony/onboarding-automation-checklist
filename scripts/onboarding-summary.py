#!/usr/bin/env python3
"""Starter learning template: summarise the onboarding checklist.

Usage:
    python3 scripts/onboarding-summary.py onboarding-checklist-template.csv
    python3 scripts/onboarding-summary.py onboarding-checklist-template.csv --phase accounts
    python3 scripts/onboarding-summary.py onboarding-checklist-template.csv --owner "Sample IT Support"

Summarises the CSV by phase, owner, and status, and flags overdue
and unassigned steps. Sample data only; no real company data.
"""
import argparse
import csv
import sys
from collections import Counter


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser(description="Summarise the onboarding checklist.")
    ap.add_argument("csv_file", help="path to onboarding-checklist-template.csv")
    ap.add_argument("--phase", help="filter by phase (e.g. day 1)")
    ap.add_argument("--owner", help="filter by owner")
    args = ap.parse_args()

    try:
        rows = load(args.csv_file)
    except FileNotFoundError:
        print(f"File not found: {args.csv_file}")
        sys.exit(1)

    if args.phase:
        rows = [r for r in rows if r.get("phase", "").lower() == args.phase.lower()]
    if args.owner:
        rows = [r for r in rows if r.get("owner", "").lower() == args.owner.lower()]

    if not rows:
        print("No matching checklist steps.")
        sys.exit(0)

    print(f"Checklist steps: {len(rows)}")
    print()
    print("By status:")
    for st, n in Counter(r.get("status", "") for r in rows).most_common():
        print(f"  {st}: {n}")
    print()
    print("By phase:")
    for ph, n in Counter(r.get("phase", "") for r in rows).most_common():
        print(f"  {ph}: {n}")
    print()
    print("By owner:")
    for ow, n in Counter(r.get("owner", "") for r in rows).most_common():
        print(f"  {ow}: {n}")
    print()
    blocked = [r for r in rows if r.get("status", "").lower() == "blocked"]
    if blocked:
        print("Blocked steps — fix these first:")
        for r in blocked:
            print(f"  {r['step']} ({r['phase']}, {r['owner']}): {r['notes']}")
    else:
        print("No blocked steps in this view.")
    print()
    unassigned = [r for r in rows if not r.get("owner", "").strip()]
    if unassigned:
        print("Unassigned steps — give each one an owner:")
        for r in unassigned:
            print(f"  {r['step']} ({r['phase']})")
    else:
        print("Every step in this view has an owner.")
    print()
    auto = [r for r in rows if r.get("can_automate", "").lower() == "yes"]
    manual = [r for r in rows if r.get("can_automate", "").lower() == "no"]
    print(f"Automatable steps: {len(auto)}; manual steps: {len(manual)}")


if __name__ == "__main__":
    main()
