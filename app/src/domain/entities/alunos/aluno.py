"""
Module containing the "Aluno" Class.
"""

from dataclasses import dataclass

from ..pessoas import Pessoa


@dataclass
class Aluno(Pessoa):
    """
    Class to represent a student.

    Attributes
    ----------
    matricula : int
        The student register.

    curso : str
        The student course.

    periodo : int
        The current student semester.

    Methods
    -------
    toString() -> str
        Method to convert the student to a string.
    """
    matricula: int
    curso: str
    periodo: int

    def toString(self) -> str:
        """
        Method to convert a student to a str printable format.

        Returns
        -------
        str
            The student in str format.
        """
        return f'''
                Nome: {self.nome}
                Matricula: {self.matricula}
                Curso: {self.curso}
                Período: {self.periodo}
        '''
