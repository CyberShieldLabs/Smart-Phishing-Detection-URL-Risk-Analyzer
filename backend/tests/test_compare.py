import sys
import os
import pandas as pd

# ---------------------------
# FIX IMPORT PATH
# ---------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.feature_extractor import extract_features


# ---------------------------
# FEATURE ORDER (LOCKED)
# ---------------------------
FEATURE_NAMES = [
    "URLLength", "DomainLength", "IsDomainIP", "TLDLength", "NoOfSubDomain",
    "NoOfLettersInURL", "LetterRatioInURL", "NoOfDigitsInURL", "DigitRatioInURL",
    "NoOfEqualsInURL", "NoOfQMarkInURL", "NoOfAmpersandInURL",
    "NoOfOtherSpecialCharsInURL", "SpecialCharRatioInURL",
    "HasObfuscation", "NoOfObfuscatedChar", "ObfuscationRatio",
    "IsHTTPS", "Bank", "Pay", "Crypto",
    "SuspiciousWords", "URLDepth", "AvgTokenLength"
]


# ---------------------------
# LOAD DATASET
# ---------------------------
try:
    file_path = os.path.join(os.path.dirname(__file__), "final_dataset.csv")
    df = pd.read_csv(file_path)
    print(f"\n✅ Dataset Loaded: {len(df)} rows\n")
except Exception as e:
    print("❌ Error loading CSV:", e)
    exit()


# ---------------------------
# USER INPUT
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
# GET ROW DATA
# ---------------------------
row = df.iloc[row_num]
url = row["URL"]

# Expected values (dict)
expected = {key: row[key] for key in FEATURE_NAMES}


# ---------------------------
# RUN EXTRACTION
# ---------------------------
actual_output = extract_features(url)
actual_features = actual_output["features"]


# ---------------------------
# VALIDATION
# ---------------------------
if len(actual_features) != len(FEATURE_NAMES):
    print("❌ Feature length mismatch")
    print(f"Expected: {len(FEATURE_NAMES)}, Got: {len(actual_features)}")
    exit()


# ---------------------------
# COMPARE
# ---------------------------
print(f"\n🔍 Testing URL: {url}\n")
print("=== FEATURE COMPARISON ===\n")

pass_count = 0
fail_count = 0

for key, act in zip(FEATURE_NAMES, actual_features):
    exp = expected[key]

    # Float safe comparison
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
# SUMMARY
# ---------------------------
print("\n=== SUMMARY ===")
print(f"✔ Passed: {pass_count}")
print(f"❌ Failed: {fail_count}")

if fail_count == 0:
    print("🔥 PERFECT MATCH — PIPELINE CONSISTENT")
else:
    print("⚠️ Some mismatches found — check feature logic")

print("================\n")
