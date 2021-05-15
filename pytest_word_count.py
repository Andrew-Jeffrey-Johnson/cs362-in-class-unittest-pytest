import pytest
import word_count

# Successful test
def test_empty():
	assert word_count.word_count("") == 0, "Empty string failed"
# Successful test
def test_regular():
	assert word_count.word_count("This is an activity.") == 4, "Regular sentence failed"

# Failed test
def test_number():
	assert word_count.word_count(123) == 1, "Number failed"
# Failed test
def test_list():
	assert word_count.word_count(["This is a sentence.","This is another sentence."]) == 8, "List failed"
