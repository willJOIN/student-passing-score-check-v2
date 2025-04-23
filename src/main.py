from aluno import Aluno

# todo pytest
# todo pattern
# todo SOLID

def main():
    obj_aluno = Aluno()

    obj_aluno.set_nota1(float(input("Digite a primeira nota:\n")))

    obj_aluno.set_nota2(float(input("Digite a segunda nota:\n")))

    obj_aluno.set_media_notas(obj_aluno.nota1, obj_aluno.nota2)

    obj_aluno.set_conceito(obj_aluno.media_notas)

    obj_aluno.set_status_aprovacao(obj_aluno.conceito)

    print("Nota média:", obj_aluno.media_notas)

    print("Conceito:", obj_aluno.conceito)

if __name__ == "__main__":
    main()
