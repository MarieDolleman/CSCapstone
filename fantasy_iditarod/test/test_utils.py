import unittest
import sys
import os

test_path = os.getcwd()
sys.path.append(test_path)

import utils

class Test_utils(unittest.TestCase):
    def test_sim_logs(self):
        # Test that the correct number of log numbers are returned
        logs = utils.sim_log_nums()
        self.assertEqual(len(logs), 23)

    def test_is_date(self):
        # Test that the date finding function is correct
        date = utils.is_date('3/4 4:45:23')
        not_date = utils.is_date('Musher')
        self.assertTrue(date)
        self.assertFalse(not_date)
    
    def test_is_float(self):
        # Test that the float finding function is correct
        fl = utils.is_float('3.43')
        not_fl = utils.is_float('3')
        also_not_fl = utils.is_float('Musher')
        date = utils.is_float('3:4:45')
        self.assertTrue(fl)
        self.assertFalse(not_fl)
        self.assertFalse(also_not_fl)
        self.assertFalse(date)


if __name__ == '__main__':
    unittest.main()
