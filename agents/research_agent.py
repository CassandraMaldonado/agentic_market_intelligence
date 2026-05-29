from app.agents.base import BaseAgent


class ResearchAgent(BaseAgent):
    name = "research_agent"

    def run(self, question: str) -> dict:
        # Placeholder for retrieval/web ingestion.
        # Future version: call search APIs, scrape approved public pages, and retrieve vector chunks.
        return {
            "question": question,
            "summary": (
                "Competitor messaging shows increased emphasis on sustainability, refillable packaging, "
                "sensitive-skin positioning, and value-based bundles."
            ),
            "sources": [
                {"source": "sample_product_page", "relevance": 0.91},
                {"source": "sample_reviews", "relevance": 0.87},
            ],
        }
