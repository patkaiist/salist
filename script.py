import pandas as pd
import argparse

def load_tsv(filename="latest.tsv"):
    """Load the TSV file into a Pandas DataFrame."""
    return pd.read_csv(filename, sep="\t", dtype=str).fillna("")

def count_stage_values(df):
    """Count unique non-empty values in the 'stage' column and report occurrences."""
    df["stage"] = pd.to_numeric(df["stage"], errors="coerce")  # Ensure numeric values
    stage_counts = df["stage"].dropna().astype(int).value_counts().sort_index()
    print("\nStage Value Counts:")
    print(stage_counts.to_string())

def check_concepticon(df):
    """Return a list of 'concept_id' values where 'conc_id' is blank."""
    missing_conc_id = df[df["conc_id"].str.strip() == ""]["concept_id"].dropna().unique()

    if len(missing_conc_id) == 0:
        print("✅ All rows have a 'conc_id'.")
    else:
        print("❌ Missing 'conc_id' for the following 'concept_id' values:")
        print("\n".join(str(concept_id) for concept_id in missing_conc_id))

def validate_tsv(df, other_filename):
    """Compare 'concept_id' in another TSV file against 'latest.tsv' and print missing values."""
    try:
        other_df = pd.read_csv(other_filename, sep="\t", dtype=str).fillna("")
    except FileNotFoundError:
        print(f"❌ Error: File '{other_filename}' not found.")
        return

    if "concept_id" not in other_df.columns:
        print(f"❌ Error: '{other_filename}' does not contain a 'concept_id' column.")
        return

    latest_concept_ids = set(df["concept_id"].str.strip().dropna().unique())
    other_concept_ids = set(other_df["concept_id"].str.strip().dropna().unique())

    missing_concept_ids = sorted(other_concept_ids - latest_concept_ids)

    if not missing_concept_ids:
        print("✅ All 'concept_id' values in the provided TSV exist in 'latest.tsv'.")
    else:
        print("❌ The following 'concept_id' values in the provided TSV do not exist in 'latest.tsv':")
        print("\n".join(missing_concept_ids))

def check_unique_concept_id(df):
    """Check if 'concept_id' is unique and report any duplicates (only once per value)."""
    duplicate_ids = df["concept_id"][df.duplicated(subset=["concept_id"], keep=False)].unique()

    if len(duplicate_ids) == 0:
        print("✅ All 'concept_id' values are unique.")
    else:
        print("❌ Duplicate 'concept_id' values found:")
        for concept_id in duplicate_ids:
            name = df.loc[df["concept_id"] == concept_id, "name"].iloc[0]
            print(f"{concept_id}\t{name}")

def check(df):
    """Run both check_unique_concept_id and count_stage_values."""
    check_unique_concept_id(df)
    count_stage_values(df)

def export_filtered_tsv(df, max_stage, output_filename):
    """Export rows where 'stage' is <= max_stage to a new TSV file."""
    df["stage"] = pd.to_numeric(df["stage"], errors="coerce").fillna(0).astype(int)
    filtered_df = df[df["stage"].le(max_stage)].copy()

    if filtered_df.empty:
        print(f"\n⚠️ No rows found with 'stage' <= {max_stage}. No file created.")
    else:
        filtered_df.to_csv(output_filename, sep="\t", index=False)
        print(f"\n✅ Exported filtered data to '{output_filename}'.")

def main():
    parser = argparse.ArgumentParser(description="Process 'latest.tsv' file.")
    parser.add_argument("action", choices=["count_stage", "check", "check_concept_id", "check_concepticon", "validate_tsv", "export"], help="Action to perform")
    parser.add_argument("extra_arg", nargs="?", help="Additional argument: filename (for 'validate_tsv') or number (for 'export')")

    args = parser.parse_args()
    df = load_tsv()

    if args.action == "count_stage":
        count_stage_values(df)
    elif args.action == "check":
        check(df)
    elif args.action == "check_concept_id":
        check_unique_concept_id(df)
    elif args.action == "check_concepticon":
        check_concepticon(df)
    elif args.action == "validate_tsv":
        if not args.extra_arg:
            print("\n❌ Error: You must provide a filename for the 'validate_tsv' command.")
        else:
            validate_tsv(df, args.extra_arg)
    elif args.action == "export":
        if not args.extra_arg or not args.extra_arg.isdigit():
            print("\n❌ Error: You must provide a number for the 'export' command.")
        else:
            export_filtered_tsv(df, int(args.extra_arg), f"{args.extra_arg}.tsv")

if __name__ == "__main__":
    main()
