import pytest
import aluno

def test_aluno_inicializa_corretamente():
    obj_aluno = aluno.Aluno()

    assert obj_aluno.nota1 == 0
    assert obj_aluno.nota2 == 0
    assert obj_aluno.media_notas == 0
    assert obj_aluno.conceito == ""
    assert obj_aluno.status_aprovacao == False

def test_aluno_seta_nota1_corretamente():
    obj_aluno = aluno.Aluno()

    obj_aluno.set_nota1(5.0)
    assert obj_aluno.nota1 == 5.0

def test_aluno_seta_nota2_corretamente():
    obj_aluno = aluno.Aluno()

    obj_aluno.set_nota2(5.0)
    assert obj_aluno.nota2 == 5.0

def test_aluno_set_media_notas_corretamente():
    obj_aluno = aluno.Aluno()

    obj_aluno.set_media_notas(2.0, 7.0)
    assert obj_aluno.media_notas == 4.5

def test_aluno_nao_pode_setar_nota_negativa():
    obj_aluno = aluno.Aluno()

    with pytest.raises(Exception):
        obj_aluno.set_nota1(-1.0)

def test_aluno_nao_pode_setar_nota_maior_que_10():
    obj_aluno = aluno.Aluno()

    with pytest.raises(Exception):
        obj_aluno.set_nota1(11.0)
    
def test_aluno_seta_conceito_corretamente_a():
    obj_aluno = aluno.Aluno()

    obj_aluno.set_conceito(9.0)
    assert obj_aluno.conceito == "a"

def test_aluno_seta_conceito_corretamente_b():
    obj_aluno = aluno.Aluno()

    obj_aluno.set_conceito(7.5)
    assert obj_aluno.conceito == "b"

def test_aluno_seta_conceito_corretamente_c():
    obj_aluno = aluno.Aluno()

    obj_aluno.set_conceito(6.0)
    assert obj_aluno.conceito == "c"

def test_aluno_seta_conceito_corretamente_d():
    obj_aluno = aluno.Aluno()

    obj_aluno.set_conceito(4.0)
    assert obj_aluno.conceito == "d"

def test_aluno_seta_conceito_corretamente_e():
    obj_aluno = aluno.Aluno()

    obj_aluno.set_conceito(0.0)
    assert obj_aluno.conceito == "e"
    
def test_aluno_aprovado_corretamente():
    obj_aluno = aluno.Aluno()

    obj_aluno.set_status_aprovacao("a")
    assert obj_aluno.status_aprovacao

def test_aluno_reprovado_corretamente():
    obj_aluno = aluno.Aluno()

    obj_aluno.set_status_aprovacao("e")
    assert obj_aluno.status_aprovacao == False
    
