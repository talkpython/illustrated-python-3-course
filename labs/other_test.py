def test_other():
    # Lazy range
    #
    # Get the 100th item from
    # the vals variable. Store
    # it in a variable named ``hun``.
    # ***********************************

    vals = range(42, 2_000_000, 32)

    assert hex(hun) == '0xcaa'

    def fn(x):
        return x + 10

    # Map
    #
    # Find the 100th item from mapping
    # ``fn`` to ``vals`` using ``map``.
    # Store the result in ``hun_fn``.
    # ***********************************

    assert chr(hun_fn) == 'ಔ'

    # Sorting
    #
    # Sort the ``nums`` list as if they
    # were integers. Store the result in
    # ``ordered``.
    # Hint (look at sorted and the keys
    # parameter)
    # ***********************************
    nums = [42, -1, '24', 99.9]


    assert ordered == [-1, '24', 42, 99.9]

    # Name leakage
    #
    # Sum the square of the numbers in nums,
    # Store the result in ``sq_sum``
    # ***********************************
    num = 42
    x = 38

    assert sq_sum == 12142
    assert x == 38
    assert num == 42
    


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

