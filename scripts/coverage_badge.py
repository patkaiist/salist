import csv
import json
import os

LISTS = [
    "salist_30",
    "salist_100",
    "salist_350",
    "salist_500",
    "salist_1000",
    "salist_full",
]
OUTPUT_DIR = "badges"
CONCEPT_DOI = "10.5281/zenodo.18515381"
EMPTY = {"", "-", "–", "—", "nan", "NA"}


def color(pct):
    if pct >= 95:
        return "brightgreen"
    if pct >= 80:
        return "yellow"
    if pct >= 70:
        return "orange"
    return "red"


def write(name, badge):
    with open(os.path.join(OUTPUT_DIR, f"{name}.json"), "w", encoding="utf-8") as f:
        json.dump(badge, f, indent=2)
        f.write("\n")


def coverage(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    total = len(rows)
    mapped = sum(1 for r in rows if (r.get("concepticon_id") or "").strip() not in EMPTY)
    return mapped, total


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for name in LISTS:
        mapped, total = coverage(os.path.join("lists", f"{name}.tsv"))
        pct = 100 * mapped / total if total else 0
        label = name.split("_")[1]

        badge = {
            "schemaVersion": 1,
            "label": label,
            "message": f"{mapped}/{total} ({pct:.0f}%)",
            "color": color(pct),
        }

        write(name, badge)
        print(f"{label}: {badge['message']}")

    doi = {
        "schemaVersion": 1,
        "label": "DOI",
        "message": CONCEPT_DOI,
        "color": "blue",
    }
    write("doi", doi)
    print(f"DOI: {doi['message']}")


if __name__ == "__main__":
    main()
