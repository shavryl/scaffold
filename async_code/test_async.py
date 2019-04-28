import pytest
from async_code.async_testing import f



def test_f(loop):
    # pytest will recognize the "loop" argument here
    # find that name in fixtures and then call our
    # test_f() above with that new loop instance
    # yielded out of the future
    collected_msgs = []

    def dummy_nofify(msg):
        collected_msgs.append(msg)

    loop.create_task(f(dummy_nofify))
    # we're using run_forever to run the loop so this
    # makes sure the loop will actually stop. Alternatively,
    # we might have used run_until_complete(f(...)) without
    # a call_later(); but which you choose depends on what
    # youre testing. For testing side effects, as is the case here,
    # I find it simpler to use run_forever(). On the other hand
    # when you're testing return values from coroutines it's
    # better to use run_until_complete()
    loop.call_later(1, loop.stop)
    loop.run_forever()


    assert collected_msgs[0] == 'Alert!'
