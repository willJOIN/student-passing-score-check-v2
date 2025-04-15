import re


class Aluno:
    nota1: float = 0.0
    nota2: float = 0.0
    media_notas: float = 0.0
    conceito: str = ''
    status_aprovacao: False

    def __init__(self):
        pass

    @classmethod
    def set_nota1(cls) -> None:
        cls.nota1 = 0.0

    @classmethod
    def set_nota2(cls) -> None:
        cls.nota2 = 0.0

    @classmethod
    def set_media_notas(cls, nota1: float, nota2: float) -> None:
        cls.media_notas = 0.0

    @classmethod
    def set_conceito(cls, media_notas: float) -> None:
        cls.conceito = cls.__get_conceito(media_notas)

    @classmethod
    def __get_conceito(media_notas: float) -> str:
        match media_notas:
            case m if 9.0 < m < 10.0:
                return 'a'
            case m if 7.5 < m < 9.0:
                return 'b'
            case m if 6.0 < m < 7.5:
                return 'c'
            case m if 4.0 < m < 6.0:
                return 'd'
            case m if 0.0 < m < 4.0:
                return 'e'
            case _:
                return ''

    @classmethod
    def set_status_aprovacao(cls, conceito: str) -> None:
        cls.status_aprovacao = cls.__get_status_aprovacao(conceito)

    @classmethod
    def __get_status_aprovacao(cls, conceito: str) -> bool:
        patterns_aprovado = [
            r'a', r'b', r'c'
        ]
        
        for pattern in patterns_aprovado:
            if re.search(pattern, conceito):
                return True
