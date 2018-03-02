
def test_unpack():
    # Unpacking
    #
    # Given the tuple, ``person``, unpack
    # the values into name, age, and country.
    # ***********************************

    person = ('Candide', 30, 'France')

    assert (name, age, country) == ('Candide', 30, 'France')

    # Extended Unpacking
    #
    # Use unpacking to get the first letter
    # of name. Store the result in ``first``
    # ***********************************

    assert first == 'C'

    # Unpack the characters from ``name`` into a
    # list called ``letters``
    # ***********************************

    assert letters == ['C', 'a', 'n', 'd', 'i', 'd', 'e'] 

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
