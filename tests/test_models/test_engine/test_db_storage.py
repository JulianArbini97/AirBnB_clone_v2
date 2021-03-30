#!/usr/bin/python3
""" xxxddd """

import pep8
import models
import MySQLdb
import unittest

class test_db_storage(unittest.TestCase):
    """ xd """
    
def test_add(self):
    """ xdxd """
    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"), getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cant1 = 0
    cant2 = 0
    for instance in session.query(State).order_by(State.id):
        cant1 = cant1 + 1
    new = State()
    for instance in session.query(State).order_by(State.id):
        cant2 = cant2 + 1
    self.assertEqual(cant1 + 1, cant2)
