import rospy


class PrimaryInterface:
    topics = {}
    subscribers = []
    rospy.init_node('PrimaryInterface')

    def __init__(self):
        pass

    def register_callback(self, topic, callback):
        topic[topic].append(callback)

    def subscribe_topic(self, topic, data_type, queue_size=1):
        global topics

        def topic_callback(data):
            for func in topics[topic]:
                func(data)

        pub = rospy.Subscriber(topic, data_type, topic_callback, queue_size)
        topics[id] = topic_callback
        id += 1
