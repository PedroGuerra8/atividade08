class Professor:
    def __init__(self, nome, disciplina):
        self.__nome = nome
        self.__disciplina = disciplina

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def disciplina(self):
        return self.__disciplina

    @disciplina.setter
    def disciplina(self, disciplina):
        self.__disciplina = disciplina


class Aluno:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


class Curso:
    def __init__(self, nome):
        self.__nome = nome
        self.__professor = None
        self.__alunos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, professor):
        self.__professor = professor

    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)

    def listar_alunos(self):
        return self.__alunos
