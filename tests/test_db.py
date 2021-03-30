#!/usr/bin/python3
""" aaaa """

import unittest
import mysql.connector
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class testing():
    """ DB class """

    def test_add(self):
        """ xd """
        test = State(name="Facundo")
        self.storage._DBStorage__session.add(test)
        self.storage.save()
        db = MySQLdb.connect(user="hbnb_test",
                             passwd="hbnb_test_pwd",
                             db="hbnb_test_db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE BINARY name = 'Facundo'")
        query = cursor.fetchall()
        self.assertEqual(1, len(query))
        self.assertEqual(st.id, query[0][0])
        cursor.close()
