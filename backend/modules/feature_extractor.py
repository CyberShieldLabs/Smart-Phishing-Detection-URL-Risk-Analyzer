from urllib.parse import urlparse
import re


# ---------------------------
# NEW: Domain Extraction Function
# ---------------------------
def extract_domain_from_url(clean_url: str):
    """
    Extract domain for threat intel

    Example:
    https://www.google.com → google.com
    http://1.2.3.4:8080 → 1.2.3.4
    """
    parsed = urlparse(clean_url)
    domain = parsed.netloc.lower()

    # remove port
    if ":" in domain:
        domain = domain.split(":")[0]

    # remove www
    if domain.startswith("www."):
        domain = domain[4:]

    return domain


# ---------------------------
# MAIN FEATURE FUNCTION
# ---------------------------
def extract_features(clean_url: str):
    """
    Feature Extraction Engine

    Input:
        clean_url → validated URL

    Output:
        {
          "features": {...},
          "domain": "example.com"
        }
    """

    parsed = urlparse(clean_url)

    # ---------------------------
    # STEP 1: Remove scheme
    # ---------------------------
    url_no_scheme = clean_url.replace("https://", "").replace("http://", "")

    # ---------------------------
    # STEP 2: Host handling
    # ---------------------------
    host = parsed.netloc  # includes www

    if host.startswith("www."):
        core_domain = host[4:]
    else:
        core_domain = host

    parts = core_domain.split(".")
    tld = parts[-1]

    # ---------------------------
    # STEP 3: URL Length
    # ---------------------------
    URLLength = len(url_no_scheme)

    # ---------------------------
    # Domain Length
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
    # Letters
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
    # Query features
    # ---------------------------
    NoOfEqualsInURL = url_no_scheme.count("=")
    NoOfQMarkInURL = url_no_scheme.count("?")
    NoOfAmpersandInURL = url_no_scheme.count("&")

    # ---------------------------
    # Special Characters
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
    # Placeholder Features
    # ---------------------------
    CharContinuationRate = 1.0
    URLCharProb = 0.0

    # ---------------------------
    # Keyword Features
    # ---------------------------
    lower_url = clean_url.lower()

    Bank = 1 if "bank" in lower_url else 0
    Pay = 1 if "pay" in lower_url else 0
    Crypto = 1 if "crypto" in lower_url else 0

    # ---------------------------
    # NEW: Extract domain
    # ---------------------------
    domain = extract_domain_from_url(clean_url)

    # ---------------------------
    # FINAL OUTPUT
    # ---------------------------
    return {
        "features": {
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
        },
        "domain": domain
    }
