from urllib.parse import urlparse
import re


def extract_domain(clean_url: str) -> str:
    """
    Extract domain for threat intelligence
    Output: example.com
    """
    parsed = urlparse(clean_url)
    domain = parsed.netloc.lower()

    # remove port if exists
    if ":" in domain:
        domain = domain.split(":")[0]

    # remove www (guaranteed present)
    if domain.startswith("www."):
        domain = domain[4:]

    return domain


def extract_features(clean_url: str):
    """
    FINAL FEATURE EXTRACTOR (PIPELINE READY)

    INPUT:
        clean_url → validated URL (has http/https + www)

    OUTPUT:
        {
            "features": [fixed ordered list],
            "domain": "example.com"
        }
    """

    # ---------------------------
    # BASIC PARSING
    # ---------------------------
    parsed = urlparse(clean_url)

    # remove scheme only
    url_no_scheme = re.sub(r"^https?://", "", clean_url)

    host = parsed.netloc.lower()
    core_domain = host[4:]  # safe (www guaranteed)

    parts = core_domain.split(".")
    tld = parts[-1]

    URLLength = len(url_no_scheme)
    DomainLength = len(core_domain)

    # ---------------------------
    # DOMAIN FEATURES
    # ---------------------------
    IsDomainIP = 1 if re.match(r"\d+\.\d+\.\d+\.\d+", core_domain) else 0
    TLDLength = len(tld)
    NoOfSubDomain = max(len(parts) - 2, 0)

    # ---------------------------
    # CHARACTER FEATURES (FULL URL)
    # ---------------------------
    letters = sum(c.isalpha() for c in url_no_scheme)
    digits = sum(c.isdigit() for c in url_no_scheme)

    LetterRatio = round(letters / URLLength, 3) if URLLength else 0
    DigitRatio = round(digits / URLLength, 3) if URLLength else 0

    # ---------------------------
    # SPECIAL CHARACTERS
    # ---------------------------
    eq = url_no_scheme.count("=")
    qm = url_no_scheme.count("?")
    amp = url_no_scheme.count("&")

    special = sum(1 for c in url_no_scheme if not c.isalnum())
    SpecialRatio = round(special / URLLength, 3) if URLLength else 0

    # ---------------------------
    # OBFUSCATION
    # ---------------------------
    obf = re.findall(r"%[0-9A-Fa-f]{2}", clean_url)

    HasObf = 1 if obf else 0
    NoOfObf = len(obf)
    ObfRatio = round(NoOfObf / URLLength, 3) if URLLength else 0

    # ---------------------------
    # SECURITY
    # ---------------------------
    IsHTTPS = 1 if clean_url.startswith("https://") else 0

    # ---------------------------
    # KEYWORD FEATURES
    # ---------------------------
    lower_url = clean_url.lower()

    Bank = 1 if any(k in lower_url for k in ["bank", "sbi", "hdfc", "icici"]) else 0
    Pay = 1 if any(k in lower_url for k in ["pay", "upi", "payment"]) else 0
    Crypto = 1 if any(k in lower_url for k in ["crypto", "btc", "bitcoin"]) else 0

    SuspiciousWords = 1 if any(
        k in lower_url for k in ["login", "verify", "secure", "account", "update"]
    ) else 0

    # ---------------------------
    # ADVANCED FEATURES
    # ---------------------------
    # URL Depth
    path_parts = [p for p in parsed.path.split("/") if p]
    URLDepth = len(path_parts)

    # Avg Token Length
    tokens = re.split(r"[./?=&-]", url_no_scheme)
    tokens = [t for t in tokens if t]

    AvgTokenLength = round(
        sum(len(t) for t in tokens) / len(tokens), 3
    ) if tokens else 0

    # ---------------------------
    # FINAL FEATURE VECTOR (LOCKED ORDER)
    # ---------------------------
    features = [
        URLLength,
        DomainLength,
        IsDomainIP,
        TLDLength,
        NoOfSubDomain,

        letters,
        LetterRatio,
        digits,
        DigitRatio,

        eq,
        qm,
        amp,
        special,
        SpecialRatio,

        HasObf,
        NoOfObf,
        ObfRatio,

        IsHTTPS,

        Bank,
        Pay,
        Crypto,

        SuspiciousWords,
        URLDepth,
        AvgTokenLength
    ]

    # ---------------------------
    # DOMAIN FOR THREAT INTEL
    # ---------------------------
    domain = extract_domain(clean_url)

    return {
        "features": features,
        "domain": domain
    }
