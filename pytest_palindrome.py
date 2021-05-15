import pytest
import palindrome

# Successful test
def test_empty():
	assert palindrome.palindrome("") == False, "Empty string failed"
# Successful test
def test_racecar():
	assert palindrome.palindrome("racecar"), "racecar failed"

# Failed test
def test_Anna():
	assert palindrome.palindrome("Anna"), "Anna string failed"
# Failed test
def test_spaces():
	assert palindrome.palindrome(" racecar"), "Space + racecar failed"
