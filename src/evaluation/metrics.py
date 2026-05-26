def confidence_bucket(score: float) -> str:
    if score >= 0.8:
        return "high"
    if score >= 0.6:
        return "medium"
    return "low"


def source_grounding_score(num_sources: int, num_claims: int) -> float:
    if num_claims == 0:
        return 0.0
    return round(min(1.0, num_sources / num_claims), 2)
