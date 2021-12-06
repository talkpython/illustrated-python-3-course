import time

import pytest


@pytest.mark.asyncio
async def test_async():
    # Write an asynchronous context manager,
    # ``staller``. It should accept a time in seconds.
    # When the context is entered it should
    # pause for that many seconds ( call ``asyncio.sleep``).
    # ************************************

    now = time.time()
    async with staller(1):
        then = time.time()
        assert then - now >= 1

    # Write an asynchronous context manager,
    # ``closer``. It should accept an object
    # and call the ``.close`` method on it
    # when the context exits.
    # ************************************

    class CloseMe:
        closed = False

        def close(self):
            self.closed = True

    c = CloseMe()
    async with closer(c):
        pass
    assert c.closed


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
