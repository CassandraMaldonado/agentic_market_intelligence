from app.agents.base import BaseAgent


class StrategyAgent(BaseAgent):
    name = "strategy_agent"

    def run(self, question: str, claims: dict, sentiment: dict, forecast: dict) -> dict:
        detected_claims = claims.get("claims", [])
        trend = forecast.get("trend_direction", "unknown")
        sentiment_label = sentiment.get("interpretation", "unknown")

        recommendation = (
            "Prioritize sustainability, refillable packaging and sensitive skin messaging. "
            "Use value framing carefully because price sensitivity appears present."
        )

        evidence = [
            f"Detected claims: {', '.join(detected_claims) if detected_claims else 'none'}",
            f"Sentiment interpretation: {sentiment_label}",
            f"Market signal forecast direction: {trend}",
        ]

        confidence = 0.82 if detected_claims and trend == "upward" else 0.65

        return {
            "question": question,
            "recommendation": recommendation,
            "evidence": evidence,
            "confidence": confidence,
            "next_best_actions": [
                "Validate claim performance against review-level sentiment.",
                "Track competitor pricing and bundles weekly.",
                "Add source-level citations before executive reporting.",
            ],
        }
