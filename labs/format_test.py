def test_format():
    # Create a string variable, f1, to show a stock 
    # price. It should have 3 placeholders, using
    # the .format method to print. Given
    # data like:
    #   name = 'AAPL'
    #   price = 171.980
    #   change = .01625
    #
    # It should be able to create:
    # "Name: APPL    Price: $171.98    Change: 1.62%"

    # ***********************************

    assert f1.format('APPL', 171.980, .01625) == \
           'Name: APPL    Price: $171.98    Change: 1.62%'

    # Create f2. It should be like f1, but have
    # 10 spaces for each (left aligned)
    # placeholder
    # ***********************************

    assert f2.format('APPL', 171.980, .01625) == \
           'Name: APPL          Price: $171.98        Change: 1.62%     '

    # Create f3
    # It should have 3 placeholders and should be able
    # to create the f1 or f2 strings. The placeholders
    # accept the formatting strings.
    # ie: '', ':.2f', ':.2%'
    # ***********************************

    assert f3.format('', ':.2f', ':.2%').format(
        'APPL', 171.980, .01625) == \
           'Name: APPL    Price: $171.98    Change: 1.62%'


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
