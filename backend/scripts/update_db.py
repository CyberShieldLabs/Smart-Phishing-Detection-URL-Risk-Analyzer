import os
import urllib.request
from urllib.parse import urlparse


# ---------------------------
# CONFIG
# ---------------------------
OPENPHISH_URL = "https://raw.githubusercontent.com/openphish/public_feed/main/feed.txt"
URLHAUS_URL = "https://urlhaus.abuse.ch/downloads/text/"

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")

FINAL_DB = os.path.join(DATA_DIR, "threat_db.txt")
TEMP_DB = os.path.join(DATA_DIR, "threat_db_temp.txt")


# ---------------------------
# DOWNLOAD FUNCTION
# ---------------------------
def download_feed(url):
    print(f"⬇️ Downloading: {url}")
    try:
        with urllib.request.urlopen(url, timeout=15) as response:
            return response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"❌ Failed to download {url}: {e}")
        return ""


# ---------------------------
# EXTRACT DOMAIN
# ---------------------------
def extract_domain(url):
    try:
        parsed = urlparse(url.strip())
        domain = parsed.netloc.lower()

        # remove port if exists
        if ":" in domain:
            domain = domain.split(":")[0]

        # remove www
        if domain.startswith("www."):
            domain = domain[4:]

        return domain
    except:
        return ""


# ---------------------------
# PROCESS FEED
# ---------------------------
def process_feed(raw_data):
    domains = set()

    for line in raw_data.splitlines():
        line = line.strip()

        # skip empty or comments
        if not line or line.startswith("#"):
            continue

        domain = extract_domain(line)

        if domain and "." in domain:
            domains.add(domain)

    return domains


# ---------------------------
# MAIN FUNCTION
# ---------------------------
def main():
    print("\n🚀 Starting Threat DB Update...\n")

    # Ensure data directory exists
    os.makedirs(DATA_DIR, exist_ok=True)

    all_domains = set()

    # Download feeds
    openphish_data = download_feed(OPENPHISH_URL)
    urlhaus_data = download_feed(URLHAUS_URL)

    # Process feeds
    all_domains.update(process_feed(openphish_data))
    all_domains.update(process_feed(urlhaus_data))

    print(f"📊 Total unique domains: {len(all_domains)}")

    if not all_domains:
        print("⚠️ No data fetched. Keeping existing DB.")
        return

    # Write temp file
    try:
        with open(TEMP_DB, "w") as f:
            for domain in sorted(all_domains):
                f.write(domain + "\n")

        # Safe replace (atomic)
        os.replace(TEMP_DB, FINAL_DB)

        print(f"✅ Database updated successfully: {FINAL_DB}")

    except Exception as e:
        print(f"❌ Error writing DB: {e}")


# ---------------------------
# ENTRY POINT
# ---------------------------
if __name__ == "__main__":
    main()
