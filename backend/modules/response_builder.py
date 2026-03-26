from datetime import datetime, timezone


def build_response(url, validation, features, ml_prediction, threat_intel, risk):
    """
    Builds the final standardized JSON response returned to the frontend.
    All modules pass their results here and this function assembles the unified response.
    """
    return {
        "url": url,
        "timestamp": datetime.now(timezone.utc).isoformat(),

        "validation": {
            "is_valid":  validation.get("is_valid", False),
            "protocol":  validation.get("protocol", ""),
            "domain":    validation.get("domain", "")
        },

        "features": {
            "url_length":          features.get("url_length", 0),
            "hyphen_count":        features.get("hyphen_count", 0),
            "suspicious_keywords": features.get("suspicious_keywords", []),
            "tld":                 features.get("tld", ""),
            "has_ip_address":      features.get("has_ip_address", False),
            "has_at_symbol":       features.get("has_at_symbol", False),
            "subdomain_count":     features.get("subdomain_count", 0),
            "is_https":            features.get("is_https", False),
            "special_char_count":  features.get("special_char_count", 0)
        },

        "ml_prediction": {
            "score":      ml_prediction.get("score", 0),
            "label":      ml_prediction.get("label", "unknown"),
            "confidence": ml_prediction.get("confidence", "low")
        },

        "threat_intelligence": {
            "virustotal": {
                "found":          threat_intel.get("virustotal", {}).get("found", False),
                "malicious_count": threat_intel.get("virustotal", {}).get("malicious_count", 0),
                "total_engines":  threat_intel.get("virustotal", {}).get("total_engines", 0)
            },
            "phishtank": {
                "found":    threat_intel.get("phishtank", {}).get("found", False),
                "verified": threat_intel.get("phishtank", {}).get("verified", False)
            },
            "openphish": {
                "found": threat_intel.get("openphish", {}).get("found", False)
            }
        },

        "risk": {
            "score":   risk.get("score", 0),
            "level":   risk.get("level", "Unknown"),
            "reasons": risk.get("reasons", [])
        }
    }


def build_error_response(url, message):
    """
    Builds a standardized error response when analysis fails at any stage.
    """
    return {
        "url":       url,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "error":     True,
        "message":   message
    }