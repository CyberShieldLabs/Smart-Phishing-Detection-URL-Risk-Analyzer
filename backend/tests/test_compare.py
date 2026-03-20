import sys
import os
import pandas as pd

# ---------------------------
# Fix import path
# ---------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.feature_extractor import extract_features

# ---------------------------
# Load CSV safely
# ---------------------------
try:
    file_path = os.path.join(os.path.dirname(__file__), "modul_test.csv")
    df = pd.read_csv(file_path)
    print(f"\n✅ Dataset Loaded: {len(df)} rows\n")
except Exception as e:
    print("❌ Error loading CSV:", e)
    exit()

# ---------------------------
# Ask user for row
# ---------------------------
try:
    row_num = int(input("Enter row number to test: "))
except:
    print("❌ Invalid input")
    exit()

if row_num < 0 or row_num >= len(df):
    print("❌ Row out of range")
    exit()

# ---------------------------
# Extract row
# ---------------------------
row = df.iloc[row_num]
url = row["URL"]

# Expected values (drop URL + label)
expected = row.drop(["URL", "label"]).to_dict()

# ---------------------------
# Run feature extraction
# ---------------------------
actual = extract_features(url)

# ---------------------------
# Compare
# ---------------------------
print(f"\n🔍 Testing URL: {url}\n")
print("=== FEATURE COMPARISON ===\n")

pass_count = 0
fail_count = 0

for key in expected:
    exp = expected[key]
    act = actual.get(key)

    # Handle float comparison safely
    if isinstance(exp, float):
        match = abs(act - exp) < 0.01
    else:
        match = act == exp

    if match:
        print(f"✔ {key}: PASS ({act})")
        pass_count += 1
    else:
        print(f"❌ {key}: FAIL (Expected {exp}, Got {act})")
        fail_count += 1

# ---------------------------
# Summary
# ---------------------------
print("\n=== SUMMARY ===")
print(f"✔ Passed: {pass_count}")
print(f"❌ Failed: {fail_count}")
print("================\n")
