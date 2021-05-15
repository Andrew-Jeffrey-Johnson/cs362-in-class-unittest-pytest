import unittest
import word_count

class testWordCount(unittest.TestCase):
	# Successful test
	def test_empty(self):
		self.assertEqual(word_count.word_count(""), 0)
	# Successful test
	def test_regular(self):
		self.assertEqual(word_count.word_count("This is an activity."), 4)

	# Failed test
	def test_number(self):
		self.assertEqual(word_count.word_count(123), 1)
	# Failed test
	def test_list(self):
		self.assertEqual(word_count.word_count(["This is a sentence.","This is another sentence."]), 8)

	if __name__ == '__main__':
		unittest.main()
