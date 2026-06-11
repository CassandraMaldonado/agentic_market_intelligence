from fastapi import FastAPI
from pydantic import BaseModel

from app.agents.research_agent import ResearchAgent
from app.agents.claims_agent import ClaimsAgent
from app.agents.sentiment_agent import SentimentAgent
from app.agents.forecast_agent import ForecastAgent
from app.agents.strategy_agent import StrategyAgent
from app.agents.evaluator_agent import EvaluatorAgent


app = FastAPI(
    title="Agentic Market Intelligence Platform",
    description="Source competitive intelligence using agents, RAG, forecasting, and evaluation.",
    version="0.1.0",
)


class IntelligenceRequest(BaseModel):
    question: str
    market_context: str | None = None


@app.get("/")
def health_check():
    return {"status": "ok", "service": "agentic-market-intelligence-platform"}


@app.post("/analyze")
def analyze_market(request: IntelligenceRequest):
    research = ResearchAgent().run(request.question)
    claims = ClaimsAgent().run(research["summary"])
    sentiment = SentimentAgent().run(research["summary"])
    forecast = ForecastAgent().run()
    strategy = StrategyAgent().run(
        question=request.question,
        claims=claims,
        sentiment=sentiment,
        forecast=forecast,
    )
    evaluation = EvaluatorAgent().run(strategy)

    return {
        "question": request.question,
        "research": research,
        "claims": claims,
        "sentiment": sentiment,
        "forecast": forecast,
        "strategy": strategy,
        "evaluation": evaluation,
    }
