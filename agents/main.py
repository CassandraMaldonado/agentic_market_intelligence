


app = FastAPI(
    title="Agentic Market Intelligence Platform",
    description="Competitive intelligence using agents, RAG, forecasting and evaluation.",
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
