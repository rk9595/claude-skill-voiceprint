"""
ingest/load.py — Load email thread exhibits from the Musk v. Altman dataset.

Usage:
    python -m ingest.load                  # print all email threads
    python -m ingest.load --survey         # show all exhibit types + counts
    python -m ingest.load DX-509 DX-516    # load specific exhibit ids
    python -m ingest.load --type email     # filter by type keyword
"""

import sys

from datasets import load_dataset

DATASET = "MTSlive/musk-v-altman-exhibits"

ATTRIBUTION = (
    'Source: "MTS — musk-v-altman trial coverage", CC-BY-4.0, '
    "https://huggingface.co/datasets/MTSlive/musk-v-altman-exhibits "
    "(underlying texts are U.S. public court records)."
)

EMAIL_KEYWORDS = {"email", "mail", "message", "thread", "chain", "correspondence"}


def is_email_type(type_val: str) -> bool:
    t = (type_val or "").lower()
    return any(kw in t for kw in EMAIL_KEYWORDS)


def survey(ds) -> None:
    from collections import Counter
    counts = Counter(row["type"] for row in ds)
    print(f"{'Type':<40} {'Count':>6}")
    print("-" * 48)
    for t, n in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{t:<40} {n:>6}")
    print(f"\nTotal rows: {len(ds)}")


def print_exhibit(row) -> None:
    print(f"\n### {row['exhibit_id']}  ({row['type']})")
    print(f"PDF: {row['pdf_url']}")
    print("-" * 70)
    print(row["body_markdown"])
    print("\n" + "=" * 70)


def main() -> None:
    args = sys.argv[1:]

    print(f"Loading {DATASET} ...\n")
    ds = load_dataset(DATASET, split="train")
    print(f"Loaded {len(ds)} rows.\n")
    print(ATTRIBUTION + "\n")

    if "--survey" in args:
        survey(ds)
        return

    type_filter = None
    if "--type" in args:
        idx = args.index("--type")
        type_filter = args[idx + 1].lower()
        args = args[:idx] + args[idx + 2:]

    # Specific exhibit IDs passed on the command line
    if args:
        wanted = set(args)
        rows = [row for row in ds if row["exhibit_id"] in wanted]
        missing = wanted - {row["exhibit_id"] for row in rows}
        if missing:
            print(f"[!] Not found: {', '.join(sorted(missing))}\n")
    elif type_filter:
        rows = [row for row in ds if type_filter in (row["type"] or "").lower()]
    else:
        # Default: all email threads
        rows = [row for row in ds if is_email_type(row["type"])]

    print(f"Showing {len(rows)} exhibit(s).\n{'=' * 70}")
    for row in rows:
        print_exhibit(row)

    if not rows:
        print("No matching exhibits found. Run with --survey to see available types.")


if __name__ == "__main__":
    main()
