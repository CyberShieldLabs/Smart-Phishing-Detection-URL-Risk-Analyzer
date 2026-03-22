import pandas as pd


def create_balanced_dataset(
    input_file="final_dataset.csv",
    output_file="balanced_dataset.csv"
):
    print("🚀 Creating balanced dataset...\n")

    # ---------------------------
    # LOAD DATA
    # ---------------------------
    df = pd.read_csv(input_file)

    print(f"Total rows: {len(df)}")

    # ---------------------------
    # COUNT LABELS
    # ---------------------------
    count_0 = len(df[df["label"] == 0])
    count_1 = len(df[df["label"] == 1])

    print(f"Label 0: {count_0}")
    print(f"Label 1: {count_1}")

    # ---------------------------
    # FIND MINIMUM
    # ---------------------------
    min_count = min(count_0, count_1)

    print(f"\nUsing min count: {min_count}")

    # ---------------------------
    # SAMPLE DATA
    # ---------------------------
    df_0 = df[df["label"] == 0].sample(n=min_count, random_state=42)
    df_1 = df[df["label"] == 1].sample(n=min_count, random_state=42)

    # ---------------------------
    # COMBINE + SHUFFLE
    # ---------------------------
    balanced_df = pd.concat([df_0, df_1])
    balanced_df = balanced_df.sample(frac=1, random_state=42).reset_index(drop=True)

    # ---------------------------
    # SAVE
    # ---------------------------
    balanced_df.to_csv(output_file, index=False)

    print("\n✅ Balanced dataset created!")
    print(f"Final rows: {len(balanced_df)}")
    print(f"Each class: {min_count}")


# ---------------------------
# RUN
# ---------------------------
if __name__ == "__main__":
    create_balanced_dataset()
