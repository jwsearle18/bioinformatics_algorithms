import unittest
import sys
sys.path.append('src')
from burrows_wheeler_transform import burrows_wheeler_transform

class TestBurrowsWheelerTransform(unittest.TestCase):
    def test_burrows_wheeler_transform(self):
        self.assertEqual(burrows_wheeler_transform("GCGTGCCTGGTCA$"), "ACTGGCT$TGCGGC")

if __name__ == '__main__':
    unittest.main()
