import rospy


topics = {}
modifiers = {}
callbacks = {}
subscribers = []


def register_callback(topic, callback):
    global callbacks
    callbacks[topic].append(callback)


def register_modifier(topic, modifier):
    global modifiers
    modifiers[topic].append(modifier)


def subscribe_topic(topic, data_type, queue_size=1):
    global topics, subscribers, modifiers, callbacks

    def topic_callback(data, arg):
        for func in modifiers[topic]:
            data = func(data)

        for func in callbacks[topic]:
            func(data)

    pub = rospy.Subscriber(topic, data_type, topic_callback, queue_size)
    topics[topic] = topic_callback
    callbacks[topic] = []
    modifiers[topic] = []
    subscribers.append(pub)
    print("Subscribed to " + topic)