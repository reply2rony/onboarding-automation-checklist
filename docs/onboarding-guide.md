# Onboarding Automation Checklist — Guide

A starter guide for automating new-starter IT onboarding in a small
IT team. This is a learning template — adapt the steps to your own
organisation's process. All people, roles, systems, and steps below
are fictional.

## What onboarding automation means

Onboarding automation is preparing as much as possible before a new
starter's first day, so their first login works and nothing is
forgotten. Some steps can be scripted or templated — creating an
email account from a form, for example — and some must stay manual,
such as handing over a device in person. The checklist keeps both
kinds in one place, with an owner for every step.

## The four phases

- **Before day 1** — prepare everything: accounts, device,
  access requests. Nothing here needs the starter present.
- **Day 1** — welcome and first login: hand over the device, help
  with the first login, set a password, check the basics work.
- **Week 1** — access and training: grant system access, introduce
  the team, run basic training, answer questions.
- **Week 2+** — review and close out: check everything works,
  collect feedback, and close the checklist only when every step
  is done or explicitly marked not needed.

## The fields that matter

- **Step** — one clear action, written so anyone on the team can
  do it without asking what it means.
- **Phase** — when the step happens (before day 1, day 1, week 1,
  or week 2+).
- **Owner** — the person or team responsible. A step with no owner
  is a step nobody does.
- **Can automate** — yes or no. "Yes" means the step can be run
  from a template or script; "no" means a person must do it.
- **Due day** — the day the step is due, counted from the starter's
  first day (negative days are before day 1).
- **Status** — not started, in progress, done, or blocked.
  "Blocked" means the step cannot proceed and needs help — say
  what is blocking it in the notes column.

## What to automate, what to keep manual

Automate the repeatable parts: account creation from a standard
form, standard software installs, standard access for a role, and
the welcome email. Keep manual: handing over hardware, checking
the starter can actually log in, anything involving a password
the starter chooses, and the first-week check-in conversation.
Automation saves time; it does not replace a person checking that
the new starter can work.

## The review rhythm

1. **Before day 1** — run the summary script and read the overdue
   and unassigned steps first.
2. **End of day 1** — mark the day-1 steps done or blocked, and
   fix anything blocked the same day.
3. **End of week 1** — review the week-1 steps with the starter;
   record what was confusing or missing.
4. **End of week 2** — close the checklist, and write one note
   about what to improve for the next starter.

## Common mistakes (starter notes)

- No owner on a step, so nobody does it.
- Creating accounts on day 1 instead of before, so the starter
  waits while accounts are made.
- Giving access before the starter's role is confirmed.
- Marking steps done without checking they actually work.
- Recording real employee names, account details, or credentials
  in a shared template.
- Treating the checklist as finished when the starter can log in
  — onboarding is done when the starter can do their job, not
  when they can open their email.

## Adding your own steps

Add a row to `onboarding-checklist-template.csv` with: step, phase,
owner, can_automate, due_day, status, and notes. Keep every entry
fictional in samples — never commit real employee names, account
details, or credentials.

## Sample / Demo notice

All people here are fictional samples for learning, labelled
"Sample / Demo" in the diagram. This template does not claim any
production use.
