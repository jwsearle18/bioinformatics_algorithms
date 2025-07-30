import unittest
import sys
sys.path.append('src')
from bwt_matching import bwt_matching

class TestBwtMatching(unittest.TestCase):
    def test_bwt_matching(self):
        bwt = "GGCGCCGC$TAGTCACACACGCCGTA"
        patterns = ["ACC", "CCG", "CAG"]
        expected = [1, 2, 1]
        result = bwt_matching(bwt, patterns)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
