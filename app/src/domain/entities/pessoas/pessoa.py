"""
Module containing the "Pessoa" Class.
"""

from dataclasses import dataclass


@dataclass
class Pessoa():
    """
    Class to represent a person.

    Attributes
    -----------
    nome : str
        The person name.
    """
    nome: str
