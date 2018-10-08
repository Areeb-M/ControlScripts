#!/usr/bin/env python
import rospy

pub = rospy.SubscribeListener('/scan')

while True:
    print(pub)