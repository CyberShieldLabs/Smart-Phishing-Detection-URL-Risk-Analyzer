from urllib.parse import urlparse


def validate_url_input(data: dict):
    """
    Validation + Normalization Module

    Output format (STRICT for pipeline):

    Success:
    {
        "status": "success",
        "clean_url": "https://www.example.com"
    }

    Error:
    {
        "status": "error",
        "message": "error message"
    }
    """

    # ---------------------------
    # 1. Check JSON format
    # ---------------------------
    if not isinstance(data, dict):
        return {
            "status": "error",
            "message": "Invalid input format (JSON required)"
        }

    url = data.get("url")

    # ---------------------------
    # 2. Basic validation
    # ---------------------------
    if not url or not isinstance(url, str):
        return {
            "status": "error",
            "message": "URL must be a non-empty string"
        }

    url = url.strip()

    if url == "":
        return {
            "status": "error",
            "message": "URL cannot be empty"
        }

    if " " in url:
        return {
            "status": "error",
            "message": "URL must not contain spaces"
        }

    # ---------------------------
    # 3. Protocol validation
    # ---------------------------
    if not (url.startswith("http://") or url.startswith("https://")):
        return {
            "status": "error",
            "message": "Only http:// or https:// URLs are allowed"
        }

    # ---------------------------
    # 4. Parse URL
    # ---------------------------
    try:
        parsed = urlparse(url)
    except Exception:
        return {
            "status": "error",
            "message": "Invalid URL format"
        }

    if not parsed.netloc:
        return {
            "status": "error",
            "message": "Invalid domain"
        }

    netloc = parsed.netloc

    # ---------------------------
    # 5. Domain validation
    # ---------------------------
    if "." not in netloc:
        return {
            "status": "error",
            "message": "Invalid domain (missing TLD)"
        }

    if netloc.startswith(".") or netloc.endswith("."):
        return {
            "status": "error",
            "message": "Invalid domain format"
        }

    if ".." in netloc:
        return {
            "status": "error",
            "message": "Invalid domain (double dots)"
        }

    # ---------------------------
    # 6. Add www if missing
    # ---------------------------
    if not netloc.lower().startswith("www."):
        netloc = "www." + netloc

    # ---------------------------
    # 7. Rebuild URL
    # ---------------------------
    scheme = parsed.scheme
    path = parsed.path or ""
    query = f"?{parsed.query}" if parsed.query else ""

    clean_url = f"{scheme}://{netloc}{path}{query}"

    # ---------------------------
    # 8. Return success
    # ---------------------------
    return {
        "status": "success",
        "clean_url": clean_url
    }
