def test_venv():
    # Use pipenv to create a virtual environment
    # and install pytest.
    # Activate your virtual environment and
    # run pytest on this file::
    #   python venv_test.py

    assert 1


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
