import streamlit as st
import pandas as pd
import plotly.express as px

from app.agents.strategy_agent import StrategyAgent
from app.agents.sentiment_agent import SentimentAgent
from app.agents.forecast_agent import ForecastAgent


st.set_page_config(
    page_title="Agentic Market Intelligence",
    page_icon="📊",
    layout="wide",
)

st.title("Agentic Market Intelligence Platform")
st.caption("RAG + agents + forecasting + sentiment analysis for competitive intelligence")

question = st.text_input(
    "Ask a market intelligence question",
    value="Which competitor claims are gaining traction?",
)

sample_text = st.text_area(
    "Market signal text",
    value=(
        "Customers mention sustainability, refillable packaging, sensitive skin, and better value. "
        "Some reviews complain about price increases but sentiment around product quality is improving."
    ),
    height=120,
)

if st.button("Run Analysis"):
    sentiment = SentimentAgent().run(sample_text)
    forecast = ForecastAgent().run()
    strategy = StrategyAgent().run(
        question=question,
        claims={"claims": ["sustainability", "refillable packaging", "sensitive skin"]},
        sentiment=sentiment,
        forecast=forecast,
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Sentiment Score", sentiment["sentiment_score"])
    col2.metric("Forecast Direction", forecast["trend_direction"])
    col3.metric("Confidence", strategy["confidence"])

    st.subheader("Recommendation")
    st.write(strategy["recommendation"])

    st.subheader("Evidence")
    for item in strategy["evidence"]:
        st.markdown(f"- {item}")

    df = pd.DataFrame(forecast["forecast_points"])
    fig = px.line(df, x="period", y="value", title="Market Signal Forecast")
    st.plotly_chart(fig, use_container_width=True)
