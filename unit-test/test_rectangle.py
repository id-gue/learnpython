import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
	"""Tests for `rectangle.py`."""

	def test_size_is_six(self):
		"""What is a rectangle area with length 3 and width 2? Six"""
		length = 3
		width = 2
		size = rectangle.calc_area(length, width)
		self.assertEqual(size, 6)

	def test_size_is_72(self):
		"""What is a rectangle area with length 8 and width 9? 72"""
		length = 8
		width = 9
		size = rectangle.calc_area(length, width)
		self.assertEqual(size, 72)

	def test_size_is_float(self):
		"""What is a rectangle area with length 1,5 and width 2,5? 3,75"""
		length = 1.5
		width = 2.5
		size = rectangle.calc_area(length, width)
		self.assertEqual(size, 3.75)	

	def test_side_is_negative(self):
		"""What is a rectangle area with length -2 and width 5? ValueError"""
		length = -2
		width = 5
		with self.assertRaises(ValueError):
			rectangle.calc_area(length, width)

	def test_side_is_0(self):
		"""What is a rectangle area with length 0 and width 2? ValueError"""
		length = 0
		width = 2
		with self.assertRaises(ValueError):
			rectangle.calc_area(length, width)

	def test_side_is_string(self):
		"""What is a rectangle area with length a and width 3? TypeError"""
		length = 'a'
		width = 3
		with self.assertRaises(TypeError):
			rectangle.calc_area(length, width)

	def test_side_is_boolean(self):
		"""What is a rectangle area with length a and width 3? TypeError"""
		length = False
		width = 3
		with self.assertRaises(TypeError):
			rectangle.calc_area(length, width)

if __name__ == '__main__':
	unittest.main()

