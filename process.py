import pandas as pd
import os

def process_concepts():
    df = pd.read_csv('concepts.tsv', sep='\t')

    columns_to_drop = []

    for col in ['ok', 'inc', 'SILCAWL', 'se-tone', 'CALMSEA', 'old']:
        if col in df.columns:
            columns_to_drop.append(col)
    
    for col in df.columns:
        if col.endswith('_r'):
            columns_to_drop.append(col)

    df = df.drop(columns=columns_to_drop, errors='ignore')

    stage_filters = [
        (1, "stage == 1"),
        (2, "stage <= 2"),
        (3, "stage <= 3"),
        (4, "stage <= 4"),
        (None, None)
    ]

    os.makedirs('lists', exist_ok=True)

    for i, (max_stage, filter_expr) in enumerate(stage_filters):
        if filter_expr is None:
            filtered_df = df
        else:
            filtered_df = df.query(filter_expr)

        row_count = len(filtered_df)

        if filter_expr is None:
            filename = os.path.join('lists', 'salist_full.tsv')
        else:
            filename = os.path.join('lists', f"salist_{row_count}.tsv")

        filtered_df.to_csv(filename, sep='\t', index=False)

if __name__ == "__main__":
    process_concepts()