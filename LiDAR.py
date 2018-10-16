#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import LaserScan


def average_distance(data, a=0, b=270):
    PPD = 4 # points per degree
    data = data[a*PPD:b*PPD]
    arr = np.array(data)
    return arr.mean()


max = -1000
min = 10000000


def print_data(data):
    global max, min
    index = 500
    if data.ranges[index] > max:
        max = data.ranges[index]
    if data.ranges[index] < min:
        min = data.ranges[index]
    print("Max:"+str(max))
    print("Min:"+str(min))

    #print(average_distance(data.ranges, 120, 150))
    #print(len(data.ranges))
    #print(data.intensities)


rospy.init_node('hello_darkness')
pub = rospy.Subscriber('scan', LaserScan, print_data, queue_size=1)


while not rospy.is_shutdown():
    pass
