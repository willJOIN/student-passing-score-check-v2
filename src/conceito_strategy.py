from approval_strategy import ApprovalStrategy

class ConceitoApprovalStrategy(ApprovalStrategy):
    def is_approved(self, conceito: str) -> bool:
        return conceito in ['a', 'b', 'c']

