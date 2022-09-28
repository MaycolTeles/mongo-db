"""
Module containing the "DatabaseInterface" Interface.
"""

from abc import ABC, abstractmethod
from typing import List

from ....domain import Aula


class DatabaseInterface(ABC):
    """
    Interface to represent an Database.
    """

    @abstractmethod
    def insert(self, aula: Aula) -> bool:
        """
        Abstract Method to insert an "Aula" object into the database.

        This method must be implemented in all classes that wants
        to implement the 'DatabaseInterface' Interface.

        Parameters
        -----------
        aula : Aula
            A reference to the "Aula" object.

        Returns
        --------
        bool
            - True if the object was successfully stored in the database;
            - False otherwise.
        """

    @abstractmethod
    def read_all(self) -> List[Aula]:
        """
        Abstract Method to read an "Aula" object from the database.

        This method must be implemented in all classes that wants
        to implement the 'DatabaseInterface' Interface.

        Returns
        -----------
        Aula
            A reference to the "Aula" object.
        """

    @abstractmethod
    def read_by_assunto(self, assunto: str) -> Aula:
        """
        Abstract Method to read an "Aula" object from the database
        based on its 'assunto' received as argument.

        This method must be implemented in all classes that wants
        to implement the 'DatabaseInterface' Interface.

        Parameters
        -----------
        assunto : str
            The "Aula"'s assunto.

        Returns
        -----------
        Aula
            A reference to the "Aula" object.
        """

    @abstractmethod
    def update_by_assunto(self, assunto: str, new_assunto: str) -> bool:
        """
        Abstract Method to update an "Aula" object into the database
        based on its 'assunto' received as argument.

        This method must be implemented in all classes that wants
        to implement the 'DatabaseInterface' Interface.

        Parameters
        -----------
        assunto : str
            The "Aula"'s assunto.

        aula : Aula
            The "Aula"'s new assunto.

        Returns
        -----------
        bool
            - True if the object was successfully updated in the database;
            - False otherwise.
        """

    @abstractmethod
    def delete_by_assunto(self, assunto: str) -> bool:
        """
        Abstract Method to delete an "Aula" object from the database
        based on its 'assunto' received as argument.

        This method must be implemented in all classes that wants
        to implement the 'DatabaseInterface' Interface.

        Parameters
        -----------
        assunto : str
            The "Aula"'s assunto.

        Returns
        -----------
        bool
            - True if the object was successfully deleted from the database;
            - False otherwise.
        """
