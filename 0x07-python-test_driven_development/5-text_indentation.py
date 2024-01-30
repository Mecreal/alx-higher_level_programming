#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of these
characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of
    these characters: ., ? and :

    Args:
        text: string, the text to be idented

    Raises:
        TypeError: If the text is not a string.
    """

    i = 0

    if not isinstance(text, (str)):
        raise TypeError("text must be a string")

    while i < len(text):
        print("{:s}".format(text[i]), end="")
        if text[i] in [":", "?", "."]:
            print("\n")
            i = i + 1 if text[i] == " " else i
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
