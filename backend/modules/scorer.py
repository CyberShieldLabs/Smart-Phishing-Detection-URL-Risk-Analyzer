def calculate_risk_score(features):
    score = 0

    if features.get("has_ip"):
        score += 30

    if features.get("url_length") > 75:
        score += 20

    if features.get("has_at_symbol"):
        score += 15

    if features.get("has_hyphen"):
        score += 10

    if features.get("num_dots") > 3:
        score += 15

    return score


def get_risk_level(score):
    if score < 30:
        return "Low Risk"
    elif score < 60:
        return "Medium Risk"
    else:
        return "High Risk"