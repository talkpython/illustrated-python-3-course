from pathlib import Path


def test_ann():
    """
    0. Make a copy of py3code.py to py3code.pyORIG
    1. Use virtualenv/pip to install mypy
    2. Run::

      mypy --strict py3code.py

    3. Try to annotate the issues to address them.
    4. Run py3code.py with test code::

      mypy py3code.py --strict --ignore-missing-imports labs/super_test.py labs/keyword_test.py

    5. Fix any additional issues in py3code.py
       (If they are not false positives)

    """
    p = Path('py3code.pyORIG')
    assert p.exists()


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
