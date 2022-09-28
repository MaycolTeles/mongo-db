"""
Module containig the "Database" Class.
"""

from pymongo import MongoClient
from pymongo.errors import PyMongoError
from pymongo.collection import Collection

from typing import List

from .aula_db import AulaDB
from ..interfaces import DatabaseInterface
from ..environment import DB_PASSWORD, DB_DATABASE
from ....domain import Aula


class Database(DatabaseInterface):
    """"""
    aula_db: AulaDB

    def __init__(self) -> None:
        """
        Constructor to set up some attributes.
        """
        collection = self.__get_collection()
        self.aula_db = AulaDB(collection)

    def __get_collection(self) -> Collection:
        """
        Private Method to return the mongodb collection.
        """
        connection_string = f"mongodb+srv://root:{DB_PASSWORD}@cluster0.jbnvzk5.mongodb.net/test"

        try:
            client = MongoClient(
                connection_string,
                tlsAllowInvalidCertificates=True
            )

            db = client[DB_DATABASE]

            collection = db.Aulas

            return collection

        except PyMongoError as error:
            print('ERROR WHILE TRYING TO CONNECT TO THE DATABASE')
            print(error)

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
        response = self.aula_db.insert(aula)
        return response

    def read_all(self) -> List[Aula]:
        """
        Method to read all "Aula" objects from the database.

        Returns
        -----------
        List[Aula]
            A list containing all the "Aula" objects found in the database.
        """
        aulas = self.aula_db.read_all()
        return aulas

    def read_by_assunto(self, assunto: str) -> Aula:
        """
        Method to read the "Aula" object from the database
        that matches the 'assunto' received as argument.

        Returns
        -----------
        Aula
            The "Aula" objects found in the database.
        """
        aula = self.aula_db.read_by_assunto(assunto)
        return aula

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
        response = self.aula_db.update_by_assunto(assunto, new_assunto)
        return response

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
        response = self.aula_db.delete_by_assunto(assunto)
        return response
