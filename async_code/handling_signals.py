import asyncio
from signal import SIGINT, SIGTERM



async def main():
    try:
        while True:
            print('your app is running')
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        # when the cancellation signal is received,
        # there will be a period of three seconds while
        # main() will continue running during the
        # run_until_complete() phase of shutdown process
        for i in range(3):
            print('your app is shutting down...')
            await asyncio.sleep(1)

def handler(sig):
    # the primary purpose of the handler is to stop the loop:
    # this will unblock the loop.run_forever() call and allow
    # pending-task collection, cancellation and the run_complete
    # for shutdown
    loop.stop()
    print(f'Got signal: {sig!s}, shutting down.')
    # since we are now in shutdown mode, we dont want another
    # SIGINT or SIGTERM to trigger this handler again: that would
    # call loop.stop during the run_until_complete() phase which
    # would interfere with our shutdown process. Therefore, we
    # remove the signal handler for SIGTERM from the loop
    loop.remove_signal_handler(SIGTERM)
    # we cant simply remove the handler for SIGINT, because in that
    # case KeyboardInterrupt will again become the handler for
    # SIGINT, the same as it was before we added our own handlers.
    # Instead we set an empty lambda function as the handler.
    # This means that KeyboardInterrupt stays away, and SIGINT
    # and CTRL+C has no effect
    loop.add_signal_handler(SIGINT, lambda: None)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # note thas by setting a handler on SIGINT, a KeyboardInterrupt
    # will no longer be raised on SIGINT. The raising of a
    # KeyboardInterrupt is the default handler for SIGINT as if
    # configured until you do something to change the handler
    for sig in (SIGTERM, SIGINT):
        loop.add_signal_handler(sig, handler, sig)
    loop.create_task(main())
    loop.run_forever()
    tasks = asyncio.Task.all_tasks()
    for t in tasks:
        t.cancel()
    group = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(group)
    loop.close()
