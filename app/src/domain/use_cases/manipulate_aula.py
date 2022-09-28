"""
Module containing the "ManipulateAula" Class.
"""

from typing import List

from ..entities import Aula
from ...infra import DatabaseInterface
from ...presenters import CLI


class ManipulateAula(DatabaseInterface):
    """
    Class to manipulate "Aula" objects related to the database.
    """
    presenter: CLI
    database: DatabaseInterface

    def __init__(self, database: DatabaseInterface, presenter: CLI) -> None:
        """
        Constructor to set up some attributes.

        Parameters
        -----------
        database : DatabaseInterface
            A reference to the database object.
        """
        self.database = database
        self.presenter = presenter

    def insert(self, aula: Aula) -> bool:
        """
        Method to insert an "Aula" object into the database.

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
        response = self.database.insert(aula)

        if response:
            return self.presenter.show_insert_ok()

        return self.presenter.show_insert_error()

    def read_all(self) -> List[Aula]:
        """
        Method to read all "Aula" objects from the database.

        Returns
        -----------
        List[Aula]
            A list containing all the "Aula" objects found in the database.
        """
        aulas = self.database.read_all()

        if aulas:
            return self.presenter.show_all_ok(aulas)

        return self.presenter.show_all_error()

    def read_by_assunto(self, assunto: str) -> Aula:
        """
        Method to read the "Aula" object from the database
        that matches the 'assunto' received as argument.

        Returns
        -----------
        Aula
            The "Aula" objects found in the database.
        """
        aula = self.database.read_by_assunto(assunto)

        if aula:
            return self.presenter.show_one_ok(aula)

        return self.presenter.show_one_error()

    def update_by_assunto(self, assunto: str, new_assunto: str) -> bool:
        """
        Method to update the "Aula" object from the database
        that matches the 'assunto' received as argument.

        Parameters
        -----------
        assunto : str
            The "Aula"'s assunto.

        new_assunto : str
            The "Aula"'s new assunto.

        Returns
        -----------
        bool
            - True if the object was successfully updated in the database;
            - False otherwise.
        """
        aula = self.database.update_by_assunto(assunto, new_assunto)

        if aula:
            return self.presenter.show_update_ok()

        return self.presenter.show_update_error()

    def delete_by_assunto(self, assunto: str) -> bool:
        """
        Method to delete an "Aula" object from the database
        based on its 'assunto' received as argument.

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
        response = self.database.delete_by_assunto(assunto)

        if response:
            return self.presenter.show_delete_ok()

        return self.presenter.show_delete_error()
