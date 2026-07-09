# Task Documentation Index Skill

A Codex skill that makes project work documentation-first.

This skill is designed for teams that want every bug fix, feature, plan, asset change, test pass, release step, or GitHub publishing task to leave behind a clear human-readable record. Before doing work, Codex must read docs/task-history/INDEX.md, check prior related documents, and then create or update a task document. Before finishing, Codex must update the index with the document path, purpose, and status.

## What It Enforces

- Read the task-document index before implementation, bug fixing, planning, asset work, tests, releases, or publishing.
- Search prior task documents so new work does not ignore earlier decisions or repeated problems.
- Create or update a readable Markdown task document for each meaningful task.
- Record purpose, prior docs checked, affected files or systems, verification steps, outcomes, and follow-ups.
- Keep a central index at docs/task-history/INDEX.md so future Codex sessions can recover project history quickly.

## Included Files

- 	ask-documentation-index/SKILL.md - the skill instructions and hard workflow rule.
- 	ask-documentation-index/scripts/task_doc.py - helper script for initializing the index and creating task docs.
- 	ask-documentation-index/references/task-doc-template.md - human-readable task-document template for manual repair or custom docs.
- 	ask-documentation-index/agents/openai.yaml - Codex UI metadata for the skill.

## Typical Use

Install the 	ask-documentation-index folder into your Codex skills directory, commonly:

`powershell
C:\Users\<you>\.codex\skills\task-documentation-index
`

Then future Codex tasks that involve bugs, code changes, planning, requirements, assets, tests, releases, or GitHub publishing should trigger the skill automatically.

## Helper Script

From a project root, initialize the task history:

`powershell
python C:\Users\<you>\.codex\skills\task-documentation-index\scripts\task_doc.py init --root .
`

Create a new task document:

`powershell
python C:\Users\<you>\.codex\skills\task-documentation-index\scripts\task_doc.py new --root . --kind bug --title "Fix player collision" --summary "Correct collider data and record verification."
`

## License

MIT. This repository contains only the reusable Codex skill and documentation workflow helper, not any private game assets or project-specific protected content.