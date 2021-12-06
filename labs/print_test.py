"""
In Python 3, ``print`` is a function. You can provide the
name arguments:

* sep - String to insert between each argument (' ' default)
* end - String to insert at end ('\n' default)
"""

from io import StringIO
import sys


def test_print1():
    out = StringIO()
    sys.stdout = out
    # Print the numbers from 10 down to 0
    # with a space between them
    # (and newline at the end)
    # ***********************************
    nums = list(range(10, -1, -1))

    assert out.getvalue() == '10 9 8 7 6 5 4 3 2 1 0\n'


def test_print2():
    out = StringIO()
    sys.stdout = out
    # Print the numbers from 10 down to 0
    # with a "-*-" between them
    # (and no newline at the end)
    # ***********************************
    nums = list(range(10, -1, -1))

    assert out.getvalue() == '10-*-9-*-8-*-7-*-6-*-5-*-4-*-3-*-2-*-1-*-0'


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
