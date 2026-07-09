#!/usr/bin/env python3
"""Report study notes that may be ready for folder promotion.

This script is advisory. It never moves, deletes, or edits files.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOPICS_DIR = ROOT / "topics"
SOURCES_DIR = ROOT / "sources"

HEADING_RE = re.compile(r"^#{2,3}\s+\S")
ENTRY_HEADING_RE = re.compile(r"^###\s+\S")
ENTRY_TOPICS_RE = re.compile(r"^\s*-\s*topics:\s*(.+)$")
DAILY_SOURCE_NAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")
LEGACY_SOURCE_NAME_RE = re.compile(r"^(\d{4})-(\d{2})-\d{2}-.+\.md$")
MONTH_DIR_RE = re.compile(r"^\d{4}-\d{2}$")
DATE_VALUE_RE = re.compile(r"^(\d{4})-(\d{2})-\d{2}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check whether topic files or source entries are ready to be promoted into folders."
    )
    parser.add_argument(
        "--topic-lines",
        type=int,
        default=300,
        help="Flag a topic file at this many lines. Default: 300.",
    )
    parser.add_argument(
        "--topic-headings",
        type=int,
        default=12,
        help="Flag a topic file at this many H2/H3 headings. Default: 12.",
    )
    parser.add_argument(
        "--topic-sources",
        type=int,
        default=30,
        help="Flag a topic when this many source entries reference it. Default: 30.",
    )
    parser.add_argument(
        "--flat-sources",
        type=int,
        default=100,
        help="Flag sources/ when this many source files live directly under it. Default: 100.",
    )
    parser.add_argument(
        "--monthly-sources",
        type=int,
        default=30,
        help="Flag a month when this many source entries share it. Default: 30.",
    )
    parser.add_argument(
        "--daily-source-entries",
        type=int,
        default=20,
        help="Flag a daily source log at this many entries. Default: 20.",
    )
    parser.add_argument(
        "--daily-source-lines",
        type=int,
        default=500,
        help="Flag a daily source log at this many lines. Default: 500.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with status 1 when promotion candidates are found.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_frontmatter(text: str) -> list[str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return []

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return lines[1:index]

    return []


def clean_value(value: str) -> str:
    return value.strip().strip("'\"")


def parse_inline_list(value: str) -> list[str]:
    body = value.strip()[1:-1]
    if not body.strip():
        return []
    return [clean_value(item) for item in body.split(",") if clean_value(item)]


def parse_topic_value(value: str) -> list[str]:
    value = value.strip()
    if not value:
        return []
    if value.startswith("[") and value.endswith("]"):
        return parse_inline_list(value)
    return [clean_value(item) for item in value.split(",") if clean_value(item)]


def parse_frontmatter(text: str) -> dict[str, object]:
    data: dict[str, object] = {}
    current_key: str | None = None

    for line in split_frontmatter(text):
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        key_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if key_match:
            key, raw_value = key_match.groups()
            value = raw_value.strip()
            current_key = None

            if value == "":
                data[key] = []
                current_key = key
            elif value.startswith("[") and value.endswith("]"):
                data[key] = parse_inline_list(value)
            else:
                data[key] = clean_value(value)
            continue

        item_match = re.match(r"^\s*-\s+(.+)$", line)
        if item_match and current_key:
            items = data.setdefault(current_key, [])
            if isinstance(items, list):
                items.append(clean_value(item_match.group(1)))

    return data


def normalize_slug(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    value = value.strip().lower()
    return value or None


def normalize_topics(value: object) -> list[str]:
    if isinstance(value, str):
        return [topic for topic in (normalize_slug(item) for item in parse_topic_value(value)) if topic]
    if isinstance(value, list):
        topics = [normalize_slug(item) for item in value]
        return [topic for topic in topics if topic]
    return []


def topic_files() -> list[Path]:
    if not TOPICS_DIR.exists():
        return []
    return sorted(
        path
        for path in TOPICS_DIR.glob("*.md")
        if path.is_file() and path.name.lower() != "readme.md"
    )


def source_files() -> list[Path]:
    if not SOURCES_DIR.exists():
        return []
    return sorted(
        path
        for path in SOURCES_DIR.rglob("*.md")
        if path.is_file() and path.name.lower() != "readme.md"
    )


def flat_source_files() -> list[Path]:
    if not SOURCES_DIR.exists():
        return []
    return sorted(
        path
        for path in SOURCES_DIR.glob("*.md")
        if path.is_file() and path.name.lower() != "readme.md"
    )


def is_daily_source_log(path: Path, metadata: dict[str, object]) -> bool:
    if normalize_slug(metadata.get("type")) == "daily-sources":
        return True
    return bool(MONTH_DIR_RE.match(path.parent.name) and DAILY_SOURCE_NAME_RE.match(path.name))


def source_entry_count(path: Path) -> int:
    text = read_text(path)
    metadata = parse_frontmatter(text)
    if is_daily_source_log(path, metadata):
        count = sum(1 for line in text.splitlines() if ENTRY_HEADING_RE.match(line))
        return count
    return 1


def source_entry_topics(path: Path) -> list[str]:
    text = read_text(path)
    metadata = parse_frontmatter(text)

    if is_daily_source_log(path, metadata):
        topics: list[str] = []
        for line in text.splitlines():
            match = ENTRY_TOPICS_RE.match(line)
            if match:
                topics.extend(normalize_topics(match.group(1)))
        return topics

    topics = normalize_topics(metadata.get("topics"))
    if not topics:
        topics = normalize_topics(metadata.get("topic"))
    return topics


def source_month(path: Path) -> str | None:
    text = read_text(path)
    metadata = parse_frontmatter(text)
    date = metadata.get("date") or metadata.get("captured") or metadata.get("published")
    if isinstance(date, str):
        match = DATE_VALUE_RE.match(date.strip())
        if match:
            year, month = match.groups()
            return f"{year}-{month}"

    if MONTH_DIR_RE.match(path.parent.name):
        return path.parent.name

    match = LEGACY_SOURCE_NAME_RE.match(path.name)
    if match:
        year, month = match.groups()
        return f"{year}-{month}"

    return None


def count_source_topics(paths: list[Path]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for path in paths:
        counts.update(source_entry_topics(path))
    return counts


def count_source_months(paths: list[Path]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for path in paths:
        month = source_month(path)
        if month:
            counts[month] += source_entry_count(path)
    return counts


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_topics(args: argparse.Namespace, source_topic_counts: Counter[str]) -> list[str]:
    candidates: list[str] = []

    for path in topic_files():
        text = read_text(path)
        metadata = parse_frontmatter(text)
        topic = normalize_slug(metadata.get("topic")) or path.stem.lower()

        line_count = len(text.splitlines())
        heading_count = sum(1 for line in text.splitlines() if HEADING_RE.match(line))
        source_count = source_topic_counts.get(topic, 0)

        reasons = []
        if line_count >= args.topic_lines:
            reasons.append(f"{line_count} lines >= {args.topic_lines}")
        if heading_count >= args.topic_headings:
            reasons.append(f"{heading_count} H2/H3 headings >= {args.topic_headings}")
        if source_count >= args.topic_sources:
            reasons.append(f"{source_count} linked source entries >= {args.topic_sources}")

        if reasons:
            candidates.append(f"- {rel(path)} ({topic}): " + "; ".join(reasons))

    return candidates


def check_sources(args: argparse.Namespace, sources: list[Path], flat_sources: list[Path]) -> list[str]:
    candidates: list[str] = []

    if len(flat_sources) >= args.flat_sources:
        candidates.append(
            f"- sources/: {len(flat_sources)} flat source files >= {args.flat_sources}; "
            "consider sources/YYYY-MM/YYYY-MM-DD.md."
        )

    for month, count in sorted(count_source_months(sources).items()):
        if count >= args.monthly_sources:
            candidates.append(
                f"- sources/{month}: {count} source entries >= {args.monthly_sources}; "
                "consider splitting heavy days into deep-dive notes."
            )

    for path in sources:
        text = read_text(path)
        metadata = parse_frontmatter(text)
        if not is_daily_source_log(path, metadata):
            continue

        entry_count = source_entry_count(path)
        line_count = len(text.splitlines())
        reasons = []
        if entry_count >= args.daily_source_entries:
            reasons.append(f"{entry_count} entries >= {args.daily_source_entries}")
        if line_count >= args.daily_source_lines:
            reasons.append(f"{line_count} lines >= {args.daily_source_lines}")

        if reasons:
            candidates.append(f"- {rel(path)}: " + "; ".join(reasons))

    return candidates


def main() -> int:
    args = parse_args()
    sources = source_files()
    flat_sources = flat_source_files()
    source_topic_counts = count_source_topics(sources)
    source_entries = sum(source_entry_count(path) for path in sources)

    topic_candidates = check_topics(args, source_topic_counts)
    source_candidates = check_sources(args, sources, flat_sources)
    candidates = topic_candidates + source_candidates

    print("Promotion candidate check")
    print(f"- topic files: {len(topic_files())}")
    print(f"- source files: {len(sources)}")
    print(f"- source entries: {source_entries}")
    print(f"- flat source files: {len(flat_sources)}")

    if not candidates:
        print("\nNo promotion candidates found.")
        return 0

    print("\nPromotion candidates:")
    for candidate in candidates:
        print(candidate)

    print("\nThis is advisory only. Review candidates during the monthly review.")
    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
