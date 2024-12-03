import unittest
from atividade08 import Professor
from atividade08 import Aluno
from atividade08 import Curso

class TestIntegracao(unittest.TestCase):
    def setUp(self):
        # Creating instances of the classes with updated values
        self.curso = Curso("Curso de ADS")
        self.professor = Professor("Luciano Silva", "Engenharia de Software")
        self.curso.professor = self.professor
        self.aluno1 = Aluno("Pedro")
        self.aluno2 = Aluno("Marco")
        self.curso.adicionar_aluno(self.aluno1)
        self.curso.adicionar_aluno(self.aluno2)

    def test_criacao_professor(self):
        # Testing if the professor's name and discipline are correct
        self.assertEqual(self.professor.nome, "Luciano")
        self.assertEqual(self.professor.disciplina, "Engenharia de Software")

    def test_criacao_alunos(self):
        # Testing if the number of students in the course is correct
        self.assertEqual(len(self.curso.listar_alunos()), 2)

    def test_associacao_professor_curso(self):
        # Testing if the professor is correctly associated with the course
        self.assertEqual(self.curso.professor.nome, "Luciano")

    def test_listagem_alunos(self):
        # Testing if the list of students is correct
        alunos = self.curso.listar_alunos()
        self.assertEqual(len(alunos), 2)
        self.assertIn(self.aluno1, alunos)
        self.assertIn(self.aluno2, alunos)

# Fix the typo in the following line to ensure the tests run
if __name__ == "__main__":
    unittest.main()
