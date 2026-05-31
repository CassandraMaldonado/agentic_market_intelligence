from app.agents.base import BaseAgent


class SentimentAgent(BaseAgent):
    name = "sentiment_agent"

    POSITIVE_TERMS = {"improving", "better", "quality", "love", "great", "effective", "gentle"}
    NEGATIVE_TERMS = {"complain", "price", "expensive", "bad", "poor", "issue", "problem"}

    def run(self, text: str) -> dict:
        tokens = set(text.lower().replace(".", "").replace(",", "").split())
        positive_hits = len(tokens.intersection(self.POSITIVE_TERMS))
        negative_hits = len(tokens.intersection(self.NEGATIVE_TERMS))

        raw_score = positive_hits - negative_hits
        normalized = max(-1, min(1, raw_score / 5))

        return {
            "sentiment_score": round(normalized, 2),
            "positive_hits": positive_hits,
            "negative_hits": negative_hits,
            "interpretation": self._interpret(normalized),
        }

    def _interpret(self, score: float) -> str:
        if score > 0.2:
            return "positive"
        if score < -0.2:
            return "negative"
        return "mixed_or_neutral"
