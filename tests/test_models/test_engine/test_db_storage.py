#!/usr/bin/python3

import unittest
import pep8
from models import Amenity
from models import State
from models import City
from models import Place
from models import User
from models import Review
from models.engine.db_storage import DBStorage
from os import environ


class TestDBStorage(unittest.TestCase):
    """Tests the DBStorage class"""