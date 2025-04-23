from abc import ABC, abstractmethod

class ApprovalStrategy(ABC):
    @abstractmethod
    def is_approved(self, conceito: str) -> bool:
        pass

