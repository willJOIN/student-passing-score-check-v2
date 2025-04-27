from approval_strategy import ApprovalStrategy


class ConceitoStrategy(ApprovalStrategy):
    def calcula_conceito(self, media_notas: float) -> str:
        match media_notas:
            case m if 9.0 <= m <= 10.0:
                return 'a'
            case m if 7.5 <= m < 9.0:
                return 'b'
            case m if 6.0 <= m < 7.5:
                return 'c'
            case m if 4.0 <= m < 6.0:
                return 'd'
            case m if 0.0 <= m < 4.0:
                return 'e'
            case _:
                return ''

    def is_approved(self, conceito: str) -> bool:
        return conceito in ['a', 'b', 'c']