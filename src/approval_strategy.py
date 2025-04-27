from abc import ABC, abstractmethod


class ApprovalStrategy(ABC):
    @abstractmethod
    def calcula_conceito(self, media_notas: float) -> str:
        pass

    @abstractmethod
    def is_approved(self, conceito: str) -> bool:
        pass
