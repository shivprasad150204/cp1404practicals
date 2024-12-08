def repeat_string(s, n):
    """
    Return a string repeated n times.
    >>> repeat_string("abc", 3)
    'abcabcabc'
    >>> repeat_string("hello", 0)
    ''
    """
    return s * n

# Test the function
assert repeat_string("abc", 3) == "abcabcabc"
assert repeat_string("xyz", 0) == ""
