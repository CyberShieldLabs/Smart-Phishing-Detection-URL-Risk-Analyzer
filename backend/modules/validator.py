from urllib.parse import urlparse

def validate_url_input(request_json):

    # 1. Check if "url" key exists in JSON
    if "url" not in request_json:
        return {
            "status": "error",
            "message": "URL field missing"
        }

    # 2. Get URL and remove extra spaces
    url = request_json["url"].strip()

    # 3. Check if empty
    if not url:
        return {
            "status": "error",
            "message": "URL cannot be empty"
        }

    # 4. Add https if missing
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # 5. Parse URL safely
    parsed = urlparse(url)
    domain = parsed.netloc

    # 6. Basic domain validation
    if not domain or "." not in domain:
        return {
            "status": "error",
            "message": "Invalid URL format"
        }

    # 7. Return clean URL
    return {
        "status": "success",
        "clean_url": url
    }
