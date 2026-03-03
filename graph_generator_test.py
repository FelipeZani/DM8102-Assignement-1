import unittest
from main import sampling_without_replacement
import random

random.seed(10)
class TestGraphGenerator(unittest.TestCase):

    def test_sampling_wo_replacement_smallstream(self,):
        S = [(0,1),(0,2)] # G(2,2)
        k = 1
        Sprime = sampling_without_replacement(S,k,10)
        self.assertTrue(Sprime == [(0,1)s] or Sprime == [(0,2)])
    
    def test_reservoir_statistical(self):
        n, k, iterations = 10, 3, 20000
        
        for _ in range(iterations):
            sample = reservoir_sampling(range(n), k)
        
        expected_prob = k / n
        for val in range(n):
            # Use a tolerance for floating point comparison
            self.assertAlmostEqual(actual_prob, expected_prob, delta=0.01)
        


if __name__ == '__main__':
    unittest.main()