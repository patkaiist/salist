import csv
import json

SOURCE = "lists/salist_full.tsv"
OUTPUT = "badge.json"
EMPTY = {"", "-", "–", "—", "nan", "NA"}


def color(pct):
    if pct > 90:
        return "brightgreen"
    if pct > 80:
        return "orange"
    if pct > 70:
        return "yellow"
    return "red"


def main():
    with open(SOURCE, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    total = len(rows)
    mapped = sum(1 for r in rows if (r.get("concepticon_id") or "").strip() not in EMPTY)
    pct = 100 * mapped / total if total else 0

    badge = {
        "schemaVersion": 1,
        "label": "Concepticon",
        "message": f"{mapped}/{total} ({pct:.1f}%)",
        "color": color(pct),
    }

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(badge, f, indent=2)
        f.write("\n")

    print(badge["message"])


if __name__ == "__main__":
    main()
