import csv
import re
from urllib.parse import urlparse


# ---------------------------
# FEATURE NAMES (LOCKED)
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
# FEATURE EXTRACTION
# ---------------------------
def extract_features(url):
    parsed = urlparse(url)

    url_no_scheme = re.sub(r"^https?://", "", url)

    host = parsed.netloc.lower()
    core_domain = host[4:] if host.startswith("www.") else host

    parts = core_domain.split(".")
    tld = parts[-1] if parts else ""

    URLLength = len(url_no_scheme)
    DomainLength = len(core_domain)

    IsDomainIP = 1 if re.match(r"\d+\.\d+\.\d+\.\d+", core_domain) else 0
    TLDLength = len(tld)
    NoOfSubDomain = max(len(parts) - 2, 0)

    letters = sum(c.isalpha() for c in url_no_scheme)
    digits = sum(c.isdigit() for c in url_no_scheme)

    LetterRatio = round(letters / URLLength, 3) if URLLength else 0
    DigitRatio = round(digits / URLLength, 3) if URLLength else 0

    eq = url_no_scheme.count("=")
    qm = url_no_scheme.count("?")
    amp = url_no_scheme.count("&")

    special = sum(1 for c in url_no_scheme if not c.isalnum())
    SpecialRatio = round(special / URLLength, 3) if URLLength else 0

    obf = re.findall(r"%[0-9A-Fa-f]{2}", url)
    HasObf = 1 if obf else 0
    NoOfObf = len(obf)
    ObfRatio = round(NoOfObf / URLLength, 3) if URLLength else 0

    IsHTTPS = 1 if url.startswith("https://") else 0

    lower_url = url.lower()

    Bank = int(any(k in lower_url for k in ["bank", "sbi", "hdfc", "icici"]))
    Pay = int(any(k in lower_url for k in ["pay", "upi", "payment"]))
    Crypto = int(any(k in lower_url for k in ["crypto", "btc", "bitcoin"]))

    SuspiciousWords = int(any(
        k in lower_url for k in ["login", "verify", "secure", "account", "update"]
    ))

    path_parts = [p for p in parsed.path.split("/") if p]
    URLDepth = len(path_parts)

    tokens = re.split(r"[./?=&-]", url_no_scheme)
    tokens = [t for t in tokens if t]

    AvgTokenLength = round(
        sum(len(t) for t in tokens) / len(tokens), 3
    ) if tokens else 0

    return [
        URLLength, DomainLength, IsDomainIP, TLDLength, NoOfSubDomain,
        letters, LetterRatio, digits, DigitRatio,
        eq, qm, amp, special, SpecialRatio,
        HasObf, NoOfObf, ObfRatio,
        IsHTTPS,
        Bank, Pay, Crypto,
        SuspiciousWords, URLDepth, AvgTokenLength
    ]


# ---------------------------
# BUILD DATASET FROM CLEAN FILE
# ---------------------------
def build_dataset(input_file="clean_urls.csv", output_file="final_dataset.csv"):

    processed = 0
    skipped = 0

    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)

        # Header
        writer.writerow(["URL"] + FEATURE_NAMES + ["label"])

        for i, row in enumerate(reader):
            try:
                url = row.get("URL", "").strip()
                label = row.get("label", "0").strip()

                if not url:
                    skipped += 1
                    continue

                features = extract_features(url)

                if len(features) != 24:
                    skipped += 1
                    continue

                writer.writerow([url] + features + [label])
                processed += 1

                if i < 5:
                    print(f"[DEBUG] {url}")

            except Exception:
                skipped += 1
                continue

    print("\n✅ FINAL DATASET CREATED")
    print(f"Processed: {processed}")
    print(f"Skipped: {skipped}")


# ---------------------------
# RUN
# ---------------------------
if __name__ == "__main__":
    print("🚀 Building final dataset...")
    build_dataset("clean_urls.csv", "final_dataset.csv")
