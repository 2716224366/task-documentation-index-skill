#!/usr/bin/env python3
"""Create and maintain a human-readable task history index."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


VALID_KINDS = {
    "bug",
    "feature",
    "requirement",
    "plan",
    "asset",
    "test",
    "release",
    "research",
    "other",
}


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug[:60] or "task"


def docs_dir(root: Path) -> Path:
    return root / "docs" / "task-history"


def index_path(root: Path) -> Path:
    return docs_dir(root) / "INDEX.md"


def ensure_index(root: Path) -> Path:
    directory = docs_dir(root)
    directory.mkdir(parents=True, exist_ok=True)
    path = index_path(root)
    if not path.exists():
        path.write_text(
            "# Task History Index\n\n"
            "This index records human-readable task documents. Read this file before "
            "bug fixes, code changes, requirements work, planning, asset work, tests, "
            "or releases.\n\n"
            "| Date | Kind | Title | Purpose | Document | Status |\n"
            "| --- | --- | --- | --- | --- | --- |\n",
            encoding="utf-8",
        )
    return path


def append_index_entry(
    root: Path,
    *,
    date: str,
    kind: str,
    title: str,
    purpose: str,
    doc_path: Path,
    status: str,
) -> None:
    path = ensure_index(root)
    relative_doc = doc_path.relative_to(path.parent).as_posix()
    row = (
        f"| {date} | {kind} | {escape(title)} | {escape(purpose)} | "
        f"[doc]({relative_doc}) | {status} |\n"
    )
    current = path.read_text(encoding="utf-8")
    if f"]({relative_doc})" not in current:
        path.write_text(current.rstrip() + "\n" + row, encoding="utf-8")


def escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def create_task_doc(
    root: Path,
    *,
    kind: str,
    title: str,
    summary: str,
    status: str,
) -> Path:
    if kind not in VALID_KINDS:
        raise SystemExit(f"Invalid kind: {kind}. Choose one of: {', '.join(sorted(VALID_KINDS))}")

    ensure_index(root)
    now = dt.datetime.now()
    date = now.strftime("%Y-%m-%d")
    timestamp = now.strftime("%Y-%m-%d-%H%M")
    filename = f"{timestamp}-{slugify(title)}.md"
    path = docs_dir(root) / filename
    counter = 2
    while path.exists():
        path = docs_dir(root) / f"{timestamp}-{slugify(title)}-{counter}.md"
        counter += 1

    path.write_text(
        f"# {title}\n\n"
        f"- Date: {date}\n"
        f"- Kind: {kind}\n"
        f"- Status: {status}\n\n"
        "## Purpose\n\n"
        f"{summary or 'Describe why this task exists.'}\n\n"
        "## Index Check\n\n"
        "- Read `docs/task-history/INDEX.md` before starting.\n"
        "- Related prior docs checked: TODO\n\n"
        "## Plan\n\n"
        "- TODO\n\n"
        "## Work Log\n\n"
        "- TODO\n\n"
        "## Files Or Systems Affected\n\n"
        "- TODO\n\n"
        "## Verification\n\n"
        "- TODO\n\n"
        "## Outcome\n\n"
        "- TODO\n\n"
        "## Follow-Ups Or Risks\n\n"
        "- TODO\n",
        encoding="utf-8",
    )
    append_index_entry(
        root,
        date=date,
        kind=kind,
        title=title,
        purpose=summary or title,
        doc_path=path,
        status=status,
    )
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Maintain task history docs and index.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init", help="Create docs/task-history/INDEX.md if missing.")
    init.add_argument("--root", default=".", help="Project root.")

    new = subparsers.add_parser("new", help="Create a task doc and add it to the index.")
    new.add_argument("--root", default=".", help="Project root.")
    new.add_argument("--kind", required=True, choices=sorted(VALID_KINDS))
    new.add_argument("--title", required=True)
    new.add_argument("--summary", default="")
    new.add_argument("--status", default="In progress")

    args = parser.parse_args()
    root = Path(args.root).resolve()

    if args.command == "init":
      print(ensure_index(root))
      return

    if args.command == "new":
      path = create_task_doc(
          root,
          kind=args.kind,
          title=args.title,
          summary=args.summary,
          status=args.status,
      )
      print(path)


if __name__ == "__main__":
    main()
