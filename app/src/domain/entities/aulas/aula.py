"""
Module containing the "Aula" Class.
"""

from dataclasses import dataclass
from typing import List

from ..alunos import Aluno
from ..professores import Professor


@dataclass
class Aula():
    """
    Class to represent a lesson.

    Attributes
    ----------
    assunto : str
        The lesson subject.

    professor : Professor
        A reference to the professor object.

    alunos : List[Aluno]
        A list containing all the students.

    Methods
    --------
    getListaPresenca() -> str
        Method to get the presence list of that lesson.
    """
    assunto: str
    alunos: List[Aluno]
    professor: Professor

    def getListaPresenca(self) -> str:
        """
        Method to return the presence list.

        Returns
        ---------
        str
            The presence list.
        """
        base_string = f'''
            Aula de {self.assunto}
        '''

        professor_string = f'''
            - Professor: 
                {self.professor.toString()}
        '''

        alunos_string = f'''
            - Alunos presentes:
        '''

        for aluno in self.alunos:
            alunos_string += aluno.toString()

        return base_string + professor_string + alunos_string