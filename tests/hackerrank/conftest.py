import pytest
import asyncio


@pytest.fixture(scope='function')
def loop():
    loop = asyncio.new_event_loop()
    try:
        yield loop
    finally:
        loop.close()
