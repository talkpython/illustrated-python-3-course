def test_unpack():
    # Merging dictionaries
    #
    # Given the ``coin_value`` dictionary,
    # create a new dictionary, ``new_value``,
    # that has coin_value values, and
    # that has the following keys and values:
    #   'BCH' 1650
    #   'ETH' 1055
    # Use extended unpacking (no dictionary
    # methods or inserts)
    # ***********************************
    coin_value = {'BTC': 11_157,
                  'BCH': 1_439,
                  'ETH': 993}

    assert new_value == {'BCH': 1650, 'BTC': 11157, 'ETH': 1055}

    # Create a set of the keys from
    # new value by unpacking. Put the
    # result in ``coins``
    # ***********************************

    assert coins == {'BCH', 'BTC', 'ETH'}

    # Create a list of the keys from new_value
    # and the other_coins tuple. Put the result
    # in ``all_coins``
    # ***********************************
    other_coins = 'DOGE', 'XRP', 'LTC'

    assert isinstance(all_coins, list)
    assert sorted(all_coins) == ['BCH', 'BTC', 'DOGE', 'ETH', 'LTC', 'XRP']


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
