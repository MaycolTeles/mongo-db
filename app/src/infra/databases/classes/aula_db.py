"""
Module containig the "AulaDB" Class.
"""

from pymongo.collection import Collection

from typing import Any, List

from ..interfaces import DatabaseInterface
from ....domain import Aula


class AulaDB(DatabaseInterface):
    """
    Class to handle all the "Aula"'s objects in the database.
    """
    collection: Collection

    def __init__(self, collection: Collection) -> None:
        """"""
        self.collection = collection

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
        response = self.collection.insert_one(aula.__dict__)

        return True if response else False

    def read_all(self) -> List[Any]:
        """
        Method to read all "Aula" objects from the database.

        Returns
        -----------
        List[Aula]
            A list containing all the "Aula" objects found in the database.
        """
        response = self.collection.find()

        return response

    def read_by_assunto(self, assunto: str) -> Any:
        """
        Method to read the "Aula" object from the database
        that matches the 'assunto' received as argument.

        Returns
        -----------
        Aula
            The "Aula" objects found in the database.
        """
        db_filter_json = {
            "assunto": assunto
        }

        response = self.collection.find_one(db_filter_json)

        return response

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
        db_filter_json = {
            "assunto": assunto
        }

        db_update_json = {
            "$set": {
                'assunto': new_assunto,
            }
        }

        response = self.collection.update_one(
            db_filter_json,
            db_update_json
        )

        return True if response else False

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
        db_filter_json = {
            "assunto": assunto
        }

        response = self.collection.delete_one(db_filter_json)

        return True if response else False
