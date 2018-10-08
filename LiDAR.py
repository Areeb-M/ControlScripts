#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import LaserScan


def average_distance(data, a=0, b=270):
    PPD = 4 # points per degree
    data = data[a*PPD:b*PPD]
    arr = np.array(data)
    return arr.mean()


def print_data(data):
    print(average_distance(data.ranges, 120, 150))
    #print(len(data.ranges))
    #print(data.intensities)


rospy.init_node('hello_darkness')
pub = rospy.Subscriber('scan', LaserScan, print_data, queue_size=2)


while not rospy.is_shutdown():
    pass
