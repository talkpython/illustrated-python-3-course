def test_fstring():
    # Assuming the variables ``stock`` and ``price``
    # exist, make a variable ``res`` that
    # has:
    #   Stock: STOCK_VAL Price: PRICE_VAL
    # You should use an fstring to do this
    # ***********************************
    stock = 'APPL'
    price = 171.98

    assert res == 'Stock: APPL Price: 171.98'

    # Assume the variable ``x`` exists.
    # Create a variable, ``answer``, that
    # has the sine of x (using math.sin)
    # to two decimal places:
    #   x: X sin(x): SINE_RESULT
    # You should use an fstring to do this
    # ***********************************
    x = 0

    assert answer == 'x: 0 sin(x): 0.00'


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
