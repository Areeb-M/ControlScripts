import rospy


class PrimaryInterface:
    topics = {}
    subscribers = []
    rospy.init_node('')

    def __init__(self):
        pass

    def register_callback(self, topic, callback):
        pass

    def generate_topic(self, topic, data_type):
        global topics

        def topic_callback(data):
            for func in topics[topic]:
                func(data)

        topics[id] = topic_callback
        id += 1


