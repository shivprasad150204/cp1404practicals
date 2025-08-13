"""CP1404/CP5632 Practical - Testing and fixing functions with doctest."""
import doctest


def repeat_string(s, n):
    """Return string s repeated n times, separated by spaces.

    >>> repeat_string("hi", 3)
    'hi hi hi'
    """
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """Return True if word length is greater than or equal to the given length.

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_as_sentence(phrase):
    """Format phrase as a sentence with a capital and a full stop.

    >>> format_as_sentence("hello")
    'Hello.'
    >>> format_as_sentence("Hello")
    'Hello.'
    >>> format_as_sentence("hello world.")
    'Hello world.'
    """
    phrase = phrase.strip().capitalize()
    if not phrase.endswith("."):
        phrase += "."
    return phrase


def run_tests():
    """Run basic assert tests for Car fuel."""
    from prac_09.car import Car
    car1 = Car("Test Car", 50)
    assert car1.fuel == 50
    car2 = Car("Empty Car", 0)
    assert car2.fuel == 0
    print("All assert tests passed.")


if __name__ == '__main__':
    run_tests()
    doctest.testmod()
