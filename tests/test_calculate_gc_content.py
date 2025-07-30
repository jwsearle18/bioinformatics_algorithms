import unittest
import sys
sys.path.append('src')
from calculate_gc_content import calculate_gc_content

class TestCalculateGcContent(unittest.TestCase):
    def test_calculate_gc_content(self):
        self.assertAlmostEqual(calculate_gc_content("AGCT"), 50.0)
        self.assertAlmostEqual(calculate_gc_content("GATTACA"), 28.57142857)
        self.assertAlmostEqual(calculate_gc_content(""), 0.0)
        self.assertAlmostEqual(calculate_gc_content("GCGCGC"), 100.0)
        self.assertAlmostEqual(calculate_gc_content("ATATAT"), 0.0)

if __name__ == '__main__':
    unittest.main()
