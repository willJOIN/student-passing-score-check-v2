from validador_notas import ValidadorDeNotas
from calculadora_de_notas import CalculadoraDeNotas
from conceito_strategy import ConceitoStrategy

class ErroNotaInvalida(Exception):
    pass

class Aluno:
    # Atributos de instância, agora cada aluno possui seus próprios dados.
    def __init__(self, conceito_strategy: ConceitoStrategy) -> None:
        self.nota1: float = 0.0
        self.nota2: float = 0.0
        self.media_notas: float = 0.0
        self.conceito: str = ''
        self.status_aprovacao: bool = False
        self.conceito_strategy = conceito_strategy # Injeção de dependência de uma estratégia de conceito

    def set_nota1(self, nota1: float) -> None:
        if not ValidadorDeNotas.valida_nota(nota1):  # Realiza a validação de notas em outra classe.
            raise ErroNotaInvalida("Nota inválida")
        self.nota1 = nota1

    def set_nota2(self, nota2: float) -> None:
        if not ValidadorDeNotas.valida_nota(nota2): # Realiza a validação de notas em outra classe.
            raise ErroNotaInvalida("Nota inválida")
        self.nota2 = nota2

    def set_media_notas(self) -> None:
        self.media_notas = CalculadoraDeNotas.calcula_media(self.nota1, self.nota2) # Realiza o calculo da média em outra classe.

    def set_conceito(self) -> None:
        self.conceito = self.conceito_strategy.calcula_conceito(self.media_notas)

    def set_status_aprovacao(self) -> None:
        self.status_aprovacao = self.conceito_strategy.is_approved(self.conceito)
