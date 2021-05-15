def palindrome(original):
	reverse = original[::-1]
	if original == "":
		return False
	elif original == reverse:
		return True
	else:
		return False