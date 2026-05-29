from app.agents.base import BaseAgent


class EvaluatorAgent(BaseAgent):
    name = "evaluator_agent"

    def run(self, strategy_output: dict) -> dict:
        evidence = strategy_output.get("evidence", [])
        confidence = strategy_output.get("confidence", 0)

        grounding_score = min(1.0, len(evidence) / 3)
        risk_flags = []

        if confidence < 0.7:
            risk_flags.append("low_confidence")
        if grounding_score < 0.8:
            risk_flags.append("limited_evidence")

        return {
            "grounding_score": round(grounding_score, 2),
            "hallucination_risk": "low" if grounding_score >= 0.8 else "medium",
            "risk_flags": risk_flags,
        }
