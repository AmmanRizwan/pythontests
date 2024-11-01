# Test Cases For the Problem
import unittest

# import the function to test
from function import add, sub, multiply, divide

# Create a Test Class
class TestArithmetic(unittest.TestCase):
  def test_case_1(self):
    add_num_1, add_num_2 = 2, 3
    self.assertEqual(add(add_num_1, add_num_2), 5)

  def test_case_2(self):
    sub_num_1, sub_num_2 = 3, 9
    self.assertEqual(sub(sub_num_1, sub_num_2), -6)
  
  def test_case_3(self):
    mul_num_1, mul_num_2 = 4, 4
    self.assertEqual(multiply(mul_num_1, mul_num_2), 16)

  def test_case_4(self):
    div_num_1, div_num_2 = 2, 4
    self.assertEqual(divide(div_num_1, div_num_2), 0.5)
  

if __name__ == '__main__':
  unittest.main()
  