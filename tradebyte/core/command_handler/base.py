from abc import ABC, abstractmethod
from typing import Dict, Any, Callable

class Command(ABC):
    """Base command interface"""
    @property
    @abstractmethod
    def help_text(self) -> str:
        pass

    @abstractmethod
    def execute(self, args: Dict[str, Any]) -> Any:
        pass

class AsyncCommand(Command):
    """For async operations like exchange commands"""
    @abstractmethod
    async def execute(self, args: Dict[str, Any]) -> Any:
        pass