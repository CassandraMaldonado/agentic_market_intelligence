from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Agentic Market Intelligence Platform"
    environment: str = "development"
    vector_store_path: str = "data/vector_store"


settings = Settings()
