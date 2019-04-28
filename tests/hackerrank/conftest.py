import pytest
import asyncio


@pytest.fixture(scope='function')
def loop():
    loop = asyncio.new_event_loop()
    # once set_event_loop() is called, every subsequent
    # call to asyncio.get_event_loop() will return the
    # loop instance created in this future, and you dont
    # have to explicitly pass the loop instance through
    # all your function calls.
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        loop.close()
