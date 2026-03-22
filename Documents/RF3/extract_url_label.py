import csv
import re


def extract_url_label(input_file="dataset.csv", output_file="clean_urls.csv"):

    extracted = 0
    skipped = 0

    with open(input_file, "r", encoding="utf-8-sig", errors="ignore") as infile, \
         open(output_file, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)

        print("Columns detected:", reader.fieldnames)

        writer = csv.writer(outfile)
        writer.writerow(["URL", "label"])

        for i, row in enumerate(reader):
            try:
                # ---------------------------
                # GET URL SAFELY
                # ---------------------------
                url = row.get("URL")

                # fallback if broken parsing
                if not url or "http" not in url:
                    raw_line = ",".join(str(v) for v in row.values())
                    match = re.search(r"https?://[^\s,]+", raw_line)
                    url = match.group(0) if match else None

                if not url:
                    skipped += 1
                    continue

                # ---------------------------
                # GET LABEL SAFELY
                # ---------------------------
                label = row.get("label")

                if label not in ["0", "1"]:
                    raw_line = ",".join(str(v) for v in row.values())
                    last_val = raw_line.strip().split(",")[-1]
                    label = last_val if last_val in ["0", "1"] else "0"

                # ---------------------------
                # WRITE CLEAN ROW
                # ---------------------------
                writer.writerow([url, label])
                extracted += 1

                if i < 5:
                    print(f"[DEBUG] {url} -> {label}")

            except Exception:
                skipped += 1
                continue

    print("\n✅ CLEAN DATASET CREATED")
    print(f"Extracted: {extracted}")
    print(f"Skipped: {skipped}")


if __name__ == "__main__":
    print("🚀 Extracting URL + Label...")
    extract_url_label("dataset.csv", "clean_urls.csv")
