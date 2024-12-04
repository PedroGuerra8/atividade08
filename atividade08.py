import unittest

class Professor:
    def __init__(self, nome, id):
        self.__nome = nome  # Nome do professor (privado)
        self.__id = id      # Identificador único do professor (privado)

    @property
    def nome(self):
        return self.__nome
    
    @property
    def id(self):
        return self.__id

class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome
    
    @property
    def matricula(self):
        return self.__matricula

class Curso:
    def __init__(self, nome):
        self.__nome = nome  # Nome do curso (privado)
        self.__professor = None  # Instância da classe Professor (privado)
        self.__alunos = []  # Lista de instâncias da classe Aluno (privado)

    @property
    def nome(self):
        return self.__nome

    def adicionar_professor(self, professor):
        self.__professor = professor

    def remover_professor(self):
        self.__professor = None

    def get_professor(self):
        return self.__professor

    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)

    def remover_aluno(self, matricula):
        self.__alunos = [aluno for aluno in self.__alunos if aluno.matricula != matricula]

    def listar_alunos(self):
        return [aluno.nome for aluno in self.__alunos]

    def listar_professor(self):
        return self.__professor.nome if self.__professor else None