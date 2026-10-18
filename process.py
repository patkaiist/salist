import pandas as pd
import os

PROTOKHM_SLNOS = [
    395, 84, 384, 72, 57, 373, 201, 339, 377, 111, 61, 329, 355, 152, 333, 620,
    43, 278, 143, 467, 28, 11, 45, 73, 188, 484, 394, 29, 471, 2673, 335, 8,
    337, 287, 13, 2839, 5, 70, 97, 177, 18, 16, 55, 51, 428, 208, 363, 22, 19,
    121, 203, 79, 95, 67, 300, 2237, 227, 36, 499, 42, 1444, 279, 477, 219, 160,
]

def process_concepts():
    df = pd.read_csv('concepts.tsv', sep='\t')

    if 'slno' in df.columns:
        df['slno'] = df['slno'].astype('Int64')

    if 'stage' in df.columns:
        df['stage'] = df['stage'].astype('Int64')

    columns_to_drop = []
    for col in ['ok', 'inc', 'se-tone', 'old', 'Wolam.1', 'Lainong.1', 'Lainong.2', 'Lainong.3', 'Unnamed: 41', 'Unnamed: 42', 'Unnamed: 43', 'Unnamed: 44', 'Muishaung', 'Wolam', 'Wolam', 'Thang', 'Patsho', 'Peshu', 'Nokhu', 'Pasaung', 'Kingphu', 'mak-maky1236-khalai1', 'mak-maky1236-khalai2', 'mak-maky1236-santong1', 'mak-maky1236-santong2', 'Kuku', 'Lainong', 'Lainong', 'Lainong', 'Lainong', 'Lainong (Khamti)', 'Lainong (Lahe)', 'Lainong (Long Kyan Nok Kone)', 'Lainong (Anbaw)', 'Lainong (Hwi Thaik)', 'Lainong (Wan Ton Tha Mai)', 'Lainong (Nok Nyo Kha Shang)', 'Ponyo (Ponyo Nok Inn)', 'Ponyo (Lang Kheng)', 'Gongwan (Solo Nok Kone)', 'Khiamniungan (Pasaung)', 'Makyam (Makyam)', 'Makyam (Khale)', 'Makyam (Santhong)', 'Makyam (Kuku Nokkone)']:
        if col in df.columns:
            columns_to_drop.append(col)

    for col in df.columns:
        if col.endswith('_r'):
            columns_to_drop.append(col)

    df = df.drop(columns=columns_to_drop, errors='ignore')

    stage_filters = [
        (0, "stage == 0"),
        (1, "stage <= 1"),
        (2, "stage <= 2"),
        (3, "stage <= 3"),
        (4, "stage <= 4"),
        (5, "stage <= 5"),
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

        if row_count > 0:
            filtered_df.to_csv(filename, sep='\t', index=False)

    order = {slno: i for i, slno in enumerate(PROTOKHM_SLNOS)}
    protokhm_df = df[df['slno'].isin(order)].sort_values(
        'slno', key=lambda s: s.map(order)
    )
    protokhm_df.to_csv(
        os.path.join('lists', 'salist_protokhm.tsv'), sep='\t', index=False
    )

if __name__ == "__main__":
    process_concepts()