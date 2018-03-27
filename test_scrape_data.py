import unittest
import scrape_data as sd

# If time, maybe mock iditarod website?
class TestData(unittest.TestCase):
    def test_table_clean(self):
        pass

    def test_log_data(self):
        progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
        raw = sd.data_collect(667)
        tables = sd.table_clean(raw)
        manual_list = sd.organize_data(tables[0], tables[1], progress_keys)
        manual_list += sd.organize_data(tables[2], tables[3], progress_keys)
        log_list = sd.log_data(667, progress_keys)
        self.assertNotEquals(manual_list, [])
        self.assertNotEquals(log_list, [])
        self.assertEqual(len(log_list), len(manual_list))

    def test_log_1(self):
        progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
        musher_list = sd.log_data(1, progress_keys)
        self.assertNotEquals(musher_list, [])
        for d in musher_list:
            self.assertIs(type(d['Pos']), int)
            self.assertIs(type(d['Musher']), str)
            self.assertIs(type(d['Dogs']), int)
            self.assertIs(type(d['Bib']), int)
            self.assertIs(type(d['Checkpoint']), str)

    def test_log_2(self):
        progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
        musher_list = sd.log_data(2, progress_keys)
        self.assertNotEquals(musher_list, [])
        for d in musher_list:
            self.assertIs(type(d['Pos']), int)
            self.assertIs(type(d['Musher']), str)
            self.assertIs(type(d['Dogs']), int)
            self.assertIs(type(d['Bib']), int)
            self.assertIs(type(d['Checkpoint']), str)

    def test_log_667(self):
        progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
        musher_list = sd.log_data(667, progress_keys)
        self.assertNotEquals(musher_list, [])
        for d in musher_list:
            self.assertIs(type(d['Pos']), int)
            self.assertIs(type(d['Musher']), str)
            self.assertIs(type(d['Dogs']), int)
            self.assertIs(type(d['Bib']), int)
            self.assertIs(type(d['Checkpoint']), str)

    def test_log_770(self):
        progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
        musher_list = sd.log_data(770, progress_keys)
        self.assertNotEquals(musher_list, [])
        for d in musher_list:
            self.assertIs(type(d['Pos']), int)
            self.assertIs(type(d['Musher']), str)
            self.assertIs(type(d['Dogs']), int)
            self.assertIs(type(d['Bib']), int)
            self.assertIs(type(d['Checkpoint']), str)

if __name__ == '__main__':
    unittest.main()
