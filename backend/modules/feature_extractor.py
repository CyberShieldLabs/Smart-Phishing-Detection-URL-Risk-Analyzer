from urllib.parse import urlparse
import re


def extract_features(clean_url: str):
    """
    Feature Extraction Engine (FINAL)

    Input:
        clean_url → validated URL (http/https, normalized)

    Output:
        dict → feature vector (exact order for ML model)
    """

    parsed = urlparse(clean_url)

    # ---------------------------
    # 🔥 STEP 1: Remove scheme
    # ---------------------------
    url_no_scheme = clean_url.replace("https://", "").replace("http://", "")

    # ---------------------------
    # 🔥 STEP 2: Host handling
    # ---------------------------
    host = parsed.netloc  # includes www

    # For calculations (remove www)
    if host.startswith("www."):
        core_domain = host[4:]
    else:
        core_domain = host

    parts = core_domain.split(".")
    tld = parts[-1]

    # ---------------------------
    # 🔥 STEP 3: URL Length
    # ---------------------------
    URLLength = len(url_no_scheme)

    # ---------------------------
    # Domain Length (WITH www)
    # ---------------------------
    DomainLength = len(host)

    # ---------------------------
    # IP Check
    # ---------------------------
    IsDomainIP = 1 if re.match(r"\d+\.\d+\.\d+\.\d+", host) else 0

    # ---------------------------
    # TLD Length
    # ---------------------------
    TLDLength = len(tld)

    # ---------------------------
    # Subdomain Count
    # ---------------------------
    NoOfSubDomain = len(parts) - 2
    if NoOfSubDomain < 0:
        NoOfSubDomain = 0

    # ---------------------------
    # 🔥 STEP 4: Letters (IMPORTANT FIX)
    # Remove ONLY last TLD
    # ---------------------------
    domain_without_tld = ".".join(parts[:-1])

    NoOfLettersInURL = sum(c.isalpha() for c in domain_without_tld)

    LetterRatioInURL = round(NoOfLettersInURL / URLLength, 3)

    # ---------------------------
    # Digits
    # ---------------------------
    NoOfDegitsInURL = sum(c.isdigit() for c in url_no_scheme)

    DegitRatioInURL = round(NoOfDegitsInURL / URLLength, 3)

    # ---------------------------
    # Query-based features
    # ---------------------------
    NoOfEqualsInURL = url_no_scheme.count("=")
    NoOfQMarkInURL = url_no_scheme.count("?")
    NoOfAmpersandInURL = url_no_scheme.count("&")

    # ---------------------------
    # 🔥 STEP 5: Special Characters (IMPORTANT FIX)
    # Count ONLY in core domain (no www)
    # ---------------------------
    NoOfOtherSpecialCharsInURL = sum(
        1 for c in core_domain if c in [".", "-"]
    )

    SpacialCharRatioInURL = round(
        NoOfOtherSpecialCharsInURL / URLLength, 3
    )

    # ---------------------------
    # HTTPS
    # ---------------------------
    IsHTTPS = 1 if clean_url.startswith("https://") else 0

    # ---------------------------
    # Obfuscation
    # ---------------------------
    obf = re.findall(r"%[0-9A-Fa-f]{2}", clean_url)
    NoOfObfuscatedChar = len(obf)
    HasObfuscation = 1 if obf else 0

    ObfuscationRatio = round(
        NoOfObfuscatedChar / URLLength, 3
    )

    # ---------------------------
    # Placeholder Features (dataset-specific)
    # ---------------------------
    CharContinuationRate = 1.0  # keep constant for now
    URLCharProb = 0.0           # advanced feature (skip for now)

    # ---------------------------
    # Keyword-based features
    # ---------------------------
    lower_url = clean_url.lower()

    Bank = 1 if "bank" in lower_url else 0
    Pay = 1 if "pay" in lower_url else 0
    Crypto = 1 if "crypto" in lower_url else 0

    # ---------------------------
    # FINAL FEATURE DICT (ORDER MATTERS)
    # ---------------------------
    return {
        "URLLength": URLLength,
        "DomainLength": DomainLength,
        "IsDomainIP": IsDomainIP,
        "CharContinuationRate": CharContinuationRate,
        "URLCharProb": URLCharProb,
        "TLDLength": TLDLength,
        "NoOfSubDomain": NoOfSubDomain,
        "HasObfuscation": HasObfuscation,
        "NoOfObfuscatedChar": NoOfObfuscatedChar,
        "ObfuscationRatio": ObfuscationRatio,
        "NoOfLettersInURL": NoOfLettersInURL,
        "LetterRatioInURL": LetterRatioInURL,
        "NoOfDegitsInURL": NoOfDegitsInURL,
        "DegitRatioInURL": DegitRatioInURL,
        "NoOfEqualsInURL": NoOfEqualsInURL,
        "NoOfQMarkInURL": NoOfQMarkInURL,
        "NoOfAmpersandInURL": NoOfAmpersandInURL,
        "NoOfOtherSpecialCharsInURL": NoOfOtherSpecialCharsInURL,
        "SpacialCharRatioInURL": SpacialCharRatioInURL,
        "IsHTTPS": IsHTTPS,
        "Bank": Bank,
        "Pay": Pay,
        "Crypto": Crypto,
    }
