"""
Module containing some environment variables.
"""

import os

from dotenv import load_dotenv


load_dotenv()


DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')

DB_DATABASE = os.getenv('DB_DATABASE', 'database')
