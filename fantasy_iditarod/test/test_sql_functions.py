import unittest
import sys
import os

test_path = os.getcwd()
sys.path.append(test_path)

import update_insert_sql as sql

class Test_DB(unittest.TestCase):
    def test_connection(self):
        connected = sql.test_connect()
        self.assertTrue(connected)

if __name__ == '__main__':
    unittest.main()
