"""
Module containing the "Professor" Class.
"""

from dataclasses import dataclass

from ..pessoas import Pessoa


@dataclass
class Professor(Pessoa):
    """
    Class to represent a professor.

    Attributes
    ----------
    especialidade : str
        The professor's main knowledge.

    Methods
    -------
    toString() -> str
        Method to convert the professor to a string.
    """
    especialidade: str

    def toString(self) -> str:
        """
        Method to convert a professor to a str printable format.

        Returns
        -------
        str
            The professor in str format.
        """
        return f'''
                Nome: {self.nome}
                Especialidade: {self.especialidade}
        ''' 