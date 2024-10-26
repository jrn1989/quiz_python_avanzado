import pytest

#from palindrome import is_palindrome  # Assuming your function is in a file named palindrome.py

def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]
 

# Test cases for the is_palindrome function

@pytest.mark.parametrize("word, expected", [

    ("radar", True),          # Single word palindrome

    ("hello", False),        # Single word palindrome


])

def test_is_palindrome(word, expected):

    # Using assert to check if the function result matches the expected output

    assert is_palindrome(word) == expected
    #assert is_palindrome("hello") == False