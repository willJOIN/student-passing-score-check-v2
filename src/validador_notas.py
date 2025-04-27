class ValidadorDeNotas:
    @staticmethod
    def valida_nota(nota: float) -> bool:
        return 0.0 <= nota <= 10.0