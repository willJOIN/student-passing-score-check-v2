from aluno import Aluno
from conceito_strategy import ConceitoStrategy

def main():

    conceito_strategy = ConceitoStrategy()

    obj_aluno = Aluno(conceito_strategy)

    obj_aluno.set_nota1(float(input("Digite a primeira nota:\n")))

    obj_aluno.set_nota2(float(input("Digite a segunda nota:\n")))

    obj_aluno.set_media_notas()

    obj_aluno.set_conceito()

    obj_aluno.set_status_aprovacao()

    print("Nota média:", obj_aluno.media_notas)

    print("Conceito:", obj_aluno.conceito)

if __name__ == "__main__":
    main()