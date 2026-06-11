from app.agents.base import BaseAgent


class ForecastAgent(BaseAgent):
    name = "forecast_agent"

    def run(self) -> dict:
        # Baseline deterministic forecast.
        historical = [42, 47, 51, 58, 63, 67]
        forecast = [72, 76, 81]

        return {
            "historical_points": [
                {"period": i + 1, "value": value} for i, value in enumerate(historical)
            ],
            "forecast_points": [
                {"period": i + 1, "value": value}
                for i, value in enumerate(historical + forecast)
            ],
            "trend_direction": "upward",
            "forecast_confidence": 0.74,
        }
