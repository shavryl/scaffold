import time

from google.cloud import pubsub_v1

project_id = "inetestproject001"
subscription_name = "TestSub"

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_name}`
subscription_path = subscriber.subscription_path(
    project_id, subscription_name)

def callback(message):
    print('Received message: {}'.format(message.data))
    if message.attributes:
        print('Attributes:')
        for key in message.attributes:
            value = message.attributes.get(key)
            print('{}: {}'.format(key, value))
    message.ack()

# Limit the subscriber to ten messages at a time
flow_control = pubsub_v1.types.FlowControl(max_messages=10)

future = subscriber.subscribe(
    subscription_path, callback=callback, flow_control=flow_control)

# Blocks the thread while messages are coming in through the stream. Any
# exceptions that crop up on the thread will be set on the future.
try:
    # Waits indefinitely if not specified
    future.result(timeout=30)
except Exception as e:
    print(
        'Listening for messages on {} threw Exception: {}.'. format(
            subscription_name, e))
