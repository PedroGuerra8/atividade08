import unittest
from atividade08 import Professor
from atividade08 import Aluno
from atividade08 import Curso

class TestIntegracao(unittest.TestCase):
    def setUp(self):
        # Criando instâncias das classes
        self.curso = Curso("Curso de ADS")
        self.professor = Professor("Luciano", 1)  # ID do professor como um número
        self.curso.adicionar_professor(self.professor)  # Adicionando o professor ao curso
        self.aluno1 = Aluno("Pedro", 123)  # Supondo que a matrícula seja um número
        self.aluno2 = Aluno("Marco", 124)
        self.curso.adicionar_aluno(self.aluno1)
        self.curso.adicionar_aluno(self.aluno2)

    def test_criacao_professor(self):
        # Testando se o nome do professor está correto
        self.assertEqual(self.professor.nome, "Luciano")
        self.assertEqual(self.professor.id, 1)  # Verificando o ID do professor

    def test_criacao_alunos(self):
        # Testando se o número de alunos no curso está correto
        self.assertEqual(len(self.curso.listar_alunos()), 2)

    def test_associacao_professor_curso(self):
        # Testando se o professor está corretamente associado ao curso
        self.assertEqual(self.curso.get_professor().nome, "Luciano")

    def test_listagem_alunos(self):
        # Testando se a lista de alunos está correta
        alunos = self.curso.listar_alunos()
        self.assertEqual(len(alunos), 2)
        self.assertIn("Pedro", alunos)  # Verificando se o nome do aluno está na lista
        self.assertIn("Marco", alunos)

# Executa os testes se o script for chamado diretamente
if __name__ == "__main__":
    unittest.main()