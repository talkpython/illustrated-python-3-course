import pytest


def test_kw():
    # One formula for force is mass times acceleration.
    # Create a function, ``force``, that takes 2
    # keyword only arguments: mass & acceleration
    # and returns the product of the arguments.
    # Put this function in a module called py3code.py
    # ***********************************

    from py3code import force
    assert force(mass=10, acceleration=9.8) == 98.0
    assert force(**{'mass': 10, 'acceleration': 9.8}) == 98.0
    with pytest.raises(TypeError):
        force(10, 9.8)

    # The quadratic formula solves an equation
    # of the form:
    #   ax^2 + bx + c = 0
    # Write a function, ``quad``, that returns a
    # tuple with the solutions.
    # Make a, b, and c keyword only arguments.
    # Put this function in a module called py3code.py
    # ***********************************

    from py3code import quad
    assert quad(a=1, b=1, c=1) == pytest.approx(
        ((-0.49999999999999994 + 0.8660254037844386j), (-0.5 - 0.8660254037844386j)))
    assert quad(a=1, b=3, c=1) == pytest.approx((-0.3819660112501051, -2.618033988749895))
    assert quad(a=1, b=0, c=0) == (0.0, 0.0)
    with pytest.raises(TypeError):
        quad(1, 3, 1)


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
