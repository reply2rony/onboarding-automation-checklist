# Onboarding Automation Checklist — Starter Template

A starter learning template for automating new-starter IT onboarding
in a small IT team: the checklist of accounts, devices, and access a
new joiner needs, in what order, and who owns each step. It is a
checklist plus a small sample log in CSV form, so an IT team can
practise running a repeatable onboarding before ever applying it to
a real hire. Sample content only — no real company data, no real
employee names, no invented metrics, and no claim of production use.

## What it is

- `docs/onboarding-guide.md` — the guide: the onboarding phases,
  which steps can be automated, which must stay manual, and how to
  review a completed onboarding.
- `onboarding-checklist-template.csv` — the checklist in CSV form,
  so you can copy it, filter it, and add your own sample steps.
- `scripts/onboarding-summary.py` — a starter Python script that
  summarises the checklist by phase, owner, and status, and flags
  overdue and unassigned steps. Labelled a starter learning
  template; it is not a production tool.

## How to use

1. Add one row per onboarding step in
   `onboarding-checklist-template.csv` — step, phase, owner,
   whether it can be automated, due day, and status.
2. Before a new starter's first day, run the summary script and
   read the flags: overdue steps first, then unassigned ones.
3. On the starter's first day, work through the checklist in phase
   order — accounts first, then device, then access, then training.
4. After the first week, review the log using
   `docs/onboarding-guide.md` and record what to improve next time.
5. Summarise the checklist from the command line:

```bash
python3 scripts/onboarding-summary.py onboarding-checklist-template.csv
python3 scripts/onboarding-summary.py onboarding-checklist-template.csv --phase accounts
python3 scripts/onboarding-summary.py onboarding-checklist-template.csv --owner "Sample IT Support"
```

## Onboarding phases (starter guide)

| Phase | What happens | Example steps |
|-------|--------------|---------------|
| Before day 1 | Prepare everything the starter needs | Create accounts, prepare device, order access |
| Day 1 | Welcome and first login | Hand over device, first login, password setup |
| Week 1 | Access and training | System access, team introductions, basic training |
| Week 2+ | Review and close out | Check everything works, close the checklist |

Phases above are starter definitions for a learning template, not
a standard for any real organisation.

## Sample / Demo notice

All people, roles, systems, and steps in this repo are fictional
samples for learning. The diagram in `docs/diagram.png` is a
locally generated illustration labelled "Sample / Demo" — it is
not a screenshot of a real system, and this template does not
claim any production use.

## License

MIT — see `LICENSE`.
