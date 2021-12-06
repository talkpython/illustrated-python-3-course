import pytest


def test_exception():
    # Define a customized Exception,
    # ``ColorError``, that subclasses
    # ``RuntimeError``.
    # ***************************************

    assert isinstance(ColorError(), RuntimeError)

    # Create a function, ``err_wrap``,
    # that takes a function (``fn``), ``*args``,
    # and ``**kwargs``.
    # It should call and return the
    # result of:
    #  fn(*args, **kwargs)
    # If an exception is raised,
    # it will use the ``raise from``
    # exception chaining to wrap the
    # error with ``ColorError``.
    # ***************************************

    assert err_wrap(lambda x, y: x + y, 2, 3) == 5

    with pytest.raises(ColorError) as ctx:
        err_wrap(lambda x, y: x / y, 2, 0)
    assert isinstance(ctx.value.__context__,
                      ZeroDivisionError)

    with pytest.raises(ColorError) as ctx:
        def raise2():
            raise KeyError

        err_wrap(raise2)
    assert isinstance(ctx.value.__context__,
                      KeyError)


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
