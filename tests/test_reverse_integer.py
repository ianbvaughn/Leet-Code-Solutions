import unittest
import reverse_integer

class Test(unittest.TestCase):
 def test_str_reverse(self):
  self.assertEqual(reverse_integer.reverse(123),321)
 def test_return_0_for_exceeds_limit(self):
  self.assertEqual(reverse_integer.reverse(1534236469),0)