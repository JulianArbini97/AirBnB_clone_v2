#!/usr/bin/python3
""" xxxddd """

import pep8
from models.state import State
import MySQLdb
import unittest
from models.engine.db_storage import DBStorage

class test_db_storage(unittest.TestCase):
    """ xd """
    
    def test_add(self):
        """ xdxd """

        MY_H = "localhost"
        MY_U = "root"
        MY_P = "root"
        MY_D = "hbnb_dev_db"

        print(MY_D, MY_H, MY_P, MY_U)

        nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)

        consulta = nuevaconexion.cursor()
        consulta.execute("SELECT * FROM states")
        resultado = consulta.fetchall()
        cant1 = 0
        cant2 = 0
        for fila in resultado:
            cant1 = cant1 + 1

        new = State()
        State.name = "California"
        self.storage = DBStorage()
        self.storage.reload()

        consulta2 = nuevaconexion.cursor()
        consulta2.execute("SELECT * FROM states")
        resultado2 = consulta2.fetchall()
        for fila in resultado2:
            cant2 = cant2 + 1

        self.assertEqual(cant1 + 1, cant2)
