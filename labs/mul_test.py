def test_mul():
    # Implement a class, Vector, that
    # accepts a list of numbers.
    # Implement the matrix multiplication
    # operator to return the dot product.
    # (multiply each corresponding value, then sum results)
    # ***********************************

    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    assert v1 @ v2 == 32


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
