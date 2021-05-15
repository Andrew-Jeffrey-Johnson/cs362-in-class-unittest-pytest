import unittest
import palindrome

class testPalindrome(unittest.TestCase):
	# Successful test
	def test_empty(self):
		self.assertEqual(palindrome.palindrome(""), False)
	# Successful test
	def test_racecar(self):
		self.assertEqual(palindrome.palindrome("racecar"), True)

	# Failed test
	def test_Anna(self):
		self.assertEqual(palindrome.palindrome("Anna"), True)
	# Failed test
	def test_spaces(self):
		self.assertEqual(palindrome.palindrome(" racecar"), True)

	if __name__ == '__main__':
		unittest.main()
