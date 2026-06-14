import re
from app.agents.base import BaseAgent


class ClaimsAgent(BaseAgent):
    name = "claims_agent"

    CLAIM_KEYWORDS = [
        "sustainability",
        "refillable",
        "sensitive-skin",
        "value",
        "plant-based",
        "dermatologist-tested",
        "eco-friendly",
    ]

    def run(self, text: str) -> dict:
        text_lower = text.lower()
        claims = [claim for claim in self.CLAIM_KEYWORDS if claim in text_lower]

        return {
            "claims": claims,
            "claim_count": len(claims),
            "positioning_summary": self._summarize_positioning(claims),
        }

    def _summarize_positioning(self, claims: list[str]) -> str:
        if not claims:
            return "No strong claims detected."
        return f"Detected positioning around: {', '.join(claims)}."
