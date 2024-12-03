from atividade08 import Professor
from atividade08 import Aluno
from atividade08 import Curso
import unittest

class TestProfessor(unittest.TestCase):
    def setUp(self):
        self.professor = Professor("Luciano", "Engenharia de Software")

    def test_get_nome(self):
        self.assertEqual(self.professor.nome, "Luciano")

    def test_get_disciplina(self):
        self.assertEqual(self.professor.disciplina, "Engenharia de Software")


class TestAluno(unittest.TestCase):
    def setUp(self):
        self.aluno = Aluno("Pedro")

    def test_get_nome(self):
        self.assertEqual(self.aluno.nome, "Pedro")


class TestCurso(unittest.TestCase):
    def setUp(self):
        self.curso = Curso("Curso de ADS")
        self.professor = Professor("Luciano", "Engenharia de Software")
        self.curso.professor = self.professor
        self.aluno1 = Aluno("Pedro")
        self.aluno2 = Aluno("Marco")
        self.curso.adicionar_aluno(self.aluno1)
        self.curso.adicionar_aluno(self.aluno2)

    def test_adicionar_aluno(self):
        # Test if students are added correctly
        self.assertEqual(len(self.curso.listar_alunos()), 2)
        self.assertEqual(self.curso.listar_alunos()[0].nome, "Pedro")
        self.assertEqual(self.curso.listar_alunos()[1].nome, "Marco")

    def test_get_professor(self):
        self.assertEqual(self.curso.professor.nome, "Luciano")

    def test_listar_alunos(self):
        # Ensure the list of students is correct
        alunos = self.curso.listar_alunos()
        self.assertEqual(len(alunos), 2)
        self.assertIn(self.aluno1, alunos)
        self.assertIn(self.aluno2, alunos)

if __name__ == "__main__":
    unittest.main()
