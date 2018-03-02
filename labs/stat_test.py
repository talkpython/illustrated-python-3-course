

def test_stat():
    # Calculate the mean, variance, and
    # standard deviation of the ``data``
    # array.
    # Store the results in ``m``, ``v``,
    # and ``s``
    # ***********************************
    data = [967, 1190, 1179, 1349, 2328, 2504, 2873, 4764,
            4349, 4353, 9916, 13889]

    assert m == 4138.416666666667
    assert v == 15616030.265151514
    assert s == 3951.712320646774

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
