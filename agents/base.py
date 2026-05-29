from abc import ABC, abstractmethod
from typing import Any


class BaseAgent(ABC):
    name: str = "base_agent"

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> dict:
        raise NotImplementedError
