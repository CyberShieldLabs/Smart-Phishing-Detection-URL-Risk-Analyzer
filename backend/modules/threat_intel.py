import os

# ---------------------------
# Load DB once
# ---------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "data", "threat_db.txt")

THREAT_DB = set()


def load_threat_db():
    global THREAT_DB

    if not os.path.exists(DB_PATH):
        print("⚠️ Threat DB not found. Run update_db.py first.")
        return

    with open(DB_PATH, "r") as f:
        THREAT_DB = set(line.strip() for line in f if line.strip())

    print(f"✅ Threat DB loaded: {len(THREAT_DB)} entries")


# Load at startup
load_threat_db()


# ---------------------------
# Main function
# ---------------------------
def check_threat(data: dict):
    """
    Input:
        {
            "domain": "example.com"
        }

    Output:
        {
            "status": "success",
            "is_malicious": True/False,
            "confidence": "high/low",
            "source": "local_db"
        }
    """

    # ---------------------------
    # Validate input
    # ---------------------------
    if not isinstance(data, dict):
        return {
            "status": "error",
            "message": "Invalid input format"
        }

    domain = data.get("domain")

    if not domain or not isinstance(domain, str):
        return {
            "status": "error",
            "message": "Invalid or missing domain"
        }

    domain = domain.lower().strip()

    # ---------------------------
    # Check in DB
    # ---------------------------
    if domain in THREAT_DB:
        return {
            "status": "success",
            "is_malicious": True,
            "confidence": "high",
            "source": "local_db"
        }

    return {
        "status": "success",
        "is_malicious": False,
        "confidence": "low",
        "source": "local_db"
    }
