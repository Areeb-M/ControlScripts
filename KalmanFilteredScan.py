import rospy
import numpy as np
import time
from sensor_msgs.msg import LaserScan

rospy.init_node('hello_darkness')
cache = []
AverageData = 0

# Made by Sidharth Babu; Pro Hacker

def data_clean(data):  # Cleaning function; constantly runs
    global cache
    global AverageData
    global pub
    scan_range = np.array(data.ranges)
    cache.append(scan_range)
    if len(cache) > 5:
        del cache[0]
        AverageData = (cache[0] + cache[1] + cache[2] + cache[3] + cache[4]) / 5

    data.ranges = AverageData
    pub.publish(data)




rospy.Subscriber('scan', LaserScan, data_clean, queue_size=1)
pub = rospy.Publisher('filtered', LaserScan, queue_size=1)


while not rospy.is_shutdown():
    time.sleep(0.001)
    #pass