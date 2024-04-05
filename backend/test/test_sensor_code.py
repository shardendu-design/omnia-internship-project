import unittest
import psycopg2
from unittest.mock import patch
import os

# Import the function to be tested
from src.sensor_api.sensor_api_connection import awair_api_call

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.host = 'localhost'
        self.port = int(db_port)
        self.database = db_name
        self.user = db_user
        self.password = db_password

    def test_database_connection(self):
        conn1 = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        conn1.autocommit = True
        cur1 = conn1.cursor()

        self.assertIsNotNone(cur1)
       
class TestCreateDatabase(unittest.TestCase):
    def setUp(self):
        self.host = 'localhost'
        self.port = int(db_port)
        self.database = db_name
        self.user = db_user
        self.password = db_password

    def test_database_connection(self):
        conn1 = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        conn1.autocommit = True
        cur1 = conn1.cursor()

        self.assertIsNotNone(cur1)

        cur1.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'sensordata'")
        exists = cur1.fetchone()

        if not exists:
            cur1.execute("CREATE DATABASE sensordata")

        cur1.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'sensordata'")
        exists_after_creation = cur1.fetchone()
        conn1.set_session(autocommit=True)


        self.assertIsNotNone(exists)
        self.assertIsNotNone(exists_after_creation)


if __name__ == '__main__':
    unittest.main()

    ### python -m unittest -v test/test_sensor_code.py