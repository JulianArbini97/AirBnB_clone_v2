#!/usr/bin/python
"""Unittests for DBStorage class of AirBnb_Clone_v2"""
import unittest
import pep8
import os
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import MySQLdb


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db',
    "Only for DBStorage")
class TestDBStorage(unittest.TestCase):
    """test of the class DBStorage"""

    @classmethod
    def User_def(cls):
        """Tests"""
        cls.user = User()
        cls.user.first_name = "Name"
        cls.user.last_name = "Last"
        cls.user.email = "abc@def.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """delete of the user"""
        del cls.user

    def json_file_remover(self):
        """json file remover"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8(self):
        """Tests pep8 style"""
        code = pep8.StyleGuide(quiet=True)
        text = code.check_files(['models/engine/db_storage.py'])
        self.assertEqual(text.total_errors, 0, "pep8 needs fix")

    def test_all(self):
        """DBStorage general testing"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """new test"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.name = "Name"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_dbtorage(self):
        """ reload test """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except Exception:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
