import pytest


def get_average(li):
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean

# test_exception.py


def palindrome(word):
    if not isinstance(word, str):
        raise TypeError('Please provide a string argument')
    return word == word[::-1]


def test_palindrom():
    with pytest.raises(TypeError):
        palindrome(44)
