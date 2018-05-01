import unittest
import sys
import os

test_path = os.getcwd()
sys.path.append(test_path)

import scrape_data as sd
class TestData(unittest.TestCase):
    def test_table_clean(self):
        # Test that the table is cleaned properly
        progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs In', 'rookie']
        data = sd.log_data(667, progress_keys)
        found_td = False
        for ele in data:
            if ele == '<td>' or ele == '</td>':
                found_td = True
        self.assertFalse(found_td)

    def test_log_1(self):
        # Test that the correct values are being assigned to each element
        progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
        musher_list = sd.log_data(1, progress_keys)
        self.assertNotEqual(musher_list, [])
        for d in musher_list:
            self.assertIs(type(d['Pos']), int)
            self.assertIs(type(d['Musher']), str)
            self.assertIs(type(d['Dogs']), int)
            self.assertIs(type(d['Bib']), int)
            self.assertIs(type(d['Checkpoint']), str)

    def test_log_2(self):
        # Test that the correct values are being assigned to each element
        progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
        musher_list = sd.log_data(2, progress_keys)
        self.assertNotEqual(musher_list, [])
        for d in musher_list:
            self.assertIs(type(d['Pos']), int)
            self.assertIs(type(d['Musher']), str)
            self.assertIs(type(d['Dogs']), int)
            self.assertIs(type(d['Bib']), int)
            self.assertIs(type(d['Checkpoint']), str)

    def test_log_667(self):
        # Test that the correct values are being assigned to each element
        progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
        musher_list = sd.log_data(667, progress_keys)
        self.assertNotEqual(musher_list, [])
        for d in musher_list:
            self.assertIs(type(d['Pos']), int)
            self.assertIs(type(d['Musher']), str)
            self.assertIs(type(d['Dogs']), int)
            self.assertIs(type(d['Bib']), int)
            self.assertIs(type(d['Checkpoint']), str)

    def test_log_770(self):
        # Test that the correct values are being assigned to each element
        progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
        musher_list = sd.log_data(770, progress_keys)
        self.assertNotEqual(musher_list, [])
        for d in musher_list:
            self.assertIs(type(d['Pos']), int)
            self.assertIs(type(d['Musher']), str)
            self.assertIs(type(d['Dogs']), int)
            self.assertIs(type(d['Bib']), int)
            self.assertIs(type(d['Checkpoint']), str)

if __name__ == '__main__':
    unittest.main()
