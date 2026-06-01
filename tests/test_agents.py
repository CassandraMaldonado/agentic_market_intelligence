from app.agents.sentiment_agent import SentimentAgent
from app.agents.claims_agent import ClaimsAgent
from app.agents.strategy_agent import StrategyAgent


def test_sentiment_agent_runs():
    result = SentimentAgent().run("Great quality but expensive")
    assert "sentiment_score" in result
    assert "interpretation" in result


def test_claims_agent_detects_claims():
    result = ClaimsAgent().run("This product has refillable packaging and sustainability benefits")
    assert "sustainability" in result["claims"]
    assert "refillable" in result["claims"]


def test_strategy_agent_returns_recommendation():
    result = StrategyAgent().run(
        question="What should we do?",
        claims={"claims": ["sustainability"]},
        sentiment={"interpretation": "positive"},
        forecast={"trend_direction": "upward"},
    )
    assert result["confidence"] >= 0.8
    assert "recommendation" in result
