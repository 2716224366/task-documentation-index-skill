---
name: task-documentation-index
description: Enforce a documentation-first workflow for Codex work. Use for every bug fix, code change, feature implementation, requirement/plan discussion, asset change, architecture decision, GitHub publishing step, or project task where Codex must first read a task-document index, check prior related docs, then create or update a human-readable task document and index entry.
---

# Task Documentation Index

## Non-Negotiable Rule

Before doing implementation, bug fixing, requirement writing, planning, asset work, or publishing work:

1. Locate the project task-document index.
2. Read the index.
3. Search it for related prior work or planned work.
4. Create or update a task document for the current work.
5. Update the index with the document path and purpose.

If the project has no index, create one first, then read it before continuing.

## Default Locations

Use the project root unless the user or repository clearly specifies another location.

- Index: `docs/task-history/INDEX.md`
- Task documents: `docs/task-history/YYYY-MM-DD-HHMM-<slug>.md`

Use `scripts/task_doc.py` to create or update these files when possible:

```powershell
python <skill-dir>/scripts/task_doc.py init --root .
python <skill-dir>/scripts/task_doc.py new --root . --kind bug --title "Fix player collision" --summary "Correct collider data and verification notes."
```

## Workflow

### 1. Open The Index First

- Read `docs/task-history/INDEX.md`.
- If missing, run `task_doc.py init --root .`.
- Search the index for related keywords from the user request, such as feature names, bug symptoms, file names, requirement IDs, asset names, or GitHub/release terms.
- Mention relevant prior docs in the current task document.

Do not rely on memory alone. The index is the source of project task history.

### 2. Create A Task Document Early

Create a document before substantial work, or as soon as the task scope is clear.

Choose `kind` from:

- `bug`
- `feature`
- `requirement`
- `plan`
- `asset`
- `test`
- `release`
- `research`
- `other`

The document must be readable by a human project owner. Use plain language and include:

- what the task is for;
- why it is being done;
- what prior indexed docs were checked;
- what will be changed or decided;
- what files or systems are affected;
- verification steps;
- remaining risks or follow-ups.

### 3. Update The Document While Working

For code bugs, record:

- symptom;
- suspected cause and confirmed root cause;
- changed files/modules;
- verification commands and results;
- regression-prevention notes.

For requirements or plans, record:

- user intent;
- constraints from existing docs;
- proposed execution approach;
- decisions made;
- acceptance criteria;
- open questions.

For assets, record:

- source/reference files;
- generated candidates;
- selected runtime asset;
- prompt or design note when available;
- preservation path and ownership/licensing notes.

### 4. Close The Loop

Before final response:

- update the task document with actual outcome, not only the initial plan;
- update the index row if the document title, purpose, status, or path changed;
- include verification results or explicitly state what was not verified;
- keep the final answer short, but mention the task document path when useful.

## Index Format

Use a Markdown table:

```markdown
| Date | Kind | Title | Purpose | Document | Status |
| --- | --- | --- | --- | --- | --- |
| 2026-07-09 | bug | Fix collision | Explain root cause and fix. | [doc](2026-07-09-1230-fix-collision.md) | Done |
```

Status values:

- `Planned`
- `In progress`
- `Done`
- `Blocked`
- `Superseded`

## Safety

- Never store secrets, tokens, private keys, AppSecret, passwords, or personal identifiers in task docs.
- Do not delete or overwrite existing task documents unless the user explicitly requests it.
- If unrelated user changes exist, document the scope being touched and avoid claiming ownership of unrelated files.
- If the task cannot continue because the index is missing and cannot be created, stop and report the blocker.
