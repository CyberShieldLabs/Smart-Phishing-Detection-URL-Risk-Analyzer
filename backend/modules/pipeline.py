from modules.validator import validate_url_input
from modules.feature_extractor import extract_features
from modules.threat_intel import check_threat


def process_url(data: dict):
    """
    Main pipeline function

    Input:
        {
            "url": "https://example.com"
        }

    Output:
        JSON result
    """

    # ---------------------------
    # STEP 1: Validation
    # ---------------------------
    validation_result = validate_url_input(data)

    if validation_result["status"] == "error":
        return validation_result

    clean_url = validation_result["clean_url"]

    # ---------------------------
    # STEP 2: Feature Extraction
    # ---------------------------
    extractor_output = extract_features(clean_url)

    features = extractor_output["features"]
    domain = extractor_output["domain"]

    # ---------------------------
    # STEP 3: Threat Intelligence
    # ---------------------------
    threat_output = check_threat({
        "domain": domain
    })

    # ---------------------------
    # DEBUG PRINT (for now)
    # ---------------------------
    print("\n=== PIPELINE DEBUG ===")
    print("Clean URL:", clean_url)
    print("Domain:", domain)
    print("Features:", features)
    print("Threat Intel:", threat_output)
    print("======================\n")

    # ---------------------------
    # FINAL OUTPUT (TEMP)
    # ---------------------------
    return {
        "status": "success",
        "clean_url": clean_url,
        "domain": domain,
        "features": features,
        "threat_intel": threat_output
    }
