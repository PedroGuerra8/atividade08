import unittest
from atividade08 import Professor
from atividade08 import Aluno
from atividade08 import Curso

class TestProfessor(unittest.TestCase):
    def setUp(self):
        # Criando uma instância de Professor
        self.professor = Professor("Luciano", 1)  # ID como número

    def test_get_nome(self):
        # Testando se o nome do professor está correto
        self.assertEqual(self.professor.nome, "Luciano")

    def test_get_id(self):
        # Testando se o ID do professor está correto
        self.assertEqual(self.professor.id, 1)


class TestAluno(unittest.TestCase):
    def setUp(self):
        # Criando uma instância de Aluno
        self.aluno = Aluno("Pedro", 123)  # Supondo que a matrícula seja um número

    def test_get_nome(self):
        # Testando se o nome do aluno está correto
        self.assertEqual(self.aluno.nome, "Pedro")

    def test_get_matricula(self):
        # Testando se a matrícula do aluno está correta
        self.assertEqual(self.aluno.matricula, 123)


class TestCurso(unittest.TestCase):
    def setUp(self):
        # Criando uma instância de Curso e adicionando um professor e alunos
        self.curso = Curso("Curso de ADS")
        self.professor = Professor("Luciano", 1)
        self.curso.adicionar_professor(self.professor)
        self.aluno1 = Aluno("Pedro", 123)
        self.aluno2 = Aluno("Marco", 124)
        self.curso.adicionar_aluno(self.aluno1)
        self.curso.adicionar_aluno(self.aluno2)

    def test_adicionar_aluno(self):
        # Testando se os alunos são adicionados corretamente
        self.assertEqual(len(self.curso.listar_alunos()), 2)
        self.assertEqual(self.curso.listar_alunos()[0], "Pedro")
        self.assertEqual(self.curso.listar_alunos()[1], "Marco")

    def test_get_professor(self):
        # Testando se o professor associado ao curso está correto
        self.assertEqual(self.curso.get_professor().nome, "Luciano")

    def test_listar_alunos(self):
        # Garantindo que a lista de alunos esteja correta
        alunos = self.curso.listar_alunos()
        self.assertEqual(len(alunos), 2)
        self.assertIn("Pedro", alunos)  # Verificando se o nome do aluno está na lista
        self.assertIn("Marco", alunos)

if __name__ == "__main__":
    unittest.main()