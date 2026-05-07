import os
from dotenv import load_dotenv

load_dotenv()

# ── API Keys ──────────────────────────────────────────────
VIRUSTOTAL_API_KEY  = os.getenv("VIRUSTOTAL_API_KEY", "")
PHISHTANK_API_KEY   = os.getenv("PHISHTANK_API_KEY", "")

# ── API Base URLs ─────────────────────────────────────────
VIRUSTOTAL_BASE_URL = "https://www.virustotal.com/api/v3"
PHISHTANK_BASE_URL  = "https://checkurl.phishtank.com/checkurl/"
OPENPHISH_FEED_URL  = "https://openphish.com/feed.txt"

# ── Risk Score Thresholds ─────────────────────────────────
RISK_THRESHOLD_SAFE       = 30   # 0  - 30  → Safe
RISK_THRESHOLD_SUSPICIOUS = 70   # 31 - 70  → Suspicious
                                  # 71 - 100 → Malicious

# ── ML Model Paths ────────────────────────────────────────
MODEL_PATH           = "models/phishing_url_model.pkl"
FEATURE_COLUMNS_PATH = "models/feature_columns.pkl"

# ── Threat Intel ──────────────────────────────────────────
THREAT_DB_PATH = "data/threat_db.txt"

# ── Flask ─────────────────────────────────────────────────
DEBUG = os.getenv("FLASK_DEBUG", "true").lower() == "true"
PORT  = int(os.getenv("PORT", 5000))