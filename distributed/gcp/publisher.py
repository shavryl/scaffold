from google.cloud import pubsub_v1


# export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"


project_id = "inetestproject001"
topic_name = "VasyaKolya"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

topic = publisher.create_topic(topic_path)

print('Topic created: {}'.format(topic))

