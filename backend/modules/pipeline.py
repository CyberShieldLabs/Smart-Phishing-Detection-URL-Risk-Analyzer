from modules.validator import validate_url_input
from modules.feature_extractor import extract_features
from modules.threat_intel import check_threat


def process_url(data: dict):
    """
    Pipeline with full debug visibility
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
    # DEBUG: ML INPUT (future)
    # ---------------------------
    print("\n=== ML INPUT (FEATURES) ===")
    print("Feature Count:", len(features))
    print("Features:", features)

    # ---------------------------
    # DEBUG: THREAT INTEL INPUT
    # ---------------------------
    print("\n=== THREAT INTEL INPUT ===")
    print("Domain:", domain)

    # ---------------------------
    # STEP 3: Threat Intelligence
    # ---------------------------
    threat_output = check_threat({
        "domain": domain
    })

    # ---------------------------
    # DEBUG: THREAT INTEL OUTPUT
    # ---------------------------
    print("\n=== THREAT INTEL OUTPUT ===")
    print(threat_output)

    print("\n============================\n")

    # ---------------------------
    # FINAL OUTPUT (TEMP)
    # ---------------------------
    return {
        "status": "success",
        "clean_url": clean_url,
        "domain": domain,
        "features": features,
        "feature_count": len(features),
        "threat_intel": threat_output
    }
