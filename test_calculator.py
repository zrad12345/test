import unittest
from calculator import multiply


class TestStringMethods(unittest.TestCase):
  
  def test_multiply(self):
    a = 10
    b = 4
    expected = a * b
    
    res = multiply(a)(b)
    
    self.assertEqual(res, expected)
    
   
if __name__ == "__main__":
  unittest.main()
