import unittest
import sys
sys.path.append('src')
from frequent_words_with_mismatches import frequent_words_with_mismatches

class TestFrequentWordsWithMismatches(unittest.TestCase):
    def test_frequent_words_with_mismatches(self):
        text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
        k = 4
        d = 1
        expected = ["GATG", "ATGC", "ATGT"]
        result = frequent_words_with_mismatches(text, k, d)
        self.assertCountEqual(result, expected)

        text = "AAAAAAAAAA"
        k = 2
        d = 1
        expected = ["AA"]
        result = frequent_words_with_mismatches(text, k, d)
        self.assertCountEqual(result, expected)

        text = "AGTCAGTC"
        k = 4
        d = 0
        expected = ["AGTC"]
        result = frequent_words_with_mismatches(text, k, d)
        self.assertCountEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
