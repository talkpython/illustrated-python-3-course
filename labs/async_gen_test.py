import time

import pytest



@pytest.mark.asyncio
async def test_async():
    # Write an asynchronous generator, ``countdown``,
    # that accepts a ``count`` and a ``delay``.
    # When looped over asynchronously, it
    # returns the numbers from ``count`` down to
    # and including 0. It waits for ``delay``
    # seconds before returning the next value.
    # ************************************
    co = countdown(2, 1)
    aiter = co.__aiter__()
    now = time.time()
    val = await co.__anext__()
    assert val == 2
    assert time.time() - now < .5
    now = time.time()
    val = await co.__anext__()
    assert val == 1
    assert time.time() - now >= 1
    val = await co.__anext__()
    assert val == 0
    with pytest.raises(StopAsyncIteration):
        val = await co.__anext__()



if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
