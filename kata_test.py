import unittest
from kata import Kata

class TestKata(unittest.TestCase):
	def setUp(self):
		self.kata = Kata()
	def test_convertToRoman(self):
		expected = "IX"
		result = self.kata.convertToRoman(9)
		self.assertEqual(result, expected)
	def test_convertToRoman_outOfBounds(self):
		expected = "Your number is either too big or too small!"
		result = self.kata.convertToRoman(2000000000)
		self.assertEqual(result, expected)
	def test_convertToRoman_TypeError(self):
		with self.assertRaises(TypeError):
			self.kata.convertToRoman("This is not a number")
	
if __name__ == "__main__":
	unittest.main()